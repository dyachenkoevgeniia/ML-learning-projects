import pandas as pd
import spotipy

def fetch_playlist_tracks(playlist_id, access_token):
    sp = spotipy.Spotify(auth=access_token)

    playlist_tracks = sp.playlist_tracks(
        playlist_id,
        fields='items(track(id, name, artists, album(id, name), popularity, explicit, external_urls))'
    )

    music_data = []

    for item in playlist_tracks['items']:
        track = item['track']

        track_name = track['name']
        artists = ', '.join(artist['name'] for artist in track['artists'])
        album_name = track['album']['name']
        track_id = track['id']

        track_data = {
            'track_name': track_name,
            'artists': artists,
            'album_name': album_name,
            'track_id': track_id,
            'popularity': track.get('popularity'),
            'explicit': track.get('explicit'),
            'spotify_url': track.get('external_urls', {}).get('spotify')
        }

        music_data.append(track_data)

    return pd.DataFrame(music_data)