MT940 to JSON – HTTP Service in Docker
======================================

We use the https://github.com/WoLpH/mt940 library to convert MT940 to JSON.

Use `make` to build the docker container and `make run` to start the service.

To convert a MT940 to JSON:

```
curl -X POST \
  http://localhost:8000 \
  -d '
:20:STARTUMSE
.... Content from MT940 ....
'
```