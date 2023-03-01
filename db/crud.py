import hashlib
from sqlalchemy import select
from sqlalchemy.orm import Session

from sqlalchemy.sql.functions import random
import db.data_models.accent_model as accent_model
import db.data_models.spacing_model as spacing_model
import db.data_models.spelling_model as spelling_model
import db.entities.accent_entity as accent_entity
import db.entities.spelling_entity as spelling_entity
import db.entities.spacing_entity as spacing_entity

import db.data_models.player_model as player_model
import db.entities.player_entity as player_entity

import db.data_models.score_model as score_model
import db.entities.score_entity as score_entity

def get_accent_entities(db: Session, limit: int = 10):
    return db \
    .query(accent_entity.accent_entity) \
    .order_by(random()) \
    .limit(limit) \
    .all()

def get_spacing_entities(db: Session, limit: int = 10):
    return db \
    .query(spacing_entity.spacing_entity) \
    .order_by(random()) \
    .limit(limit) \
    .all()

def get_spelling_entities(db: Session, limit: int = 10):
    return db \
    .query(spelling_entity.spelling_entity) \
    .order_by(random()) \
    .limit(limit) \
    .all()
    
def create_accent_entity(db: Session, item: accent_model.accent_create):
    db_item = accent_entity.accent_entity(word=item.word, 
                                          correctAnswer=item.correctAnswer)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_spacing_entity(db: Session, item: spacing_model.spacing_create):
    db_item = spacing_entity.spacing_entity(word=item.word, 
                                            correctAnswer=item.correctAnswer)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_spelling_entity(db: Session, item: spelling_model.spelling_create):
    db_item = spelling_entity.spelling_entity(word=item.word, 
                                              correctAnswer=item.correctAnswer, 
                                              wrongAnswer=item.wrongAnswer)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_user(db: Session, item: player_model.player_create):
    db_item = player_entity.player_entity(email=item.email, 
                                          hashedPassword=player_entity.hash_pass(item.hashedPassword), 
                                          name=item.name)
    
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_user_by_id(db: Session, id: int) -> player_entity.player_entity:
    return db \
    .query(player_entity.player_entity) \
    .filter(player_entity.player_entity.id == id) \
    .first()
    
def get_user_by_name(db: Session, name: str) -> player_entity.player_entity:
    return db \
    .query(player_entity.player_entity) \
    .filter(player_entity.player_entity.name == name) \
    .first()
    
def delete_user_by_id(db: Session, id: int):
    return db \
    .query(player_entity.player_entity) \
    .filter(player_entity.player_entity.id == id) \
    .update({player_entity.player_entity.isActive: False})

def delete_user_by_name(db: Session, name: str):
    return db \
    .query(player_entity.player_entity) \
    .filter(player_entity.player_entity.name == name) \
    .update({player_entity.player_entity.isActive: False})

def recover_user_by_id(db: Session, id: int):
    return db \
    .query(player_entity.player_entity) \
    .filter(player_entity.player_entity.id == id) \
    .update({player_entity.player_entity.isActive: True})

def recover_user_by_name(db: Session, name: str):
    return db \
    .query(player_entity.player_entity) \
    .filter(player_entity.player_entity.name == name) \
    .update({player_entity.player_entity.isActive: True})
    
def create_score_entry(db: Session, item: score_model.score_create, playerId: int):
    db_item = score_entity.score_entity(correctAnswered=item.correctAnswered, 
                                        totalAnswered=item.totalAnswered,
                                        playerId=playerId,
                                        playedOn=item.playedOn)
    
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_stats_by_id(db: Session, id: int):
    return db \
    .query(score_entity.score_entity) \
    .filter(score_entity.score_entity.playerId == id) \
    .order_by(score_entity.score_entity.playedOn) \
    .all()
    
def get_stats_by_name(db: Session, name: str):
    return db \
    .query(score_entity.score_entity) \
    .filter(score_entity.score_entity.playerId == name) \
    .order_by(score_entity.score_entity.playedOn) \
    .all()

    
def get_winrate_by_id(db: Session, id: int):
    total = db.query(score_entity.score_entity.totalAnswered) \
    .filter(score_entity.score_entity.playerId == id) \
    .all()
    correct = db.query(score_entity.score_entity.correctAnswered) \
    .filter(score_entity.score_entity.playerId == id) \
    .all()
    
    tScore = 0
    cScore = 0

    for t, c in zip(total, correct):
        tScore += t[0]
        cScore += c[0]
    
    return round(cScore / tScore, 2)

def check_player_name(db: Session, name: str):
    return db \
    .query(player_entity.player_entity) \
    .filter(player_entity.player_entity.name == name) \
    .count()
    
def check_player_email(db: Session, email: str):
    return db \
    .query(player_entity.player_entity) \
    .filter(player_entity.player_entity.email == email) \
    .count()
            