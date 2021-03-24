from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/BDD_Video"
db = SQLAlchemy(app)

# To avoid circular import in infinite loop : DB & Video_api
from video import Video_api






class Signup_activate(Resource):
    def post(self, username=""):
        print("username : ",username)
        return username


api.add_resource(Video_api, "/video/", "/video/<int:video_id>")
api.add_resource(Signup_activate, "/signup/activate/<string:username>")

if __name__ == "__main__":
    app.run(debug=True)
