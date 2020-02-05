# coding=utf-8
import logging
import os
import sys

from dotenv import load_dotenv

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

_DOT_ENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(_DOT_ENV_PATH)
# create settings object corresponding to specified env
APP_ENV = os.environ.get('APP_ENV', 'DEV').upper()
os.environ['APP_ENV'] = APP_ENV

for k, v in os.environ.items():
    if APP_ENV in k:
        k = k.replace(f"{APP_ENV}_", "")
        os.environ[k] = v

import settings
_current = getattr(sys.modules['settings'], '{0}'.format(APP_ENV))()
# copy attributes to the module for convenience
for atr in [f for f in dir(_current) if not '__' in f]:
    # environment can override anything
    val = os.environ.get(atr, getattr(_current, atr))
    setattr(sys.modules[__name__], atr, val)

def _env(name, default):
    """ Get configuration from environment in priorities:
      1. the env var with prefix of $APP_ENV
      2. the env var with the same name (in upper case)
      3. the default value
    :param str name: configuration name
    :param default: default value
    """

    def _bool(val):
        if not val:
            return False
        return val not in ('0', 'false', 'no')

    # make sure configuration name is upper case
    name = name.upper()

    # try to get value from env vars
    val = default
    for env_var in ('%s_%s' % (APP_ENV, name), name):
        try:
            val = os.environ[env_var]
            break
        except KeyError:
            pass
    else:
        env_var = None

    # convert to the right types
    if isinstance(default, bool):
        val = _bool(val)
    return env_var, val


_IGNORED_CONFIG = (
    'ROOT_DIR',
    'STATIC_DIR',
    'APP_ENV',
)

# rewrite all configuration with environment variables
_vars = list(locals().keys())
for name in _vars:
    if name in _IGNORED_CONFIG:
        continue
    if not name.startswith('_') and name.isupper():
        env_var, val = _env(name, locals()[name])
        locals()[name] = val