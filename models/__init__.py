#!/usr/bin/python3
'__init__.py for models package'

from models.engine.file_storage import FileStorage

storage = FileStorage()
input("in init")
storage.reload()
