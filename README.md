
This is a sample application using flask-restful with the sole purpose of exploring and testing development of web rest api using Python in 2020

its using a python 3.6 environment

Its using a out of knowlegde DB solution abstracted under Flask-SQLAlcemy.

docker-compose is using postgres for local development.

Postman colection of requests are versionated as well.

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
docker run -d -e GO_SERVER_URL=https://0.0.0.0:8154/go gocd/gocd-agent-alpine-3.10:v19.12.0

docker run -d -e GO_SERVER_URL=https://$(docker inspect --format='{{(index (index .NetworkSettings.IPAddress))}}' nifty_keller):8154/go gocd/gocd-agent-alpine-3.10:v19.12.0

```

#### Milestones:

ready to production in for heroku?
ready to hookup with GOCD?
ready to hookup with travis maybe?
ready to hookup with an free CircleCI pipeline to run tests
ready docker infra for local development in any machine.
