

# now calculating the net charges on the lower half and upper half from this txt file

# input variable declaration
outputfile = open(newfile,"r")
charges=[]
atomnumber=[]
atomname=[]
content=outputfile.readlines()
sum_lowerhalf=0.0
sum_upperhalf=0.0
lowerhalf_list=[1,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25]
upperhalf_list=[2,3,4,5,6,9,17,26,27,28,29,30]


#splitting the content into different columns named atomnumber, atomname, charges

for i in content:
	column=i.split()
	atomnumber.append(column[0])
	atomname.append(column[1])
	charges.append(column[2])

#Doing the summation of charges on the lowerhalf and upperhalf

for j in atomnumber:
	if int(j) in lowerhalf_list:
				x=int(j)-1
				k=charges[x]
				sum_lowerhalf=sum_lowerhalf+float(k)
	elif int(j) in upperhalf_list:
				x=int(j)-1
				l=charges[x]
	   			sum_upperhalf=sum_upperhalf+float(l)
outputfile.close()


# printing the net charges in the txt file

outputfile=open(newfile,"r+w")
word1="The net charge on lower half is " 
word2="The net charge on upper half is "
readline=outputfile.readlines()
for line in range(len(readline)+3):
   i=line
   if i>62:
    print >>outputfile
    print >>outputfile, "%s%s"  % (word1, str(sum_lowerhalf))
    print >>outputfile, "%s%s" % (word2, str(sum_upperhalf))
    break
