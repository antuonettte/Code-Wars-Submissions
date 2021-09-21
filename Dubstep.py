import re


def song_decoder(song):
    return " ".join(re.sub("WUB", " ", song).split())

print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
