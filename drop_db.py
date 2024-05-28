from models import storage
from models.base_model import Base

# Drop all tables
#storage._DBStorage__engine.execute("DROP DATABASE IF EXISTS edukid_dev_db")
#storage._DBStorage__engine.execute("CREATE DATABASE edukid_dev_db")

# Recreate tables
#storage.reload()

# Alternatively, you can use Base.metadata.drop_all and create_all
Base.metadata.drop_all(storage._DBStorage__engine)
Base.metadata.create_all(storage._DBStorage__engine)
