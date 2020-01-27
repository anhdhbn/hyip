import datetime
import os

import jwt


def encode_token(email, minute):
    from hyip.extensions.custom_exception import EncodeErrorException

    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=minute),
            'email': email,
        }
        return jwt.encode(
            payload,
            os.environ['SECRET_KEY'],
            algorithm='HS256'
        ).decode("utf-8")
    except Exception as e:
        raise EncodeErrorException()


def decode_token(auth_token):
    from hyip.extensions.custom_exception import InvalidTokenException
    try:
        payload = jwt.decode(auth_token, os.environ['SECRET_KEY'])
        return payload['email']
    except:
        raise InvalidTokenException()
