def get_db_uri(dbinfo):
    db = dbinfo.get("DB") or "mysql"
    driver = dbinfo.get("DRIVER") or "pymysql"
    user = dbinfo.get("USER") or "root"
    password = dbinfo.get("PASSWORD") or "root"
    host = dbinfo.get("HOST") or "localhost"
    port = dbinfo.get("PORT") or "3306"
    name = dbinfo.get("NAME")
    return "{}+{}://{}:{}@{}:{}/{}".format(db, driver, user, password, host, port, name)


class Config:
    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_TYPE = "redis"

    SECRECT_KEY = "123"


class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        "DB": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "1190",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "RESTApi"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):
    TESTING = True

    DATABASE = {
        "DB": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "1190",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "RESTApi"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StagingConfig(Config):
    DATABASE = {
        "DB": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "1190",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "RESTApi"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
    DATABASE = {
        "DB": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "1190",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "RESTApi"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}
