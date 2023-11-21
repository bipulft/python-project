def read_file():
    file = open('laptop.txt','r')
    laptop_id = 1
    myDict = {}
    for line in file:
        line = line.replace('\n','')
        myDict[laptop_id] = (line.split(','))
        laptop_id +=1
    file.close()
    return myDict
