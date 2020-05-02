import requests
import time
with open("matches.txt", "r") as myfile:
    for line in (myfile.readlines()):
        # print(line.rstrip())
        filekey = line.rstrip()
        url = (f'https://docs.google.com/feeds/download/spreadsheets/Export?key={filekey}&exportFormat=csv')
        print(url)
        r = requests.get(url)
        filename = f'{filekey}.csv'
        with open(filename, "wb") as f:
            f.write(r.content)
        time.sleep(1)    
        # this gets to a line by line readout of each of the IDs in the docs.
        
# r = requests.get('https://docs.google.com/feeds/download/spreadsheets/Export?key=1HbPPMVDNd6XuxWoVWDcJS5VxKTflLeXTZXOOYMAFYQU&exportFormat=pdf')

# with open("response.pdf", "wb") as f:
    # f.write(r.content)