
from datetime import datetime
from spotify_api import use_refresh_token
import json
from DB.models import SPOTIFY
from CRUD.spotify import *


def refresh_access_token(user_info:dict):
    try:
        print(user_info['REFRESH_TOKEN'])
        new_token_info = use_refresh_token(user_info['REFRESH_TOKEN'])
        print(new_token_info)
        user_info['ACCESS_TOKEN'] = new_token_info['access_token']
        user_info['EXPIRE_DATE']= datetime.now().timestamp() + new_token_info['expires_in']
        user_id = user_info['USER_ID']
        update_refreshtoken(user_id, user_info['ACCESS_TOKEN'], user_info['EXPIRE_DATE'])
        return user_info
    except:
        return False