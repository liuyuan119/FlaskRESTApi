from flask_restful import Api
from App.apis.BlogApi import BlogResource
from App.apis.UserApi import UserResource, UsersResource

api = Api()


def init_api(app):
    api.init_app(app)


# 添加资源
api.add_resource(UserResource, "/users/")
api.add_resource(UsersResource, "/users/<int:id>/")

api.add_resource(BlogResource, "/blogs/")
