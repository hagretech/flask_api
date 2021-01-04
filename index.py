from flask import Flask
from flask_restful import Api, abort, Resource, reqparse

app = Flask(__name__)
api = Api(app)

vid_put_args = reqparse.RequestParser()
vid_put_args.add_argument('name', type=str, help='nave is not found', required=True)
vid_put_args.add_argument('likes', type=int, help='likes is not found', required=True)
vid_put_args.add_argument('views', type=int, help='views are not found', required=True)
videos = {}

def if_vid_exit(vid_id):
    if vid_id not in videos:
        abort(404, message='video doesn\'t exist')



class videosRoute(Resource):
    def get(self, vid_id):
        if_vid_exit(vid_id)
        return videos[vid_id]

    def put(self, vid_id):
        args = vid_put_args.parse_args()
        videos[vid_id] = args
        return videos[vid_id]

 
api.add_resource(videosRoute, '/video/<int:vid_id>')
if __name__ == "__main__":
    app.run(debug=True)
