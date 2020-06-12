black:
	black api

flake8:
	flake8 api

pytest:
	pytest api

run-local:
	FLASK_APP=api FLASK_ENV=development flask run

run-local-dev:
	FLASK_APP=api flask run

build:
	docker build -t sbard/maven-api .

run:
	docker run -p 5000:5000 sbard/maven-api

push:
	docker push sbard/maven-api

post:
	@curl -H "Content-Type: application/json" --data '{"number": ${NUM}}' --request POST 127.0.0.1:5000

put:
	@curl -H "Content-Type: application/json" --data '{"number": ${NUM}, "increment_value": ${INC}}' --request PUT 127.0.0.1:5000

run-remote:
	docker run --rm -p 5000:5000 docker.io/sbard/maven-api