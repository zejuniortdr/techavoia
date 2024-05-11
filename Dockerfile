FROM python as base

ENV PYTHONUNBUFFERED 1
ENV TZ 'America/Sao_Paulo'

ARG REQUIREMENTS="--system"

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && pipenv install ${REQUIREMENTS}

COPY manage.py ./
COPY apps ./apps
COPY conf ./conf
COPY staticfiles ./staticfiles

RUN python /app/manage.py collectstatic --noinput

COPY utils/docker/entrypoint.sh /entrypoint.sh
COPY utils/docker/wait_for_redis.py /wait_for_redis.py

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
