admin-dev:
	docker-compose -f docker-compose.yaml exec django-admin make admin


run-dev:
	docker-compose -f docker-compose.yaml up -d


stop-dev:
	docker-compose -f docker-compose.yaml down
