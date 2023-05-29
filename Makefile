init:
	make start_local_services
	poetry install
	make make_migrations_migrate
	make create_su_user

start_local_services:
	docker-compose -f ./local.yml up -d db

test:
	make start_local_services
	poetry run python ./manage.py test

make_migrations_migrate:
	poetry run python ./manage.py makemigrations
	poetry run python ./manage.py migrate

create_su_user:
	DJANGO_SUPERUSER_USERNAME="admin" DJANGO_SUPERUSER_PASSWORD="q1w2e3w2e3" DJANGO_SUPERUSER_EMAIL="admin@test.ru" poetry run python ./manage.py createsuperuser --noinput

run_server:
	poetry run python ./manage.py runserver

run_server_docker:
	docker-compose -f local.yml up --build django
