#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import time
from psycopg2 import OperationalError
from django.db import connections


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def wait_for_db():
    db_conn = None
    while not db_conn:
        try:
            db_conn = connections['default']
        except OperationalError:
            print('Aguardando o banco de dados...')
            time.sleep(1)

    print('Banco de dados pronto!')


if __name__ == '__main__':
    main()
    wait_for_db()
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)




