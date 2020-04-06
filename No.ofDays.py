#This code calculates number of days between any two dates 
DATE1=input("Enter the first date in dd/mm/yyyy format: ")
DATE2=input("Enter the second date in dd/mm/yyyy format: ")
date1=DATE1.split("/")
date2=DATE2.split("/")
days=0
if int(date1[2])==int(date2[2]):
    if int(date1[1])==int(date2[1]):
        days = days + (int(date2[0])-int(date1[0]))
    else :
        days = days + int(date2[0])
        if int(date1[1])==1 or int(date1[1])==3 or int(date1[1])==5 or int(date1[1])==7 or int(date1[1])==8 or int(date1[1])==10 or int(date1[1])==12:
            days = days + (31-int(date1[0]))
            
        if int(date1[1])==4 or int(date1[1])==6 or int(date1[1])==9 or int(date1[1])==11:
            days = days + (30-int(date1[0]))
            
        if int(date1[1])==2:
            if (int(date1[2])%4==0) or (int(date1[2])%100==0 and int(date1[2])%400!=0):
                days = days + (29-int(date1[0]))
            else:
                days = days + (28-int(date1[0]))
        for i in range(int(date1[1])+1,int(date2[1])):
            if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
                days = days + 31
            if i==4 or i==6 or i==9 or i==11:
                days = days + 30
            if i==2:
               if (int(date1[2])%4==0) or (int(date1[2])%100==0 and int(date1[2])%400!=0):
                   days = days + 29
                   
               else:
                   days = days + 28
else:
    days = days + int(date2[0])
    if int(date1[1])==1 or int(date1[1])==3 or int(date1[1])==5 or int(date1[1])==7 or int(date1[1])==8 or int(date1[1])==10 or int(date1[1])==12:
            days = days + (31-int(date1[0]))
            
    if int(date1[1])==4 or int(date1[1])==6 or int(date1[1])==9 or int(date1[1])==11:
            days = days + (30-int(date1[0]))
            
    if int(date1[1])==2:
        if (int(date1[2])%4==0) or (int(date1[2])%100==0 and int(date1[2])%400!=0):
            days = days + (29-int(date1[0]))
        else:
            days = days + (28-int(date1[0]))
    for i in range(int(date1[1])+1,13):
        if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
                days = days + 31
        if i==4 or i==6 or i==9 or i==11:
                days = days + 30
        if i==2:
            if (int(date1[2])%4==0) or (int(date1[2])%100==0 and int(date1[2])%400!=0):
                   days = days + 29
            else:
                   days = days + 28
    for i in range(int(date1[2])+1,int(date2[2])):
        if (i%4==0) or (i%100==0 and i%400!=0):
            days = days + 366
        else:
            days = days + 365
    for i in range(1,int(date2[1])):
        if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
                days = days + 31
        if i==4 or i==6 or i==9 or i==11:
                days = days + 30
        if i==2:
            if (int(date2[2])%4==0) or (int(date2[2])%100==0 and int(date2[2])%400!=0):
                   days = days + 29
            else:
                   days = days + 28

print("Number of days between the two dates "+DATE1+" and "+DATE2+" are: {}".format(days))
        
        
            
    
            
            
        
    

