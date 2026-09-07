from app.core.config import settings as env
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# pattern for clear URL: "postgresql://<username>:<password>@<ip-address>/<database-name>"
SQLALCHMY_DATABASE_URL = f"postgresql://{env.DB_USERNAME}:{env.DB_PASSWORD}@{env.DB_HOSTNAME}:{env.DB_PORT}/{env.DB_NAME}"

#* create `sqlalchemy` engine
engine = create_engine(SQLALCHMY_DATABASE_URL)

#* create `sqlalchemy` session
SessionLocal = sessionmaker(bind=engine, autoflush=False)

#* define `Base` for Models
Base = declarative_base()