# coding=utf-8

from file_management import BadRequestException, UnAuthorizedException, \
    ForbiddenException, NotFoundException

from hyip.extensions.custom_exception import  *

def before_send(event, hint):
    """
    Ignore custom exception
    """
    if 'exc_info' in hint:
        exc_type, exc_value, tb = hint['exc_info']
        if isinstance(exc_value, (
                BadRequestException, UnAuthorizedException, ForbiddenException,
                NotFoundException, UserExistsException, InvalidLoginTokenException,
                DomainExistsException,
                ProjectNotFoundException)):
            return None
    return event