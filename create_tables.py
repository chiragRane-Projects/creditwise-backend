from app.core.database import engine, Base
from app.models import user

print("Creating tables....")
Base.metadata.create_all(bind=engine)
print("Done")