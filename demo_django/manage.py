#!/usr/bin/env python
"""django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('django_settings_module', 'demo_django.settings')
    try:
        from django.core.management import execute_from_command_line
    except importerror as exc:
        raise importerror(
            "couldn't import django. are you sure it's installed and "
            "available on your pythonpath environment variable? did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
