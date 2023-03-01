from pydantic import BaseModel

class spelling_model(BaseModel):
    word: str
    correctAnswer: str
    wrongAnswer: str
    
class spelling_create(spelling_model):
    pass

class spelling_game_entry(spelling_model):
    id: int
    
    class Config:
        orm_mode = True