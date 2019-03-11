stringcopy=''
stringlist=[]
inputstring=''
start=0
end=0
net=0
placevalue=0

a = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
b = ['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']
c = 'hundred'
d = ['trillion', 'billion', 'million', 'thousand']

def stringcopyfun():
    global stringcopy,inputstring
    for i in range(start,end+1):
        stringcopy+=inputstring[i]

def changetonumber():
    global stringcopy,stringlist,tempstring,end,net,start
    stringlist=stringcopy.split(' ')
    tempstring='0'
    for i in stringlist:
        count=-1
        for x in a:
            count+=1
            if(i==x):
                tempstring=int(tempstring)+count
                break
        count=1
        for x in b:
            count+=1
            if(i==x):
                tempstring=int(tempstring)+count*10
                break
        if(i==c):
            tempstring=int(tempstring)*100
    stringcopy=str(tempstring)

def addplacevalue(placevalue):
    global stringcopy,net
    for x in range(placevalue):
        stringcopy+='000'
    net+=int(stringcopy)

inputstring=input("Enter : ")
count=0
length=0
for i in d:
    ispresent=inputstring.find(i)
    if(ispresent!=-1):
        start=end+length
        length=len(i)
        end=ispresent-1
        stringcopyfun()
        changetonumber()
        addplacevalue(len(d)-count)
    count+=1
start=end+length
end=len(inputstring)-1
stringcopyfun()
changetonumber()
net+=int(stringcopy)
print(net)
