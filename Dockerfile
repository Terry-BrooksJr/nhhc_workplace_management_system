# Use a Python 3.12 base image
FROM python:3.12-slim
LABEL maintainer="Terry Brooks, Jr."
 
# Set environment variables
ARG TOKEN
ARG DOPPLER_PROJECT='nhhc'
ARG DOPPLER_CONFIG='prod'
ENV DOPPLER_TOKEN=${TOKEN}
ENV DOPPLER_PROJECT=${DOPPLER_PROJECT}
ENV DOPPLER_CONFIG=${DOPPLER_CONFIG}
ARG DOPPLER_VERSION=3.69.0
ENV DB_CERT_PATH=/src/app/postgres_ssl.crt

# Install necessary dependencies and Doppler CLI
RUN apt update && apt upgrade -y && apt install -y \
    apt-transport-https \
    ca-certificates \
    apache2-utils \
    curl \
    gnupg \
    cron \
    libmagic1 \
    libssl-dev \
    libenchant-2-dev \
    make \
    git \
    gcc \ 
    musl-dev \ 
    libffi-dev


# Install Doppler CLI
RUN curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | \
    gpg --dearmor -o /usr/share/keyrings/doppler-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/doppler-archive-keyring.gpg] https://packages.doppler.com/public/cli/deb/debian any-version main" | \
    tee /etc/apt/sources.list.d/doppler-cli.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends doppler=$DOPPLER_VERSION && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 8080


# Create necessary groups and users 
RUN groupadd --system celery && \
    useradd -g celery celery && \
    groupadd --system nhhc && \
    useradd --home-dir /src/app --no-create-home -g nhhc nhhc_app

# Copy and install requirements
COPY --chown=nhhc_app:nhhc ./requirements.txt ./requirements.txt
COPY --chown=nhhc_app:nhhc nhhc/Makefile /src/app/Makefile

# Copy the application code
COPY --chown=nhhc_app:nhhc nhhc/ /src/app/


# Install application dependencies]
RUN  pip install -U  cffi pip setuptools && \
    pip install -r ./requirements.txt

# Set up Doppler directory permissions
RUN mkdir -p /src/app/.doppler && \
    chown nhhc_app:nhhc /src/app/.doppler && \
    chmod 775 /src/app/.doppler

    # Use non-root user
USER nhhc_app

# Copy additional files
COPY --chown=nhhc_app:nhhc ./digital_ocean_postgres_ssl.crt /src/postgres_ssl.crt


# Set the shell to bash
SHELL ["/bin/bash", "-c"]

ENTRYPOINT [ "doppler run -- python3" ]

# Healthcheck command
HEALTHCHECK --interval=60s --timeout=120s --start-period=60s --retries=5 \
    CMD curl -f http://localhost:8080/status/SX2g8DpabBBA1KlZTRcb50F5DtUh2_XUQVSkhU_3_Bc/ || exit 1

# Command to run the Gunicorn server
CMD ["gunicorn", "--workers=3", "--threads=2", "nhhc.wsgi:application", "-b", ":7772"]
