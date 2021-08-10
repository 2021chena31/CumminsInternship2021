import os.path
from os import path

#pulls list of file names and returns list
def pullNames():
    try:
        #open file on read-only
        f = open('names.txt','r')        
        fileNames = []
        
        for line in f:
            line = line.strip('\n')
            fileNames.append(line)

        f.close()

        return fileNames
    
    except IOError:
        print("Invalid file name in pullNames()")



#go through all the files in the list    
def fileIteration(fileNames):
    dictionary = {} #set up a blank dictionary
    
    try:       
        for index, fileName in enumerate(fileNames):
            dictionary = addDict(fileName)
            
        return dictionary

    except IOError:
        print("File is missing in fileIteration(): {}".format(fileName))


def addDict(fileName, keyIndex=0, dictionary={}):
    try:
        curFile = fileName
        f = open(fileName,'r')
        lines = f.readlines() #convert file to list of strings

        for index, line in enumerate(lines):
            line = line.strip("\n")
            listLine = line.split(",")
            key = listLine[keyIndex] #the dictionary key becomes the chosen index

            #print(listLine)
            
            listLine.pop(keyIndex) #remove the key from the list

            entry = listLine #change key to line[-1] and entry line[:-1]

##            #is the two dictionary entries the same
##            isSame = True #assumes they are the same unless proven otherwise

            noDuplicate = True #assume there is no duplicate


            #key is already occupied
            if dictionary.has_key(key):
                oldEntry = dictionary[key]

                #compare each previous 'entry' in the dictionary
                for subList in oldEntry:
                    #compare each value of the entry
                    
                    for index, oldValue in enumerate(subList):
                        
                        if len(entry) > index and oldValue != entry[index]:
                            #isSame = False
                            noDuplicate = True #not a duplicate
                            break #breaks out of the current row
                        else:
                            #isSame = True
                            noDuplicate = False

                    if not(noDuplicate): #a duplicate if found from the previous loop
                        break
                    
                #same key, but different entries/columns
                #if not(isSame):
                if noDuplicate:
                    dictionary[key].append(entry)
           
            #key does not already exist; automatically create sublist
            else:
                dictionary[key] = [entry]

        f.close()
        return dictionary

    except IOError:
        print("File is missing in addDict()")


                
def writeDictToFile(dictionary,name='z.csv'):
    try:
        if path.exists("null.csv"): #https://www.guru99.com/python-check-if-file-exists.html
            name = raw_input("Please input new name: ")
            
        newF = open(name, 'w') #create new file

        for key in dictionary:
            subList = dictionary[key]
            
            #go through list of subLists (all linked to single key)
            for index, row in enumerate(subList):
                newString = str(key) + ',' #starts the new row

                #go through the sublist (columns in each row)
                for entry in subList[index]:
                    newString = newString + str(entry) +','
                    
                newF.write(newString + '\n') #writes the new row

        newF.close()
        print("CSV file is created")
        return None
    
    except KeyError:
        print("No dictionary exist; i.e. no files in fileNames")
    except IndexError: #exit out of file
        newF.close()
        print("Index Error: File complete")



if __name__ == "__main__":
    fileNames = pullNames() #get list of files to iterate through
    dictionary = {} #set up a blank dictionary
    
    try:       
        for index, fileName in enumerate(fileNames):
            dictionary = addDict(fileName)
    except IOError:
        print("File is missing in main")
        
    #print(dictionary)
    
    writeDictToFile(dictionary)








    
