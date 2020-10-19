from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#######################
#### Configuration ####
#######################

# Create the instances of the Flask extensions (flask-sqlalchemy) in
# the global scope, but without any arguments passed in.  These instances are not attached
# to the application at this point.
db = SQLAlchemy()

######################################
#### Application Factory Function ####
######################################

def create_app(config_filename=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_pyfile(config_filename)
	initialize_extensions(app)
	register_blueprints(app)
	return app

##########################
#### Helper Functions ####
##########################

def initialize_extensions(app):
	# Since the application instance is now created, pass it to each Flask
	# extension instance to bind it to the Flask application instance (app)
	db.init_app(app)
	# Flask configuration
	from project.item_model import Item

def register_blueprints(app):
	# Since the application instance is now created, register each Blueprint
	# with the Flask application instance (app)
	from project.api import api_blueprint

	app.register_blueprint(api_blueprint)
