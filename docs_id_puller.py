import os
import re

matchlist = []
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        try:
            with open(os.path.join(root, name), encoding='utf-8') as f:
                # print(f.read())
                filetext = (f.read())
                matchtext = (re.findall('(?:docs.google.com/spreadsheets/d/)(.{0,44})(?:/htmlembed")', filetext))
                if len(matchtext) > 0:
                    # print(matchtext)
                    matchlist.append(matchtext)
                # print("Success" + os.path.join(root, name))
        except: 
            print("Failed" + os.path.join(root, name))
            
    #for name in dirs:
    #    print(os.path.join(root, name))
    
# print(matchlist)
with open("matches.txt", "w") as output:
    for item in matchlist:
        print(len(item))
        for each in item: 
            output.write( "%s\n" %each )