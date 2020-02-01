# coding=utf-8




def before_send(event, hint):
    """
    Ignore custom exception
    """
    from hyip.extensions.exceptions import BadRequestException, UnAuthorizedException, \
    ForbiddenException, NotFoundException
    if 'exc_info' in hint:
        exc_type, exc_value, tb = hint['exc_info']
        if isinstance(exc_value, (
                BadRequestException, UnAuthorizedException, ForbiddenException,
                NotFoundException)):
            return None
    return event