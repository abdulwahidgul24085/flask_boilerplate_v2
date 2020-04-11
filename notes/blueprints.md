# Blueprints
1. Blueprints allow you to break your applications in **componenets**.
2. Namespacing for routes becomes easy. E.g. admin blueprint will be namescaped `/admin`.
3. templates, and routes will be neatly contained.
4. Maintainability becomes super easy.
5. Easy shareability between flask application, since blueprints are python packages.

## creating and using a blueprints
In the blueprints folder in the app folder create a `blueprint_name`
Import blueprints in the `app.py` by typing `from app.blueprints.blueprint_name import blueprint_name`
To register a blueprint in the `app.py` by typing `app.register_blueprint(blueprint_name)`
In the blueprint `__init__.py` include the blueprint using the following code `from app.blueprints.blueprint_name.views import blueprint_name`
create the following files in the blueprint
1. __init__.py
2. templates/blueprint_name This for preventing overright from the base templates
3. views.py

All the other files that a flask applicaiton has been created a blueprint for consistance of the package or needs.