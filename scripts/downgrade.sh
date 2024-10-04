#!/bin/bash
docker-compose exec backend alembic downgrade "-1"