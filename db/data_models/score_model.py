from datetime import datetime
import datetime as dt
from typing import Union
from pydantic import BaseModel


class score_model(BaseModel):
    totalAnswered: int
    correctAnswered: int
    gameMode: Union[str, None]

    
class score_create(score_model):
    playedOn: datetime
    pass

class score_game_entry(score_model):
    id: int
    playerId: int
    
    class Config:
        orm_mode = True
