import requests
from django.core.files.storage import Storage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.deconstruct import deconstructible

from config.settings import FILE_SERVICE_URL


@deconstructible
class CustomStorage(Storage):
    def _save(self, name, content: InMemoryUploadedFile):
        r = requests.post(FILE_SERVICE_URL, files={'file': (content.name, content, content.content_type)})
        return r.json().get('short_name')

    def url(self, name):
        return f"{FILE_SERVICE_URL}/download-stream/{name}"

    def exists(self, name):
        return False
