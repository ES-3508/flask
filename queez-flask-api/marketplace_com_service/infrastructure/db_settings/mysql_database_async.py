from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import asyncio

# DATABASE_URL = "mysql+aiomysql://root:Ahsan.1998@localhost/queez"
# async_engine = create_engine(DATABASE_URL, echo=True)
# async_session = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)
# Session = sessionmaker(bind=async_engine)
# db_context_async = Session()
