from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

vid_args = reqparse.RequestParser()
vid_args.add_argument("name", type='str', help='you need to add the name', required=True)
vid_args.add_argument("likes", type='int', help='you need to add the likes', required=True)
vid_args.add_argument("view", type='int', help='you need to add the views', required=True)

videos = {}


class videosRoute(Resource):
    def get(self, vid_id):
        return videos[vid_id]

    def put(self, vid_id):
        args = vid_args.parse_args()
        return {args}


api.add_resource(videosRoute, '/<int:vid_id>')
if __name__ == "__main__":
    app.run(debug=True)
