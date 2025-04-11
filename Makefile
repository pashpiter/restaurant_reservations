app-up:
	@echo "Starting FastAPI app ..."
	cd app && uvicorn main:app --reload

up:
	@echo "Docker compose up"
	docker compose up -d --build

stop:
	@echo "Docker compose stop"
	docker compose stop

restart:
	@echo "Docker compose deleting containers, volumes and restart"
	docker compose down && \
	docker volume rm restaurant_reservations_postgres_data && \
	docker compose up -d --build