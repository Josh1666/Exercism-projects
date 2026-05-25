import requests
import os
import subprocess

API_TOKEN = "71791e87-d803-4dd2-8622-90f5e29353b3"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

url = "https://api.exercism.org/v2/solutions"

data = requests.get(url, headers=headers).json()

print(data) 

for sol in data["results"]:
    track = sol["track"]["slug"]
    exercise = sol["exercise"]["slug"]

    print(f"Downloading {track} - {exercise}")
    subprocess.run([
        "exercism",
        "download",
        f"--track={track}",
        f"--exercise={exercise}"
    ])