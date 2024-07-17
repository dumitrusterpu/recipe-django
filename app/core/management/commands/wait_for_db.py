"""
wait for db to be available
"""
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django comman to wait for database """

    def handle(self, *args, **options):
        """ entrypoint for command"""
        self.stdout.write('waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('database unavailable')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('database available'))
