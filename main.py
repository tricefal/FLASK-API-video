from flask import Flask, request
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/BDD_Video"
db = SQLAlchemy(app)
# db.
videos = {}


class Video_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, default=1)
    likes = db.Column(db.Integer, default=1)

    def __repr__(self):
        return f"Video : (title={self.title}, views={self.views}, likes={self.likes})"

# db.create_all()


resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer,
}


class Video_api(Resource):
    def __init__(self):
        self.videos_args = reqparse.RequestParser()
        self.videos_args.add_argument(
            "title", type=str, help="Name of the video is required", required=True)
        self.videos_args.add_argument(
            "views", type=int, help="Number of views of the video", default=0)
        self.videos_args.add_argument(
            "likes", type=int, help="Number of likes on the video", default=0)
        

    # CREATE
    def post(self):
        pass

    # READ
    @marshal_with(resource_fields)
    def get(self, video_id=0):
        if video_id:
            result = Video_info.query.filter_by(id=video_id).first()
        else:
            result = Video_info.query.order_by(Video_info.id).all()
        return result

    # UPDATE
    def put(self, video_id):
        pass
        # videos[video_id] = request.form['likes']
        # return videos

    # DELETE
    def delete(self, video_id):
        pass


api.add_resource(Video_api, "/video/", "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
