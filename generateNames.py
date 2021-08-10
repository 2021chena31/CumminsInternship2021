def textGen(name, sList):
    for index, suffix in enumerate(sList):
        #new = sList[index]
        #print(str(name) + suffix)
        sList[index] = str(name) + suffix

    return sList
        

if __name__ == '__main__':
    sList = ['A.csv','B.csv','CA.csv','CE.csv','CR.csv','E.csv','M.csv','NE.csv',
             'NP.csv','NW.csv','PA.csv','PSO.csv','PSY.csv','R.csv']
    name = raw_input("File name: ")
    print(name)
    sList = textGen(name, sList)

    f = open('names.txt','w')
    for name in sList:
        #print(name)
        f.write(name + '\n')

    f.close()
        
