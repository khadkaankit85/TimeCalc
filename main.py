from datetime import datetime
dateformat="%Y-%m-%d %H:%M:%S"
timeList=[]
dayOne=[]
dayAll=[]
def menu():
    print("Kindly Select One of the Option Below: ")
    print("1. Log In\n2. Log Out\n3.View History")
    

def punchIn():
    uneditedTime1=datetime.now()
    logInTime=str(uneditedTime1.replace(microsecond=0))
    with open("StudiedTime.txt","a") as textfile:
        textfile.write(logInTime+"==>")
        
def punchOut():
    uneditedTime2=datetime.now()
    logOutTime=str(uneditedTime2.replace(microsecond=0))
    with open ("StudiedTime.txt","a") as textfile:
        textfile.write(logOutTime+"\n")
        
        
def studiedTime():
    with open("StudiedTime.txt","r") as mainfile:
        lines=mainfile.readlines()
        for line in lines:
            dateStr=line.split("==>")
            for dateString in dateStr:
                dateformatted=datetime.strptime(dateString.strip(),dateformat)
                timeList.append(dateformatted)
            
        for i in range(0,len(timeList)-1,2):
            dayOne=timeList[i+1]-timeList[i]
            dayAll.append(dayOne)
            
        for i,screentime in enumerate(dayAll,start=1):
            print(f"{i}. I Studied for {screentime}.\n")
        
    
while True: 
    menu()
    selection=input("Please Enter here: ")
    if int(selection)==1:
        punchIn()
        break
    elif int(selection)==2:
        punchOut()
        break
    elif int(selection)==3:
        studiedTime()
        break
    else:
        print("Have fun!! ")
        break
