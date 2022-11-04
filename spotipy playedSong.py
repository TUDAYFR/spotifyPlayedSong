import spotipy
import spotipy.util as util

CLIENT_ID = '****'
CLIENT_SECRET = '****'
username = "myUsername"
scope = "user-read-currently-playing,user-read-private,user-read-playback-state"
redirect_uri = "http://localhost:8888/callback/"

token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_uri)
sp = spotipy.Spotify(auth=token)

def Get_Data_CurentSong():
    #Get permision
    token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_uri)
    sp = spotipy.Spotify(auth=token)
    
    #Get Data Of The Curently Playing Song
    currentsong_data = sp.currently_playing()
    
    #Get Info From The Current Data
    song_name = currentsong_data['item']['name']
    song_artist = currentsong_data['item']['artists'][0]['name']
    progres_ms = currentsong_data['progress_ms']
    duration_ms = currentsong_data['item']['duration_ms']
    
    #Nom, Artiste, Progres, Duration
    return str(song_name) + ">" + str(song_artist) + ">" + str(progres_ms) + ">" + str(duration_ms) 

def Get_Data_Device():
    #Get permision
    token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_uri)
    sp = spotipy.Spotify(auth=token)
    
    #Get Data Of The Devices
    Data_Devices  = sp.devices()
    
    #Get Active user 
    for i in range(len(Data_Devices['devices'])):
        if Data_Devices['devices'][i]['is_active'] == True :
            I_Active_Device = i
            
    #Get Info From The User
    user_name = Data_Devices['devices'][i]['name']
    user_volume = Data_Devices['devices'][i]['volume_percent']
    #nom, volume
    return str(user_name) + ">" + str(user_volume)
    
    
print(Get_Data_CurentSong())
print(Get_Data_Device())