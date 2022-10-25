from flask import Flask
from .views import views
from .auth import auth

def create_app():
  app = Flask(__name__)

  app.config["SECRET_KEY"] == "I dont know any random word so i will give it anything"

  app.register_blueprint(views)
  
  app.register_blueprint(auth)

  return app
