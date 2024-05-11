
run:
	docker compose up


stop:
	docker compose down


create_admin:
	docker compose exec app python /app/manage.py createsuperuser

load_fixtures:
	docker compose exec app python /app/manage.py loaddata /app/articles/fixtures/initial_data.json

dumpdata:
	docker compose exec app python /app/manage.py dumpdata articles > /app/articles/fixtures/initial_data.json

setup:
	cp .env-example .env
