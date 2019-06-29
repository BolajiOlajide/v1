import os

if os.getenv('PROD'):
    from blog.settings.production import *
else:
    from blog.settings.development import *
