import csv
import re

#Get file path and filenames ready
#CHANGE THESE TO MATCH THE CSV FILE YOU ARE TRYING TO CHANGE WITH THIS PROGRAM
pathroot = "C:/Users/USER/Downloads/"    #####Replace this path with the path to your file's folder, using / instead of \, and make sure it ends with a final /
filename = "fileBeforeChanges.csv"       #####Change this to match your file's name (with file extension .csv)
outputfilename = "fileAfterChanges.csv"  #####This is what the result file will be called (with file extension .csv)

##################################
#
#       IF YOU GET THE FOLLOWING ERROR:
#
#       Traceback (most recent call last):
#        File "PATH\NAME OF PROGRAM.py", line 16, in <module>
#          with open(filepath, newline='') as csvfile:
# ---> FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/USER/Downloads/fileBeforeChanges.csv'
#
#       THEN YOU NEED TO CHANGE SOMETHING ABOUT THE CODE ABOVE THAT SETS THE PATHS AND FILE NAMES
#
##################################

filepath = pathroot + filename

#Sets delimiter for the "Image Src" section
delimiter = ","

#Open and parse the CSV into variable named "reader"
with open(filepath, newline='') as csvfile:
    reader = list(csv.reader(csvfile))
    print("File found and opened")

    #Set up array for the new data
    doneRows = []

    #Get the header row ready by popping it into the result as-is
    lastRow = reader.pop(0)

    #counter = 0  #Counter for stopping the program after a number of rows (Commented out with # so it doesn't happen)
    
    for row in reader:
        if(row[0] == "Header"):
            continue

        #Check the sample counter and stop the program (Commented out with # so it doesn't happen)
        #counter += 1    
        #if(counter > 150):
            #break

        # If the new row is a subrow that should be added to the parent row above...
        if(row[0].strip().lower() == lastRow[0].strip().lower()):
            #Then add the subrow's Imace Src to the parent row's Image Src column (stored at column index [9] in the csv)
            lastRow[9] += delimiter + row[9]
            
        #If the new row is instead part of a new grouping...
        else:
            #Save the last good row into the result file
            doneRows.append(lastRow)
            #Prep the new row
            lastRow = row
            

###################################
#This part searches the Body section (stored at [2]) with regex and searches for a keyword that tells us its Type (stored at [4])
            #Some confusing regex
            typeString = re.findall(r"Sold as(.*?)<", lastRow[2].replace("\n", " "))

            #If we found something, make it lowercase
            if(typeString):
                typeString = typeString[0].lower()

            #If we found nothing, it's likely a Set
            if(not typeString):
                lastRow[4] = "Sets"

            #Determine what is a Set
            elif("includes" in typeString):
                lastRow[4] = "Sets"
            elif("set" in typeString):
                lastRow[4] = "Sets"
            #Determine all the other stuff
            elif("bobby" in typeString):
                lastRow[4] = "Pins"
            elif("earring" in typeString):
                lastRow[4] = "Earrings"
            elif("ring" in typeString):
                lastRow[4] = "Rings"
            elif("necklace" in typeString):
                lastRow[4] = "Necklaces"
            elif("bracelet" in typeString):
                lastRow[4] = "Bracelets"
            elif("anklet" in typeString):
                lastRow[4] = "Anklets"
            elif("hair clip" in typeString):
                lastRow[4] = "Hair clips"

            #If it didn't fit any of these keywords, leave Type as "Jewelry" and print it to tell us what wasn't caught by the search
            else:
                print(typeString)
#########################################


#Last chance to stop it from making a file
print("Algorithm done, press ENTER to confirm that you want to change the file " + outputfilename)
input()
csvfile.close()

#If user hits 'Enter' then finish up by writing the file
print('Old file closed, writing to new file')
with open(pathroot + outputfilename, 'w', newline='') as csvfile:
    finisher = csv.writer(csvfile, dialect = "excel", delimiter=',')
    for i in doneRows:
        finisher.writerow(i)
print("Done, new file is located at " + pathroot + outputfilename)
