from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:Ahsan.1998@localhost/queez"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
db_context_orm = Session()




