from .aws import (
    AWS_ACCESS_KEY_ID,
    AWS_REGION,
    AWS_SECRET_ACCESS_KEY,
    AWS_STORAGE_BUCKET_NAME,
    AWS_STORAGE_STATIC_BUCKET_NAME,
)

STATIC_URL = "static/"
STATIC_ROOT = "staticfiles"

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": AWS_ACCESS_KEY_ID,
            "secret_key": AWS_SECRET_ACCESS_KEY,
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "region_name": AWS_REGION,
            "file_overwrite": False,
        },
    },
    "PublicMediaStorage": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": AWS_ACCESS_KEY_ID,
            "secret_key": AWS_SECRET_ACCESS_KEY,
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "region_name": AWS_REGION,
            "default_acl": "public-read",
            "location": "media/public",
            "querystring_auth": False,
            "file_overwrite": False,
        },
    },
    "PrivateMediaStorage": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": AWS_ACCESS_KEY_ID,
            "secret_key": AWS_SECRET_ACCESS_KEY,
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "region_name": AWS_REGION,
            "location": "media/private",
            "default_acl": "private",
            "signature_version": "s3v4",
            "file_overwrite": False,
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": AWS_ACCESS_KEY_ID,
            "secret_key": AWS_SECRET_ACCESS_KEY,
            "bucket_name": AWS_STORAGE_STATIC_BUCKET_NAME,
            "region_name": AWS_REGION,
            "default_acl": "public-read",
            "location": "staticfiles",
            "querystring_auth": False,
        },
    },
}

DBBACKUP_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
DBBACKUP_STORAGE_OPTIONS = {
    "access_key": AWS_ACCESS_KEY_ID,
    "secret_key": AWS_SECRET_ACCESS_KEY,
    "bucket_name": "sola-dev-db-backup",
    "default_acl": "private",
}
