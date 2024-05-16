#BASIC BRANCHING (if statements, booleans)
# Lab 4 - A Music Playlist
# This program gets two inputs from the user.  Using those inputs, it
# outputs a music playlist.
# Data was pulled from top 5 artists on Billboard 100 on Fri, Aug. 18
# https://www.billboard.com/charts/hot-100/

# TODO: Add your name and the names of your team members

morgan_wallen_songs = ["Last Night"]
luke_combs_songs = ["Fast Car", "Love You Anyway"]
olivia_rodrigo_songs = ["Vampire"]
rema_songs = ["Calm Down"]
taylor_swift_songs = ["I Can See You", "Cruel Summer", "Karma"]

# TODO: Write your code here
artist = input("Enter Artist: ")

if(artist == "Morgan Wallen"):
    print("My playlist:\n"
    + morgan_wallen_songs[0])

if(artist == "Luke Combs"):
    print("My playlist:\n"
    + luke_combs_songs[0])

if(artist == "Olivia Rodrigo"):
    print("My playlist:\n"
    + olivia_rodrigo_songs[0])

if(artist == "Rema"):
    print("My playlist:\n"
    + rema_songs[0])

if(artist == "Taylor Swift"):
    print("My playlist:\n"
    + taylor_swift_songs[0])
