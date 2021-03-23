from flask import Flask, request
from flask_restful import Api, Resource, reqparse


from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/BDD_Video"
db = SQLAlchemy(app)
# db.
# videos = {}


class Video(Resource):
    def __init__(self):
        self.videos_args = reqparse.RequestParser()
        self.videos_args.add_argument(
            "title", type=str, help="Name of the video is required", required=True)
        self.videos_args.add_argument(
            "views", type=int, help="Name of the video is required", default=0)
        self.videos_args.add_argument(
            "likes", type=int, help="Name of the video is required", default=0)

    # CREATE
    def post(self):
        pass

    # READ
    def get(self, video_id):
        return videos[video_id]

    # UPDATE
    def put(self, video_id):
        videos[video_id] = request.form['likes']
        return videos

    # DELETE
    def delete(self, video_id):
        pass


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
