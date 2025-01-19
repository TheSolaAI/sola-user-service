import os

import boto3
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Copy .env and .prod.env from the local folder to S3"

    def handle(self, *args, **options):
        files_to_upload = [
            {"local": ".dev.env", "s3_folder": "dev/", "rename_to": ".env"},
            {"local": ".env", "s3_folder": "local/"},
        ]

        s3_bucket_name = "tdfa-django-secrets"

        s3_client = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name="ap-south-1",
        )

        for file in files_to_upload:
            local_file_path = file["local"]
            s3_file_key = file.get("rename_to", os.path.basename(local_file_path))
            s3_file_key = os.path.join(file["s3_folder"], s3_file_key)

            if not os.path.exists(local_file_path):
                self.stdout.write(
                    self.style.ERROR(
                        f"The local file {local_file_path} does not exist."
                    )
                )
                continue

            try:
                # Upload the file to S3
                s3_client.upload_file(local_file_path, s3_bucket_name, s3_file_key)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully copied {local_file_path} to s3://{s3_bucket_name}/{s3_file_key}"  # noqa
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Error copying {local_file_path} to {s3_file_key}: {e}"
                    )
                )
