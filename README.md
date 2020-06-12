# maven-api

- To test: `python -m venv env; source env/bin/activate; pip install -r requirements.txt; make pytest;`
- To build: `make build`
- To run: `make run`

- Test POST: `curl -H "Content-Type: application/json" --data '{"number": 1}' --request POST 127.0.0.1:5000`
- Test PUT: `curl -H "Content-Type: application/json" --data '{"number": 1, "increment_value": 3}' --request PUT 127.0.0.1:5000`
