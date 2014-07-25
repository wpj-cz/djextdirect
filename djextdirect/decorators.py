# coding=utf-8
from functools import wraps
import json
from django.http import Http404


def require_authorization(func):
    @wraps(func)
    def _decorator(request, *args, **kwargs):
        # Auth by session
        if request.user and request.user.is_authenticated():
            return func(request, *args, **kwargs)

        # Try to auth by username and password from request.body
        try:
            rawjson = json.loads(request.body)
        except ValueError:
            raise Http404("Invalid request")

        username = rawjson.get('username', None)
        password = rawjson.get('password', None)
        if username and password:
            from django.contrib.auth import authenticate, login
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)

                return func(request, *args, **kwargs)
        raise Http404("Invalid password")
    return _decorator