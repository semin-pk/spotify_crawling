from spotify_user import *
from spotify_api import *
from lyrics_crawler import *
from predict_emotion import *
from CRUD.spotify import get_spotifyinfo, get_recommend_vodlist
from CRUD.movie import get_overview, insert_movie_emotion
from datetime import datetime
'''spotify_lists = get_spotifyinfo()
for spotify_list in spotify_lists:
    timestamp_datetime = datetime.fromtimestamp(spotify_list['EXPIRE_DATE'])
    if datetime.now().timestamp() > timestamp_datetime.timestamp():
        use_info = refresh_access_token(spotify_list)
        audio_names = get_playlist(use_info['ACCESS_TOKEN'])
        lyrics_list = crawling_lyrics(audio_names)
        emotion = predict_emotion(lyrics_list)
        vod_list = get_recommend_vodlist(emotion)
        update_recommend_vodlist(use_info['USER_ID'], vod_list)'''
overview_lists = get_overview()
for overview_list in overview_lists:
    emotion = predict_emotion(overview_list['MOVIE_OVERVIEW'])
    print(overview_list['MOVIE_ID'], emotion)
    insert_movie_emotion(overview_list['MOVIE_ID'], emotion)




