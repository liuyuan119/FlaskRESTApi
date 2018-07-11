from App.ext import db
from App.utils import BaseModel

PERMISSION_READ = 1
PERMISSION_WRITE = 2


class User(BaseModel, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(16), unique=True)
    u_password = db.Column(db.String(256))
    is_active = db.Column(db.Boolean, default=False)
    u_token = db.Column(db.String(128), nullable=True)
    u_permission = db.Column(db.Integer, default=0)

    # 用户权限
    # 权限设计
    # 2 的 n 次方
    # 1 2 4 8 16 32 ...
    # 1 读权限
    # 2 写权限
    # 4 删除

    def check_permission(self, permission):
        return self.u_permission & permission == permission
