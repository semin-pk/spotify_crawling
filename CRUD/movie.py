from DB.database import engineconn
from DB.models import SPOTIFY, USERS, MOVIES
from sqlalchemy import *
import json
from DB.database import MongoDB


mongodb = MongoDB()
db = mongodb.get_database('hellody')

engine = engineconn()
session_maker = engine.sessionmaker()



def get_spotifyinfo() -> list:
    collection = db['SPOTIFY']
    user_list = list(collection.find({}, {'_id': 0, 'USER_ID':1, 'ACCESS_TOKEN':1, 'REFRESH_TOKEN':1, 'EXPIRE_DATE':1, 'EMOTION':1}))
    return user_list

def get_recommend_vodlist(emotion) -> list:
    collection = db['MOVIES']
    vod_list = list(collection.find({'EMOTION':emotion}, {'_id':0, 'MOVIE_ID':1, 'TITLE':1, 'POSTER':1}))
    return vod_list


def update_recommend_vodlist(user_id, vod_list):
    collection = db['recommend_list']
    collection.update_one(
        {'user_id':user_id},
        {
            '$set':
            {
            'spotify':vod_list
            }
        }
    )


def update_refreshtoken(user_id, access_token, expires_at):
    session_maker.execute(
        update(SPOTIFY)
        .where(SPOTIFY.USER_ID == user_id)
        .values(
            {
                SPOTIFY.ACCESS_TOKEN : access_token,
                SPOTIFY.EXPIRE_DATE : expires_at
            }
        )
    )
    session_maker.commit()

def update_emotion(user_id, emotion):
    session_maker.execute(
        update(SPOTIFY)
        .where(SPOTIFY.USER_ID == user_id)
        .values(
            {
                SPOTIFY.EMOTION : emotion
            }
        )
    )
    session_maker.commit()


#영화 감정 분석
'''def get_overview():
    collection = db['MOVIES']
    vod_views = list(collection.find({},{'_id': 0, 'MOVIE_ID':1, 'MOVIE_OVERVIEW':1}))
    return vod_views

def insert_movie_emotion(MOVIE_ID, emotion):
    collection = db['MOVIES']
    session_maker.execute(
        update(MOVIES)
        .where(MOVIES.MOVIE_ID == MOVIE_ID)
        .values(
            {
                MOVIES.EMOTION : emotion
            }
        )
    )
    session_maker.commit()
    collection.update_one(
        {'MOVIE_ID':MOVIE_ID},
        {
            '$set':
            {
            'EMOTION':emotion
            }
        }
    )
'''