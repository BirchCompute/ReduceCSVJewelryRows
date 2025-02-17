import csv
import re
from tkinter import filedialog

def JeweleryCSVFixer(filepath):

    #Sets delimiter for the "Image Src" section
    delimiter = ","

    #Open and parse the CSV into variable named "CSV_data"
    with open(filepath, newline='') as CSV_file:
        CSV_data = list(csv.reader(CSV_file))
        #print("File found and opened")

        #Set up array for the new data
        new_data_rows = []

        #Get the header row ready by popping it into the result as-is
        last_good_row = CSV_data.pop(0)

        #counter = 0  #Counter for stopping the program after a number of rows (Commented out with # so it doesn't happen)

        for row in CSV_data:
            #This removes duplicate header rows
            if(row[0] == "Header"):
                continue

            #Check the sample counter and stop the program (Commented out with # so it doesn't happen)
            #counter += 1    
            #if(counter > 150):
                #break

            # If the new row is a subrow that should be added to the last_good_row...
            if(row[0].strip().lower() == last_good_row[0].strip().lower()):
                #Then add the subrow's Imace Src to the last_good_row's Image Src column (stored at column index [9] in the csv)
                last_good_row[9] += delimiter + row[9]

            #If the new row is instead part of a new grouping...
            else:
                #Save the last good row into the result file
                new_data_rows.append(last_good_row)
                #Prep the new last_good_row
                last_good_row = row


    ###################################
    #This part searches the Body section (stored at [2]) with regex and searches for a keyword that tells us its Type (stored at [4])
                #Some confusing regex
                Jewelery_type_string = re.findall(r"Sold as(.*?)<", last_good_row[2].replace("\n", " "))

                #If we found something, make it lowercase
                if(Jewelery_type_string):
                    Jewelery_type_string = Jewelery_type_string[0].lower()

                #If we found nothing, it's likely a Set
                if(not Jewelery_type_string):
                    last_good_row[4] = "Sets"

                #Determine what is a Set
                elif("includes" in Jewelery_type_string):
                    last_good_row[4] = "Sets"
                elif("set" in Jewelery_type_string):
                    last_good_row[4] = "Sets"
                #Determine all the other stuff
                elif("bobby" in Jewelery_type_string):
                    last_good_row[4] = "Pins"
                elif("earring" in Jewelery_type_string):
                    last_good_row[4] = "Earrings"
                elif("ring" in Jewelery_type_string):
                    last_good_row[4] = "Rings"
                elif("necklace" in Jewelery_type_string):
                    last_good_row[4] = "Necklaces"
                elif("bracelet" in Jewelery_type_string):
                    last_good_row[4] = "Bracelets"
                elif("anklet" in Jewelery_type_string):
                    last_good_row[4] = "Anklets"
                elif("hair clip" in Jewelery_type_string):
                    last_good_row[4] = "Hair clips"

                #If it didn't fit any of these keywords, leave Type as "Jewelry" and print it to tell us what wasn't caught by the search
                else:
                    print("Couldn't match this row: ", row, filepath)
    #########################################

    #Make a new file name
    output_file_path = filepath[:-4] + "_fixed" + filepath[-4:]

    #Last chance to stop it from making a file
    #print("Algorithm done, press ENTER to confirm that you want to change the file " + output_file_path)
    #input()
    #CSV_file.close()

    #If user hits 'Enter' then finish up by writing the file
    #print('Old file closed, writing to new file')
    with open(output_file_path, 'w', newline='') as CSV_file:
        finisher = csv.writer(CSV_file, dialect = "excel", delimiter=',')
        for i in new_data_rows:
            finisher.writerow(i)
    print("Done, new file is located at " + output_file_path)

if __name__== "__main__":
    file_path = filedialog.askopenfilenames()
    for f in file_path:
        JeweleryCSVFixer(f)