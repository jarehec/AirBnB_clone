#!/usr/bin/python3
'__init__.py for models package'

from models.engine.file_storage import FileStorage

print("++models/__init__++")
storage = FileStorage()
storage.reload()
