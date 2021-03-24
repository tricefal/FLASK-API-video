from flask_restful import Resource, reqparse, marshal_with, fields
from models import Video_info

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
        # videos[video_id] = request.form['likes']
        # return videos

    # DELETE
    def delete(self, video_id):
        pass
