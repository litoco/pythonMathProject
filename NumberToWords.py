a = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
b = ['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']
c = 'hundred'
d = ['thousand', 'million', 'billion', 'trillion']

i = input('Enter : ')
finalstring=''
numberinlist=[]
firstgroup=len(i)%3
count=0
stringtoadd=""
operationnumber=0

for x in i:
	count+=1
	stringtoadd+=x##adding the numbers one by one to a string
##	now
##	we are making groups of 3 starting from leftmost numbers entered
##	hence the last group can have any number of members(this last group will have the heighest palce value like trillion, brillion etc.)
	if(count==firstgroup or (count-firstgroup)%3==0):
		numberinlist.append(stringtoadd)##adding the number to list to assign the place value
		stringtoadd=''##making string back to null to add other groups
count=0
for x in numberinlist:
    count+=1
    operationnumber=int(x)
    tenscount=0
    while(operationnumber!=0):##till operationnumber is non zero with the help of the operationnumber we can find the wording of the number
        if(operationnumber/100>0):
            finalstring+=a[operationnumber/100]+" "##finalstring is the string containing the number in word form
            finalstring+='hundred '##if the grouped number is divisible by 100 then it should contain hundred
            operationnumber%=100##if the number is added in the word then the remaining number should be processed here after
        else:
            if(operationnumber<=(len(a)-1)):##if operationnumber is in a
                finalstring+=a[operationnumber]+" "
                operationnumber=0##finally operation number is found and implemented now is set to 0 to complete loop
            else:
                tenscount = operationnumber/10##if operationnumber is divisible by 10 then its stored in tenscount  and founded in b
                if(tenscount!=0):##operationnumber is not divisible by 10
                    finalstring+=b[tenscount-2]+' '
                    operationnumber%=10##operationnumber is updated to contain numbers within a

    placevalue=len(numberinlist)-1-count##adding placevalue digit to placevalue
    if(placevalue>=0):
        finalstring+=d[placevalue]+' '##adding corresponding word of placevalue to finalstring

print(finalstring)

    


