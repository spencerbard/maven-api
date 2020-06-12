black:
	black api

flake8:
	flake8 api

isort:
	isort -rc --atomic api

pytest:
	pytest api

run-local:
	FLASK_APP=api FLASK_ENV=development flask run

run-local-dev:
	FLASK_APP=api flask run

build:
	docker build -t sbard/maven-api .

run:
	docker run -p 127.0.0.1:5000:5000 sbard/maven-api

push:
	docker push sbard/maven-api