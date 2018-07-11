from flask import request, g
from flask_restful import Resource, abort

from App.models import User, PERMISSION_WRITE, PERMISSION_READ


def login_required(fun):
    def f(*args, **kwargs):
        u_token = request.args.get("u_token")

        if u_token:

            users = User.query.filter(User.u_token.__eq__(u_token)).all()

            if users:

                return fun(*args, **kwargs)

            else:
                abort(401, message="用户状态失效")
        else:

            abort(401, message="用户未登录")

    return f


def check_permission(permission):

    def check(fun):

        def f(*args, **kwargs):

            u_token = request.args.get("u_token")

            if u_token:

                users = User.query.filter(User.u_token.__eq__(u_token)).all()

                if users:

                    user = users[0]

                    if user.check_permission(permission):

                        g.user = user

                        return fun(*args, **kwargs)

                    else:

                        abort(403, message="你没有权限操作此模块")

                else:

                    abort(401, message="用户状态已失效")
            else:

                abort(401, message="用户暂未登录")
        return f
    return check


class BlogResource(Resource):

    @login_required
    def get(self):

        return {"msg": "这是你的这堆博客"}

    @check_permission(PERMISSION_READ)
    def post(self):
        user = g.user

        print(user)

        return {"msg": "写文章啊写文章"}


