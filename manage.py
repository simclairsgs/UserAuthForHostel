#!/usr/bin/env python
'''
Copyright (C) 2021 , George Simclair Sam 

This file is part of the UserAuthForHostel project.

This file can not be copied and/or distributed without the express
permission of George Simclair Sam, simclair.sgs@gmail.com .
'''
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_Mp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
