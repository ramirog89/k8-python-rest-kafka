.PHONY = build local deploy forward

APPLICATION_NAME	= python-demo-app
CONTAINER_NAME		= python-api
CONTAINER_PORT		= 8000
KAFKA_TOPIC			= events
NAMESPACE			= testing


build:
	docker build --progress=plain -t $(APPLICATION_NAME) .

local:
	docker run --name $(CONTAINER_NAME) -p $(CONTAINER_PORT):$(CONTAINER_PORT) $(APPLICATION_NAME)

deploy:
	kubectl	apply -k ./k8s

forward:
	kubectl port-forward service/$(APPLICATION_NAME) $(CONTAINER_PORT) -n $(NAMESPACE)

