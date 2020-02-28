from collections import OrderedDict, MutableMapping

from flask_restx.model import RawModel as OriginalRawModel
from jsonschema import Draft4Validator
from jsonschema.exceptions import ValidationError




class RawModel(OriginalRawModel):
    def validate(self, data, resolver=None, format_checker=None):
        validator = Draft4Validator(self.__schema__, resolver=resolver,
                                    format_checker=format_checker)
        try:
            validator.validate(data)
        except ValidationError:
            from hyip.extensions.exceptions import BadRequestException
            raise BadRequestException(message='Input payload validation failed',
                                      errors=dict(self.format_error(e) for e in
                                                  validator.iter_errors(data)))


class Model(RawModel, dict, MutableMapping):
    pass


class OrderedModel(RawModel, OrderedDict, MutableMapping):
    wrapper = OrderedDict
