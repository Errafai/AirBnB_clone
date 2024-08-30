"""in this module we will create the variable storage
that is an instance of the file_storage classe"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
