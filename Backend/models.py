from database import Base
from sqlalchemy import Column,Integer,String
from pydantic import BaseModel

class Logs(Base):
    __tablename__='user_logs'
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    query=Column(String)
    response=Column(String)


    
class ChatRequest(BaseModel):
    query: str
    