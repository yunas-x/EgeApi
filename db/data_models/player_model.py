from datetime import datetime
from typing import List
from pydantic import BaseModel

from db.data_models.score_model import score_game_entry

class player_model(BaseModel):
    name: str
    email: str

    
class player_create(player_model):
    registeredOn: datetime
    hashedPassword: str
    pass

class player_game_entry(player_model):
    isActive: bool
    id: int
    games: List[score_game_entry]
    
    class Config:
        orm_mode = True
    
