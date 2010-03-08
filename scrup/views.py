import datetime

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse, HttpResponseBadRequest
from boto.s3.connection import S3Connection
from boto.s3.key import Key

from scrup.models import *
from scrup.utils import BaseConverter

key = getattr(settings, 'SCRUP_AWS_ACCESS_KEY', None)
secret = getattr(settings, 'SCRUP_AWS_SECRET_KEY', None)
bucket = getattr(settings, 'SCRUP_AWS_BUCKET', None)
prefix = getattr(settings, 'SCRUP_AWS_PREFIX', '')
cname = getattr(settings, 'SCRUP_AWS_CNAME', False)

url_template = 'http://%s/%s' % (
    bucket if cname else bucket + ".s3.amazonaws.com",
    prefix + '/' if prefix else '')

if key and secret and bucket:
    # TODO: exception handling
    conn = S3Connection(key, secret)
else:
    raise ImproperlyConfigured('django-scrup AWS config requires key, secret, and bucket.')

base62_converter = BaseConverter()


def upload(request, filename=None):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    now = datetime.datetime.now()
    today = now.date()
    d, created = Date.objects.get_or_create(date=today)
    
    s = Screenshot.objects.create(date=d, name=filename, timestamp=now)
    print s.id
    converted = base62_converter.from_decimal(s.id)
    url = url_template + converted
    print url
    
    # TODO: exception handling
    headers = {
        'Content-Type': 'image/png',
    }
    b = conn.create_bucket(bucket)
    k = Key(b)
    k.key = converted
    # Hacky? Can't think of a better way to do this.
    k.set_contents_from_string(request.raw_post_data, headers=headers, policy='public-read')
    
    response = HttpResponse()
    response.status_code = 201
    response.content = url
    return response