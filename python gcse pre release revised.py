import random
busnames=["busA","busB","busC","busD","busE","busF"]
busdata = [[],[],[],[],[],[]]
days = 20
totallate = []
buslatemins = [[],[],[],[],[],[]]
latearrival = []
late = 0

for i in range(6):
    for j in range(days):
        errors = True
        while errors == True:   
            print("please enter the minutes late of", busnames[i],"on day",j+1,)
            minutes=input("data must be a interger with - meaning late and + meaning early and 0 meaning on time")
            try:
                minutes=int(minutes)
                errors = False
            except:
               print("wrong data type - enter number please")
                
       #minutes = random.randrange(-10,10,2)
    busdata[i].append(minutes)
       #print(busdata[i])

for i in range(6):
    x = 0
    
    for j in range(days):
    # This is to calculate the number of late arrivals for each bus route    
        mins_late_per_day = busdata[i][j]
        #print (mins_late_per_day)
        if (mins_late_per_day) < 0:
            x += 1
            buslatemins[i].append(mins_late_per_day)
            
    latearrival.append(x)
    print(busnames[i],"is late", latearrival[i],"times")
    
    #This is to calcuate mean minutes late
    totallate.append(sum(busdata[i])/20)
    print(busnames[i],"has an average late minute of", totallate[i])
    
    #use sum to find avarage of only late times
    print(busnames[i],"has an averge late time of", sum(buslatemins[i])/(latearrival[i]),"taking into account only late days")

maximum = max(latearrival)
for i in range(6):
    if maximum == latearrival[i]:
        print (busnames[i], "is the latest bus")

#task 3
specific = input("please enter which day 1-20 you would like to analyse")
p = int(specific)-1
for i in range(6):
    print (busnames[i], "has time", busdata[i][p], "today")
    if busdata[i][p]<0:
        print(busnames[i], "is late today")
        late +=1

print (late,"buses were late today")

    

