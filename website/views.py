from flask import Blueprint

views = Blueprint("views", __name__)

@views.route("/")
def test():
  return "<h1> Welcome <h1>"