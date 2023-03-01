from datetime import datetime
from pprint import pprint
from db.data_context import SessionLocal, Engine

import db.data_models.accent_model as accent_model
import db.data_models.player_model as player_model
import db.data_models.score_model as score_model

import db.entities.accent_entity as accent_entity
import db.entities.player_entity as player_entity
import db.entities.score_entity as score_entity
import db.entities.spelling_entity as spelling_entity
import db.entities.spacing_entity as spacing_entity

import db.crud as crud


def try_create_datatables():
    try:
        accent_entity.Base.metadata.create_all(bind=Engine)
    finally:
        pass

    try:
        spelling_entity.Base.metadata.create_all(bind=Engine)
    finally:
        pass

    try:
        spacing_entity.Base.metadata.create_all(bind=Engine)
    finally:
        pass
    
    try:
        player_entity.Base.metadata.create_all(bind=Engine)
    finally:
        pass
    
    try:
        score_entity.Base.metadata.create_all(bind=Engine)
    finally:
        pass

if __name__ == "__main__":
    try_create_datatables()
    db = SessionLocal()
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        crud.create_accent_entity(db=db, item=accent_model.accent_create(word=i, correctAnswer=1))
        

    crud.create_user(db=db, item=player_model.player_create(name="Ivan1", email="Ivan", hashedPassword="Ivan", registeredOn=datetime.now()))
    a = crud.get_user_by_id(db=db, id=1)
    pprint(a)
    crud.create_score_entry(db=db, 
                            item=score_model.score_create(totalAnswered=10, 
                                                            correctAnswered=2, 
                                                            playedOn=datetime.utcnow()), 
                            playerId=1)
    
    c = crud.get_stats_by_id(db=db, id=1)
    
    pprint(c)