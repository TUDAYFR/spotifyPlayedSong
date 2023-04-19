# spotify Played Song

## README for Get Data from Spotify Script
This script allows you to access data from your Spotify account using the Spotipy library. Specifically, the script provides two functions:

- Get_Data_CurentSong(): This function returns information about the currently playing song, including the song name, artist, progress in milliseconds, and duration in milliseconds.

- Get_Data_Device(): This function returns information about the active device associated with your Spotify account, including the device name and volume level.

## Setup
Before using this script, you need to obtain a Spotify client ID and client secret by following these steps:

- Go to the Spotify Developer Dashboard.
- Log in to your Spotify account, or create a new account if you don't have one.
- Create a new app by clicking the "Create a Client ID" button.
- Follow the prompts to provide information about your app, including a name and description.
Once your app is created, you will be redirected to the app's dashboard. Here, you can find your client ID and client secret.
- Make sure to replace the CLIENT_ID and CLIENT_SECRET variables in the script with your own client ID and client secret.

You will also need to provide your Spotify username, redirect URI, and the desired scope of permissions. Replace the username, redirect_uri, and scope variables in the script with your own information.

## Usage
To use the script, simply run it in your preferred Python environment. The Get_Data_CurentSong() and Get_Data_Device() functions will return the desired information as a formatted string. You can customize the formatting of the output as needed.

Note that you may be prompted to log in to your Spotify account when running the script. Follow the prompts in your terminal to provide authorization.

## Dependencies
This script relies on the Spotipy library, which can be installed via pip. To install Spotipy, run the following command in your terminal:


```pip install spotipy```
