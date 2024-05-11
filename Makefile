
run:
	docker compose up -d


stop:
	docker compose down


create_admin:
	docker compose exec app python manage.py createsuperuser

load_fixtures:
	docker compose exec app python manage.py loaddata apps/articles/fixtures/initial_data.json

dumpdata:
	docker compose exec app python manage.py dumpdata articles > apps/articles/fixtures/initial_data.json

setup:
	cp .env-example .env
