"""
ASGI config for backend_Mp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

'''
Copyright (C) 2021 , George Simclair Sam 

This file is part of the UserAuthForHostel project.

This file can not be copied and/or distributed without the express
permission of George Simclair Sam, simclair.sgs@gmail.com .
'''

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_Mp.settings')

application = get_asgi_application()
