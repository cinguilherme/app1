build-image:
	sudo docker build . -t app1:latest

build-gocd-images:
	docker build -f gocd/Dockerfile-pytest-agent -t gocd-agent-pytest:latest . 

run:
	sudo docker-compose up

start-gocd:
	docker run --name gocd-server -d -p8153:8153 -p8154:8154 gocd/gocd-server:v19.12.0 
	docker run -d -e GO_SERVER_URL=https://$(docker inspect --format='{{(index (index .NetworkSettings.IPAddress))}}' gocd-server):8154/go gocd-agent-pytest:latest

wip:
	git add . && git commit -m "shameless wip commit" && gp