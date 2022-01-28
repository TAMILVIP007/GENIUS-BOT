import os

if ENV := bool(os.environ.get("ENV", False)):
    from heroku_config import Var as Config
else:
    from local_config import Development as Config


Var = Config
