## Environment Setup

Fastapi Clean Architecture (SOLID Principle)

local :

```sh
$ cd backend
$ poetry shell
$ poetry install
$ alembic init -t async migrations
$ alembic revision --autogenerate -m "init"
$ alembic upgrade head
$ cd src
$ uvicorn main:app --host 0.0.0.0 --port 8888 --reload  
```

container :

```sh
$ cd docker
$ bash build-backend.sh
$ docker-compose up -d backend
$ docker-compose exec backend alembic init -t async migrations
$ docker-compose exec backend alembic revision --autogenerate -m "init"
$ docker-compose exec backend alembic upgrade head
```