from pydantic import BaseModel

class accent_model(BaseModel):
    word: str
    correctAnswer: int
    
class accent_create(accent_model):
    pass

class accent_game_entry(accent_model):
    id: int
    
    class Config:
        orm_mode = True