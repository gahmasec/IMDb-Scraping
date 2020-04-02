import subprocess
with open("output.txt", "w+") as output:
    subprocess.call(["python", "./imdb-list.py"], stdout=output);
