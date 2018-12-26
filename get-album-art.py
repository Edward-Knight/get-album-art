#!/usr/bin/env python3
import spotipy
import spotipy.util
import requests
import shutil
import os

INVALID_CHARS = ["<", ">", ":", '"', "/", "\\", "|", "?", "*"]


def main():
    scope = "user-library-read"
    username = ""
    client_id = ""
    client_secret = ""
    redirect_uri = "http://localhost:8080/callback"

    token = spotipy.util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

    sp = spotipy.Spotify(auth=token)
    album_art = {}
    limit = 50
    offset = 0
    while True:
        results = sp.current_user_saved_tracks(limit=limit, offset=offset)
        if len(results["items"]) == 0:
            break
        for item in results["items"]:
            album = item["track"]["album"]
            title = album["name"]
            images = album["images"]
            if len(images) == 0:
                image_url = "http://via.placeholder.com/150/jpg"
            else:
                images.sort(key=lambda image: image["height"])
                image_url = images[-1]["url"]
            album_art[title] = image_url
        offset += limit

    total = len(album_art)
    errors = 0
    skipped = 0
    successes = 0
    print("Found", total, "albums, now downloading...")
    for title, url in album_art.items():
        path = title
        for c in INVALID_CHARS:
            path = path.replace(c, "_")
        path += ".jpg"
        if os.path.exists(path):
            print("File already exists, skipping", path)
            skipped += 1
            continue
        else:
            print("Downloading", title)
        try:
            request = requests.get(url, stream=True)
        except Exception as e:
            print("Error:", e)
            errors += 1
            continue
        if request.status_code != 200:
            print("Error:", request.status_code, title, url)
            errors += 1
            continue
        request.raw.decode_content = True
        with open(path, "wb") as f:
            shutil.copyfileobj(request.raw, f)
        successes += 1

    print("Successes:\t", successes)
    print("Skipped:\t", skipped)
    print("Errors:\t", errors)
    print("Total:\t", total)


if __name__ == "__main__":
    main()
