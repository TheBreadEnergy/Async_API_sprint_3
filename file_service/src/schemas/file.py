from datetime import datetime

from pydantic import BaseModel
from src.schemas.base import IdentifiableMixin


class FileResponseDto(IdentifiableMixin):
    filename: str
    url: str
    size: int
    file_type: str | None
    created: datetime


class FileCreateDto(BaseModel):
    short_name: str
    filename: str
    size: int
    url: str
    file_type: str | None


class FileUploadDto(BaseModel):
    url: str
    bucket_name: str
    object_name: str
    version: str
