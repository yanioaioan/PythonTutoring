import csv

'''format modes r,rb,w,wb'''
'''On Windows, 'b' appended to the mode opens the file in binary mode, so there are also modes like 'rb', 'wb', and 'r+b'.
    Python on Windows makes a distinction between text and binary files; the end-of-line characters in text files are automatically
    altered slightly when data is read or written. This behind-the-scenes modification to file data is fine for ASCII text files, but it'll
   corrupt binary data like that in JPEG or EXE files. Be very careful to use binary mode when reading and writing such files. On Unix,
   it doesn't hurt to append a 'b' to the mode, so you can use it platform-independently for all binary files.'''

#open and read csv files
ifile  = open('MediaResults.csv', "r") 
reader = csv.reader(ifile, delimiter=',')
ofile  = open('MediaResults_copy.csv', "w")
writer = csv.writer(ofile, delimiter=':')

#write to csv files
for row in reader:
    writer.writerow(row)

ifile.close()
#need to close the testConvertfile first, and then I can open it with ifile2
ofile.close()

##################################################################################################################################################

#re-read csv
r = csv.reader(open('MediaResults_copy.csv'),delimiter=':') # Here your csv file
#lines will contain all rows of r
lines = [l for l in r]
print(r)


'''Iterate throught the file'''
rows=len(lines)
columns=len(lines[0])
print("rows="+str(rows))
print("columns="+str(columns))

#lines[0][0]




#lines[0][0]
print ('\nusing the sequence to iterate all elements 1by one')
for row in lines:
    for column in row:
        print (column)


print ('\nusing range')
for r in range(rows):
    for c in range(columns):
        print (lines[r][c])


print ('\nprint an updated csv file (update the 2nd column elements)')
'''update csv file (update the 2nd elements)'''
for r in range(rows):
    #r goes from 0 to 1
    for c in range(columns):
        #c goes from 0 to 1
        if c==1:#talking about the 2nd column element

            #here we mutate/change/update the element
            lines[r][c]='A'
            print ("lines changed="+str(lines[r]))


##################################################################################################################################################

#Well lets ovewrite file
###Update the contents of the already opened file 'ifile'
#read file
#change file in memory
#write out file (overwriting existing file)


print ('NOW update the actual update/overwrite of the file ')

overWriteFilewriterofile  = open('MediaResults_copy.csv', "wb")
overWriteFilewriter = csv.writer(overWriteFilewriterofile, delimiter='\t', quotechar='"')
#write all the lines at once after we have read them and modified them
overWriteFilewriter.writerows(lines)
overWriteFilewriterofile.close()



##################################################################################################################################################

#Well lets create another file with the modified contents of the 'MediaResults_copy.csv'


'''
ifile2  = open('MediaResults_copy.csv', "rb")
reader2 = csv.reader(ifile2, delimiter=':')#: would not recognise the TAB delimeter properly
ofile2  = open('updatedTestConvert.csv', "wb")
writer2 = csv.writer(ofile2, delimiter=':', quotechar='"')

for row in reader2:
    #print (row)
    print ('row-->'+str(row)+' has '+str(len(row))+' elements')
    for element in row:
        print ('element='+str(element))
    #print (row[0])#1st element
    #print (row[1])#2nd element

    #actual update before writing it back to the new updateDTestConvert.csv file
    row[1]='Z'
    writer2.writerow(row)



ifile2.close()
ofile2.close()
'''
