# get-album-art

Download the album art from your Spotify library


## Spotify API credentials

You need to set your Spotify API credentials.
Get your credentials from [Spotify's website](https://developer.spotify.com/my-applications).
Read more about authentication in the [Spotipy documentation](https://spotipy.readthedocs.io/en/latest/#authorization-code-flow).

You can do this by setting environment variables like so:


### In Bash:

```bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```


### In PowerShell:

```powershell
$env:SPOTIPY_CLIENT_ID='your-spotify-client-id'
$env:SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
$env:SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```
