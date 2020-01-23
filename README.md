
This is a sample application using flask-restful with the sole purpose of exploring and testing development of web rest api using Python in 2020

its using a python 3.6 environment

Its using a out of knowlegde DB solution abstracted under Flask-SQLAlcemy.

docker-compose is using postgres for local development.

Postman colection of requests are versionated as well.

## overall linux macos
#### in linux, have sudo su enabled to avoid issues with docker.

#### VS CODE section

Useful commands FOR VS CODE

Open the Command Palette (Command+Shift+P on macOS and Ctrl+Shift+P on Windows/Linux) and type in one of the following commands:

Command	Description
Python: Select Interpreter	Switch between Python interpreters, versions, and environments.
Python: Start REPL	Start an interactive Python REPL using the selected interpreter in the VS Code terminal.
Python: Run Python File in Terminal	Runs the active Python file in the VS Code terminal. You can also run a Python file by right-clicking on the file and selecting Run Python File in Terminal.
Python: Select Linter	Switch from Pylint to Flake8 or other supported linters.
Format Document	Formats code using the provided formatter in the settings.json file.
Python: Configure Tests	Select a test framework and configure it to display the Test Explorer.

#####################################


#### GOCD infra docker ####

```
docker run -d -p8153:8153 -p8154:8154 gocd/gocd-server:v19.12.0
```

```
docker run --name gocd-server -d -e GO_SERVER_URL=https://0.0.0.0:8154/go gocd/gocd-agent-alpine-3.10:v19.12.0

docker run -d -e GO_SERVER_URL=https://$(docker inspect --format='{{(index (index .NetworkSettings.IPAddress))}}' gocd-server):8154/go gocd/gocd-agent-alpine-3.10:v19.12.0
```

### customized agent for python related jobs
``` 
docker run -d -e GO_SERVER_URL=https://$(docker inspect --format='{{(index (index .NetworkSettings.IPAddress))}}' gocd-server):8154/go gocd-agent-pytest:latest

```

#### Milestones:

ready to production in for heroku? google? aws? kubernets friendly?

integration with MQs? NTH

### Websockets?? 
#### flask-socketio
(youtube video about flask-socketio)[https://www.youtube.com/watch?v=RdSrkkrj3l4]
the bads, so far: the socketio will be a commom dependency between this back-end app and the frontend.

#### flask cheat-sheets
https://www.youtube.com/redirect?q=http%3A%2F%2Fprettyprinted.com%2Fflaskcheatsheet%2F&redir_token=2tSg9aEYaBIXZNrhEmv8V_VkxLh8MTU3OTg3NTk4NUAxNTc5Nzg5NTg1&v=RdSrkkrj3l4&event=video_description

NoSQL???

Redis??

ready docker infra for local development in any machine.
