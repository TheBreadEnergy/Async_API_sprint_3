from datetime import datetime

from pydantic import BaseModel
from src.schemas.base import IdentifiableMixin


class FileBaseDto(IdentifiableMixin):
    filename: str
    short_name: str
    file_type: str | None


class FileResponseDto(FileBaseDto):
    size: int
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
