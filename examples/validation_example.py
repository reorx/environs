import os

from envargs import Env, EnvError
from marshmallow.validate import OneOf, Email, Length


os.environ['TTL'] = '-2'
os.environ['NODE_ENV'] = 'invalid'
os.environ['EMAIL'] = '^_^'


env = Env()

# simple validator
try:
    env.int('TTL', validate=lambda n: n > 0)  # => 'sloria'
except EnvError as err:
    print(err)

# marshmallow validator
try:
    env.str('NODE_ENV',
            validate=OneOf(['production', 'development'],
                           error='NODE_ENV must be one of: {choices}'))
except EnvError as err:
    print(err)


# multiple validators
try:
    env.str('EMAIL',
            validate=[Length(min=4), Email()])
except EnvError as err:
    print(err)
