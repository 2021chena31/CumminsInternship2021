##Written by Angie Chen (angie.chen@cummins.com), August 2021
##File v.1.2, last updated 8/12/2021
##
##This program combines combineNames.py and script2.py together.
##Since it's a combination, there are some parts of the code that may appear
##very inefficient.
##Instructions for use are also added to this program.
##Please refer to README.txt for more detail.

import os.path
from os import path



#Generate list of file names
def textGen(name, sList):
    for index, suffix in enumerate(sList):
        sList[index] = str(name) + suffix
        #suffix in sList is appended to the general file name
        
    return sList



#Writes list of file names to open in names.txt
def nameWrite(sList):
    #opens file in write-mode; previous data will be overwritten
    f = open('names.txt','w')
    
    for name in sList:
        f.write(name + '\n')

    f.close()



#Pulls list of file names from names.txt and returns list
def pullNames():
    try:
        #open file on read-only
        f = open('names.txt','r')

        #create list of fileNames
        fileNames = []
        
        for line in f:
            line = line.strip('\n') #clear out all extra newlines
            fileNames.append(line) #add the file name into a list of file names

        f.close()

        return fileNames
    
    except IOError:
        #If this error appears, then names.txt is missing
        #This should NOT be an issue for this program because names.txt
        #will always be created
        print("ERROR: Invalid file name in pullNames()")
        print("Please fix error and restart program.")



#Add the rows from a file to the dictionary
def addDict(fileName, keyIndex=0, dictionary={}):
    try:
        curFile = fileName
        f = open(fileName,'r') #open the file on read only to parse the data
        lines = f.readlines() #convert file to list of strings

        #goes through every string in the list (i.e. every file line)
        for index, line in enumerate(lines):
            line = line.strip("\n") #remove extra newlines
            listLine = line.split(",") #breaks the line into a list of strings
            
            key = listLine[keyIndex] #the dictionary key becomes the chosen index
            listLine.pop(keyIndex) #remove the key from the list
            
            entry = listLine
            noDuplicate = True #assume there is no duplicate

            #key is already occupied
            if dictionary.has_key(key):
                #oldEntry is what is the dictionary, previously
                oldEntry = dictionary[key]

                #compare each previous 'entry' in the dictionary
                for subList in oldEntry:
                    #compare each value of the entry

                    #go through all the entries in the sublist
                    for index, oldValue in enumerate(subList):
                        
                        if len(entry) > index and oldValue != entry[index]:
                            #a singular different value means it's not a duplicate
                            noDuplicate = True
                            break #breaks out of the current row
                        else:
                            noDuplicate = False

                    #a duplicate is found from the previous loop
                    #which means the entry is a duplicate and should not be added
                    if not(noDuplicate):
                        break
                    
                #same key, but different data
                if noDuplicate and (len(entry) != 0):
                    #adds the entry to list in the dictionary key
                    dictionary[key].append(entry)
           
            #Key does not already exist
            else:
                #Automatically create an entry with a sublist
                dictionary[key] = [entry]

        f.close()
        return dictionary

    except IOError:
        #Not necessarily a bad thing if the file simply does not exist
        #but notifies user if the program is missing a file
        print("Notice (addDict): " + str(fileName) + " is missing")


                
def writeDictToFile(dictionary,name='temp.csv'):
    try:
        #file is created as temp.csv, unless otherwise selected
        if path.exists("temp.csv"):
            name = raw_input("Please input new name: ")

        #create new file with the name selected
        newF = open(name, 'w')

        print("Writing data to file...")

        #goes through every entry in the dictionary
        for key in dictionary:
            #gets all entries that share the same key
            subList = dictionary[key]
            
            #go through list of subLists (all linked to single key)
            for index, row in enumerate(subList):
                newString = str(key) + ',' #starts the new row

                #go through the sublist (columns in each row)
                for entry in subList[index]:
                    #adds each column to the row
                    newString = newString + str(entry) +','
                    
                newF.write(newString + '\n') #writes the new row to the new file

        newF.close()
        print("CSV file is created: " + str(name))
        return None
    
    except KeyError:
        newF.close()
        print("ERROR: No dictionary exist; i.e. no files in fileNames")
        
    except IndexError:
        #yeah hopefully this shouldn't happen
        newF.close() #exit out of file
        print("ERROR (writeDictToFile): File closed and transfer incomplete")
        print("Error with program index; possible programming bug")



if __name__ == '__main__':
    #SUFFIX LIST
    #Suffixes are the ones I used to differentiate the csv files.
    #Feel free to change them as needed
    sList = ['A.csv','B.csv','CA.csv','CE.csv','CR.csv','E.csv',
             'M.csv','NE.csv','NP.csv','NW.csv','PA.csv','PSO.csv',
             'PSY.csv','R.csv']


    #GENERATE AND WRITE NAMES
    print("Please input general file name. (ex. QuoteUnit) ")
    name = raw_input("File name: ")
    sList = textGen(name, sList) #generate file names
    nameWrite(sList) #write file names into a text document
    

    #COMBINE FILES
    fileNames = pullNames() #get list of files to iterate through
    dictionary = {} #set up a blank dictionary

    print("Loading data from files...")
    try:
        for index, fileName in enumerate(fileNames):
            #calls addDict() for each file
            #information from each file is added to dictionary
            dictionary = addDict(fileName)
    
    except IOError:
        #If this error appears, then a file in names.txt is not present
        #The program will still work for all of the remaining files
        print("File is missing in main")

    print("Data loaded to dictionary.")   
    writeDictToFile(dictionary) #creates the combined csv file
    
