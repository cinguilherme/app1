
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

#### flask SqlAlchemy
its ready to use. But with some grunt work to be done. create a db called test and a schema called test. Have all of this properly hooked in the application.


#### Milestones:

ready to production in for heroku? google? aws? kubernets friendly?

integration with MQs? NTH

### Websockets?? 
#### flask-socketio
(youtube video about flask-socketio)[https://www.youtube.com/watch?v=RdSrkkrj3l4]
the bads, so far: the socketio will be a commom dependency between this back-end app and the frontend.
###### some problems are up in regards to using websocket. Both api mode and websocket is not gonna fly. by it self it already seems like a possibility to have 1 application for websocket and another for rest-API


### NoSQL??? 
some dependencies were added to be possible to use mongodb

Redis??

ready docker infra for local development in any machine.


#### flask cheat-sheets
https://www.youtube.com/redirect?q=http%3A%2F%2Fprettyprinted.com%2Fflaskcheatsheet%2F&redir_token=2tSg9aEYaBIXZNrhEmv8V_VkxLh8MTU3OTg3NTk4NUAxNTc5Nzg5NTg1&v=RdSrkkrj3l4&event=video_description
