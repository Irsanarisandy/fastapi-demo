## How to setup the docker container

```bash
# make sure that docker is running on the system beforehand
# if use on Linux, make sure to prefix the docker commands with "sudo"

# create and start the docker container (can add "-d" flag to run in background)
docker compose up
```

Once run, it will detect changes and automatically reload if there's any. FastAPI includes an interactive API document which can be accessed locally in http://localhost/docs.

When API is started, the default will be http://localhost/states which will list all states and its average prices. Can also access specific state, e.g. http://localhost/states/nsw .
