from datetime import datetime
dateformat="%Y-%m-%d %H:%M:%S.%f"
timeList=[]
with open("StudiedTime.txt","r") as file:
    lines=file.readlines()
    for line in lines:
        formatedDate=datetime.strptime(line.strip(),dateformat)
        timeList.append(formatedDate)
        StudiedTime=timeList[-1]-timeList[0]
#         print(StudiedTime)
# from datetime import datetime
# a =datetime.now()
# i=0
# while True:
#     print(i)
#     i+=1
#     if i ==99999:
#         break
# b=datetime.now()
# print(b-a)
# try:
#     print(a+b)
# except Exception as e:
#     print(e)