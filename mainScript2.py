##Written by Angie Chen (angie.chen@cummins.com), August 2021
##File v.1.1, last updated 8/12/2021
##
##This program is a modified version of mainScript2.py which allows combination
##of multiple general files in one go.
##Please refer to README2.txt for more detail.

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
        print("ERROR (pullNames): Invalid file name")
        print("Please fix error and restart program.")



#Add the rows from a file to the dictionary
def addDict(fileName, dictionary={},keyIndex=0):
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
        print("Possible Error (addDict): " + str(fileName) + " is missing")


                
def writeDictToFile(dictionary,name=''):
    try:
        #create new file with the name selected
        name = PREFIX + name + '.csv'
        newF = open(name, 'w')

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
        print("ERROR (writeDictToFile): No dictionary exists; ie. no files in fileNames")
        
    except IndexError:
        #yeah hopefully this shouldn't happen
        newF.close() #exit out of file
        print("ERROR (writeDictToFile): File closed and transfer incomplete")
        print("Error with program index; possible programming bug")
        


if __name__ == '__main__':
    #GET FILES LIST
    files = open('files.txt','r')
    filesList = files.readlines()

    #COMBINE FILES
    for curFile in filesList:
        
        #Suffix list:
        #Suffixes are the ones I used to differentiate the csv files.
        #Feel free to change them as needed
        sList = ['A.csv','B.csv','CA.csv','CE.csv','CR.csv','E.csv',
             'M.csv','NE.csv','NP.csv','NW.csv','PA.csv','PSO.csv',
             'PSY.csv','R.csv']
        
        #Prefix:
        #Feel free to chance prefix into whatever is needed
        PREFIX = 'zNew-'
        
        curFile = curFile.strip('\n') #remove newlines
        
        sList = textGen(curFile, sList) #generate file names
        nameWrite(sList) #write file names into a text document
        fileNames = pullNames() #get list of files to iterate through
        dictionary = {}

        try:
            for index, fileName in enumerate(fileNames):
                #calls addDict() for each file
                #information from each file is added to dictionary
                dictionary = addDict(fileName)
        
        except IOError:
            #If this error appears, then a file in names.txt is not present
            #The program will still work for all of the remaining files
            print("ERROR (main): " + str(fileName) + " is missing")
            
        try:
            writeDictToFile(dictionary, curFile) #creates the combined csv file
            dictionary.clear() #wipe the dictionary
        except TypeError:
            #No files were parsed or csv files are empty/missing
            print("ERROR (main): Type - Dictionary is empty; "+
                  "ie. invalid file "+str(PREFIX)+str(curFile)+'.csv'+" in files.txt")
            print("File transfer incomplete for "+str(PREFIX)+str(curFile)+'.csv')
        except AttributeError:
            #No files were parsed or csv files are empty/missing
            print("ERROR (main): Attribute - Dictionary is empty; "+
                  "ie. invalid file in files.txt")
            print("File transfer incomplete for"+str(PREFIX)+str(curFile)+'.csv')

    files.close()
        
