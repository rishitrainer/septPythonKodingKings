path = "/RISHI/H2K/H2KProjects/SEDAP/CustomerWatchTime_04052020.csv"
'''
 'r' - rt = read only and text
'w' 'a' - write, append 
write - existing data is wiped out
append - data appended to existing data
'x' - create mode 

't' - text
'b' - binary

'''
file = open(path)
# print(file.read())
# print(file.read())

for eachRow in file:
    eachRowDisect = eachRow.split(',')
    #print(eachRowDisect, type(eachRowDisect))
    #print(eachRowDisect[1:4])
    if eachRowDisect[2] == "Linwud" :
        print(eachRowDisect)
    elif eachRowDisect[2].find("Lin") > -1:
        print("in Else Clause" , eachRowDisect)