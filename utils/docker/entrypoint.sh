#!/bin/bash
set -e

wait_for_redis(){
    python /app/manage.py shell < /wait_for_redis.py
}

run_migrations() {
    python /app/manage.py migrate
}


if [ "$1" = 'celery' ]; then
    shift
    export PYTHONPATH='/app'
    celery -A celery_worker worker --loglevel=info

elif [ "$1" = 'celery-beat' ]; then
    shift
    export PYTHONPATH='/app'
    celery -A celery_worker worker --loglevel=info

elif [ "$1" = 'debug' ]; then
    run_migrations &&
    exec tail -f /dev/null

elif [ "$1" = 'local' ]; then
    wait_for_redis &&
    run_migrations &&
    exec python /app/manage.py runserver 0.0.0.0:9000
fi
