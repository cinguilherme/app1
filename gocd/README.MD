#### IMAGES FOR GOCD ####
https://www.gocd.org/download/#docker


#### base image ubuntu ####
docker run -d -e GO_SERVER_URL=... gocd/gocd-agent-ubuntu-18.04:v19.12.0

### BUILD IMAGES
#### build base agent to run jobs for python3
```
    docker build -f Dockerfile-pytest-agent -t gocd-agent-pytest:latest . 
```
#### run container with agent for pytest
```

docker run -d -e GO_SERVER_URL=https://$(docker inspect --format='{{(index (index .NetworkSettings.IPAddress))}}' nifty_keller):8154/go gocd-agent-pytest:latest
```

#### GOCD infra docker SERVER ####
```
docker run -d -p8153:8153 -p8154:8154 gocd/gocd-server:v19.12.0
```


###### MISC 
```
docker run -d -e GO_SERVER_URL=https://0.0.0.0:8154/go gocd/gocd-agent-alpine-3.10:v19.12.0

docker run -d -e GO_SERVER_URL=https://$(docker inspect --format='{{(index (index .NetworkSettings.IPAddress))}}' nifty_keller):8154/go gocd/gocd-agent-alpine-3.10:v19.12.0

GO_SERVER_URL=https://$(docker inspect --format='{{(index (index .NetworkSettings.IPAddress))}}' godc-server):8154/go

```

