#!/bin/sh

alembic upgrade head

uvicorn main:app --host ${FASTAPI_HOST} --port ${FASTAPI_PORT}