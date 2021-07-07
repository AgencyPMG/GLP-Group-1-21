build:
	docker build -t semfeed-api:latest .
up:
	docker run --name s01 -dp 5000:5000 semfeed-api
stop:
	docker stop s01
clear:
	docker container prune
entry:
	docker exec -it s01 bash
