from .base import *

env_name = os.getenv('ENV_NAME', 'production')

if env_name == 'development':
    from .development import *

else:
    from .production import *
