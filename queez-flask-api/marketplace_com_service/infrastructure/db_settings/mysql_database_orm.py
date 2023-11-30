from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql://root:Ahsan.1998@localhost/abc"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
db_context_orm = Session()


