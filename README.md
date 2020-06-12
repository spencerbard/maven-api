# maven-api

- To test: `python -m venv env; source env/bin/activate; pip install -r requirements.txt; make pytest;`
- To build: `make build`
- To run: `make run`
- Test POST (when api is running): `NUM={some_number} make post`
- Test PUT (when api is running): `NUM={some_number} INC={some_inc} make put`
