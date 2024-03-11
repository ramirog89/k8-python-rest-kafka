## SETUP

You can use the Makefile to build the image by running `make build`.

For the application deployment you can check the `k8s/apps/python-demo-app` files to put it in your cluster. The important part is the `config.yaml` which has the dependency configurations.

One IMPORTANT thing is that, you must have kafka running and the defined `KAFKA_TOPIC` already created so python api can connect properly.

When you send messages to the topic, you'll see them inspecting the `python-api` pod logs.

## MANGAGE KAFKA TOPIC

Login to pod/kafka-broker

```
kubectl exec -it pod/kafka-broker-{id} -n namespace -- /bin/bash
```

CREATE THE TOPIC
```
kafka-topics.sh --bootstrap-server kafka-broker-service:9092 --topic events --create
kafka-topics.sh --bootstrap-server kafka-broker-service:9092 --list
```

SEND MESSAGES TO TOPIC
```
kafka-console-producer.sh --broker-list kafka-broker-service:9092 --topic events
```

NOTE: I left kafka-service as `NodePort` in case you want to test it locally.


## READ/WRITE POSTGRES (demo1)

READ
```
curl -X 'GET' 'http://localhost:8000/demo1' -H 'accept: application/json'
```

WRITE
```
curl -X 'POST' \
  'http://localhost:8000/demo1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "data": "some event data",
  "event_type": "event type"
}'
```

## READ/WRITE MONGODB (demo2)

READ 
```
curl -X 'GET' 'http://localhost:8000/demo2' -H 'accept: application/json'
```

WRITE
```
curl -X 'POST' \
  'http://localhost:8000/demo2' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "data": "string",
  "event_type": "string"
}'
```
