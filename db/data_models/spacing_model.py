from pydantic import BaseModel

class spacing_model(BaseModel):
    word: str
    correctAnswer: int
    
class spacing_create(spacing_model):
    pass

class spacing_game_entry(spacing_model):
    id: int
    
    class Config:
        orm_mode = True