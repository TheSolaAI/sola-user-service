import psycopg
from django.core.management.base import BaseCommand
from django.db import connections


class Command(BaseCommand):
    help = "Forcefully closes database connections and resets the database"

    def handle(self, *args, **options):
        self.close_connections()
        self.call_reset_db()

    def close_connections(self):
        db_config = connections["default"].settings_dict.copy()
        database_name = db_config.pop("NAME")
        user = db_config.pop("USER")
        password = db_config.pop("PASSWORD")
        host = db_config.pop("HOST")
        port = db_config.pop("PORT")

        with psycopg.connect(
            dbname=database_name, user=user, password=password, host=host, port=port
        ) as conn:
            conn.autocommit = True
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = %s AND pid <> pg_backend_pid()",
                    (database_name,),
                )

    def call_reset_db(self):
        from django.core.management import call_command

        call_command("reset_db", "--noinput")
