import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.data_context import Base

class score_entity(Base):
    __tablename__ = "ScoreEntity"
    
    id = Column(Integer, primary_key=True, index=True)
    totalAnswered = Column(Integer, unique=False, index=False) #
    correctAnswered = Column(Integer, unique=False, index=False) #
    playedOn = Column(DateTime, unique=False, index=False, default=datetime.datetime.now()) #
    playerId = Column(Integer, ForeignKey("PlayerEntity.id"))
    
    player = relationship("player_entity", back_populates="games")
    
    