from datetime import datetime
import hashlib
from typing import List
from fastapi import Body, Depends, FastAPI, Request, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from db.data_context import SessionLocal, Engine

from fastapi.responses import FileResponse

import db.data_models.accent_model as accent_model
from db.data_models.player_model import player_create
from db.data_models.score_model import score_create
import db.data_models.spacing_model as spacing_model
import db.data_models.spelling_model as spelling_model
import db.data_models.spacing_model as spacing_model
import db.data_models.spelling_model as spelling_model

import db.crud as crud
from db.entities.player_entity import hash_pass

from try_create_tables import try_create_datatables

try_create_datatables()

app = FastAPI()

def get_db(request: Request):
    return request.state.db

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.get("/")
def mainpage():
    return FileResponse("index.html")


@app.get("/accents/{limit}", response_model=List[accent_model.accent_game_entry])
def get_accent_game_entries(limit: int, db: Session = Depends(get_db)):
    
    return crud.get_accent_entities(db=db, limit=limit)

@app.get("/spacing/{limit}", response_model=List[spacing_model.spacing_game_entry])
def get_spacing_game_entries(limit: int, db: Session = Depends(get_db)):
    
    return crud.get_spacing_entities(db=db, limit=limit)

@app.get("/spelling/{limit}", response_model=List[spelling_model.spelling_game_entry])
def get_spelling_accent_game_entries(limit: int, db: Session = Depends(get_db)):
    
    return crud.get_spelling_entities(db=db, limit=limit)


@app.get("/users/delete/id={id}")
def delete_user_by_id(id: int, db: Session = Depends(get_db)):
    response = "OK"
    try:
        crud.delete_user_by_id(db=db, id=id)
    except:
        response = "Invalid"
        
    return response
    
@app.get("/users/delete/name={name}")
def delete_user_by_name(name: str, db: Session = Depends(get_db)):
    response = "OK"
    try:
        crud.delete_user_by_name(db=db, name=name)
    except:
        response = "Invalid"
        
    return response

@app.get("/users/recover/id={id}")
def delete_user_by_id(id: int, db: Session = Depends(get_db)):
    response = "OK"
    try:
        crud.delete_user_by_id(db=db, id=id)
    except:
        response = "Invalid"
    return response
    
@app.get("/users/recover/name={name}")
def delete_user_by_name(name: str, db: Session = Depends(get_db)):
    response = "OK"
    try:
        crud.recover_user_by_name(db=db, name=name)
    except:
        response = "Invalid"
    return response

@app.get("/users/stats/id={id}")
def delete_stats_by_id(id: int, db: Session = Depends(get_db)):
    return crud.get_stats_by_id(db=db, id=id)
    
@app.get("/users/stats/name={name}")
def delete_stats_by_name(name: str, db: Session = Depends(get_db)):
    return crud.get_stats_by_name(db=db, name=name)

@app.get("/users/winrate/id={id}")
def get_winrate_by_id(id: int, db: Session = Depends(get_db)):
    return crud.get_winrate_by_id(db=db, id=id)

@app.post("/postscore/{id}")
def create_score_entry(data=Body(), db: Session = Depends(get_db), id=id):
    item = score_create(totalAnswered=data["totalAnswered"], 
                 correctAnswered=data["correctAnswered"], 
                 playedOn=datetime.now())
    return crud.create_score_entry(db=db, item=item, playerId=id)

@app.post("/postplayer")
def create_user(data=Body(), db: Session = Depends(get_db)):
    item = player_create(name=data["name"], 
                  email=data["email"], 
                  registeredOn=datetime.now(), 
                  hashedPassword=data["password"])
    
    if crud.check_player_name(db=db, name=item.name) != 0:
        return {"id": -3}
    if crud.check_player_email(db=db, email=item.email) != 0:
        return {"id": -4}
    
    user = crud.create_user(db=db, item=item)
    
    return {"name": user.name, "id": user.id, "registeredOn": user.registeredOn}


    
@app.post("/validateplayer")
def create_player(data=Body(), db: Session = Depends(get_db)):
    if crud.check_player_name(db=db, name=data["name"]) == 0:
        return {"name": "No one", "id": -1}
    else:
        user = crud.get_user_by_name(db=db, name=data["name"])
        if user.hashedPassword != hash_pass(data["password"]):
            return {"name": "Wrong pass", "id": -2}
        else: 
            return {"name": user.name, "id": user.id, "registeredOn": user.registeredOn}
