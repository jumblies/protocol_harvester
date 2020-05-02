import csv
import shutil
import os

myfile = "1_67BWrWdB8fK-3hRMWlelJlpu7WXWwSTkatH4CPViDg.csv"

def csv_renamer(filename):
    with open(filename, "r", newline='') as csvFile:
        new_file_name = ''
        reader = csv.reader(csvFile)
        field_names_list = reader.__next__()
        new_file_name = '_'.join(field_names_list[1:2])
        
        print(new_file_name)

        sanitized_new_file_name = "".join(x for x in new_file_name if x.isalnum())
        
        # print(sanitized_new_file_name)
        #copy csv to new filename
        
        shutil.copy(filename, (sanitized_new_file_name + ".csv"))


        shutil.copy(filename[0:-4]+".pdf", (sanitized_new_file_name + ".pdf"))


# csv_renamer(myfile)

for file in os.listdir():
    if file.endswith(".csv"):
        csv_renamer(file)