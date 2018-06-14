#!/usr/bin/python3
"""
Init Module
"""


from models.engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
