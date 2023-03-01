from datetime import datetime
import datetime as dt
from pydantic import BaseModel


class score_model(BaseModel):
    totalAnswered: int
    correctAnswered: int

    
class score_create(score_model):
    playedOn: datetime
    pass

class score_game_entry(score_model):
    id: int
    playerId: int
    
    class Config:
        orm_mode = True
