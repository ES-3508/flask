from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql://root:Ahsan.1998@localhost/abcc"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
db_context_orm = Session()


# from sqlalchemy import create_engine

# DATABASE_URL = "mysql://root:Ahsan.1998@localhost/queez"

# # Add 'pool_pre_ping=True' to check for server disconnection on every checkout
# # Add 'pool_recycle=3600' to set a timeout for the database connection
# engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True, pool_recycle=3600, connect_args={"check_same_thread": False}, isolation_level="AUTOCOMMIT")
