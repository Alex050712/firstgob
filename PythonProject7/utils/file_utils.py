
from pathlib import Path

from multipart import file_path
import uuid

ALLOW_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif"]
MAX_FILE_SIZE = 5*1024*1024
def is_allowed_file(filename):
    """Проверяем, есть ли расширение в списке разрешённых."""
    ext = filename.suffix.lower()
    print(ext)
    return ext in ALLOW_EXTENSIONS
def get_unique_name(filename: Path):
    ext = file_path.suffix.lower()
    unique_name = f"{uuid.uuid4().hex}{ext}"
    print(f"{unique_name=}")
    return unique_name