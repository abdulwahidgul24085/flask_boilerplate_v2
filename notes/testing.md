# Testing in python in the context of flask application
The fundamental idea of testing are 2 fold.
1. Make sure the code does what it suppose to do. That is not taking values that does not expect. Also, making sure always perform the function with the correct value. 
2. When the code base increase or new compnenets are added to the code base. How well do they function with the current compments.

To explain both the concept with an example. Lets say we have a users table take some information about the users and create their account. Know that at some point we want multiple type of users in our app. We introduce the roles components, we can right test for the roles and user interaciton components to see that they work, and only revisit them if we want extend the functionality.

## Running pytest in docker
This inscription will be replaced with the command-line `click` package. But for consistance sake, you can run commands against a docker container termainal as follows
`docker-compose exec container_name py.test`

## Writing tests with flask
In the app folder create a tests folder. Also in the route of the tests folder create a `conftest.py` file. This file is useful for create a flask instance for test and also a header less browser for using the app.

In the test folder, have a folder for each blueprint to run its tests in it. create a test_module.py name file.
1. import the modules that you need from flask, e.g. `from flask import url_for`
2. create a class with `Test` prefix with the name of the blueprint, e.g. `class TestBlueprintname(object)`
3. create a function for each test that you want to run

## Test coverage tool
The idea of test coverage is to see if our code is being test for all the functionality. For a large project it is not possible to have 100% coverage, as compare to a small project. But the close we are to 100% the more confident we can be about our tests. To use the coverage test we can use the following code to see the report. The output can also be in HTML. This exmaple is based on the idea that your app is containerized.
`docker-compose container_name_compose_service py.test --cov-report term-missing --cov name_of_project_containing_test`
`docker-compose website py.test --cov-report term-missing --cov app`
There is vscode plug-in way of doing it.


## Static analysis tool for our code
We have vscode plug-in for this. using `pip install flake8` and run document formation on this file. But with the command way is to formating on all of the files in the current project. To run the test we can use 
`docker-compose exec website flake8 .`
To ignore the warning for imported and unused use the following command
`docker-compose exec website flake8 . --exclude __init__.py`