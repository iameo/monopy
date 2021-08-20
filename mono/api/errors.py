
class MonoAPIException(Exception):
    pass

class MonoAuthException(MonoAPIException):
    pass

class HttpMethodException(MonoAPIException):
    pass