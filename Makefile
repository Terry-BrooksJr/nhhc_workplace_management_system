# Define constants
# DEV_ENV_RUNNING_IN_CONTAINER ?= false
VENV_DIR := $(if $(DEV_ENV_RUNNING_IN_CONTAINER), /workspaces/nhhc_workplace_management_system/.venv, /Users/terry-brooks/Documents/GitHub/nhhc_workplace_management_system/.venv)
PYTHON := python3
BIN := $(VENV_DIR)/bin
PYTHON_INTERPRETER := $(BIN)/$(PYTHON)
SHELL := /bin/bash
CURRENT_DATE := $(shell date +"%Y-%m-%d-%T")
TOKEN := ${NHHC_DT}
DOCKER_PATH := $(CONTAINER_PATH_EX)

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY:
venv: ## Make a new virtual environment
	python3 -m venv $(VENV) && source $(BIN)/activate

.PHONY: collect
collect:
	doppler -t $(TOKEN) run -- python  $(PYTHON_INTERPRETER) $(DOCKER_PATH)***manage.py collectstatic --no-input

.PHONY: install
install: ## Make venv and install requirements
	pip install -r ./requirements.txt


freeze: ## Pin current dependencies
	$(BIN)/pip freeze > ../requirements.txt

migrate: ## Make and run migrations
	doppler run -t $(TOKEN)  --  	$(PYTHON_INTERPRETER) $(DOCKER_PATH)manage.py makemigrations
	doppler run -t $(TOKEN)  --  	$(PYTHON_INTERPRETER) $(DOCKER_PATH)manage.py migrate

lint:
	doppler run -t $(TOKEN)  --  prospector  -w  pylint pyroma mypy dodgy mccabe bandit profile-validator > prospector_results_${CURRENTDATE}.json

db-shell: ## Access the Postgres Docker database interactively with psql. Pass in DBNAME=<name>.
	docker exec -it container_name psql -d $(DBNAME)

.PHONY: workers
workers:
	cd nhhc/
	doppler run -t $(TOKEN)  --  celery -A nhhc worker --without-heartbeat --without-gossip --without-mingle -D --loglevel debug

.PHONY: test
test: ## Run tests
	doppler run -- coverage run $(DOCKER_PATH)manage.py test web employee portal  --verbosity=2 --keepdb   --failfast  --force-color

.PHONY: test
pipeline-test: ## Run tests
	${VIRTUAL_ENV}/bin/python $(DOCKER_PATH)manage.py test web employee portal  --verbosity=2  --keepdb   --force-color


.PHONY: flower
flower:
	nohup doppler run -t $(TOKEN)  --  celery -A nhhc flower --port=9005

.PHONY: run
run:
	doppler run -t $(TOKEN)  --  	$(PYTHON_INTERPRETER) $(DOCKER_PATH)manage.py runserver 9555

.PHONY: debug
debug: ## Run the Django server
	doppler run -t $(TOKEN)  --  	kolo run $(DOCKER_PATH)manage.py runserver --noreload --nothreading

.PHONY: admin
admin:
	doppler run -t $(TOKEN)  --   $(PYTHON_INTERPRETER) manage.py createsuperuser --no-input

.PHONY: start
start:
	doppler run -t $(TOKEN)  --  gunicorn --workers=2  --threads=2 nhhc.nhhc.wsgi:application -b :7772
