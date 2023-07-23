#!/bin/bash
if poetry lock && poetry install; then
    if python manage.py collectstatic --no-input; then
        if python manage.py migrate; then
            echo "SUCCESSFULLY CONFIGURED SERVER! 🎊"
        else
            echo "ERROR: Unable to Intialized Database"
        fi
    else
        echo "ERROR: Unable to Collect Static"
    fi
else
    echo "ERROR: Unable to Install App Requirements"
fi
nhhc/init.shchm od