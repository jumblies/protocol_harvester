import requests

with open("matches.txt", "r") as myfile:
    for line in (myfile.readlines()):
        print(line.rstrip())
        # this gets to a line by line readout of each of the IDs in the docs.
        
        