def takeInput():
    for i in range(noProcess):
    print('Arrival time of process P', i + 1,  end = ' ')
    aarivalTime.append(int(input()))
    print('Burst time of process P', i + 1,  end = ' ')
    burstTime.append(int(input()))

def isDone(j):
    for k in range(len(done)):
            if(j == done[k]):
                return True
    return False

def computewaitingTime(time):
    waitingTime = 0
    time = time + 1
        burstTime[smallest] = burstTime[smallest] - 1
        waitingtime = time - arrivalTime[smallest] - burstTime[smallest]
        turnaroundtime = wairingtime + burstTime[smallest]
        if(burstTime[smallest] == 0):
            done.append(smallest)
                       
    return waitingTime

burstTime = []  
aarivalTime = []  

print('Enter total number of process', end = ' ')
noProcess = int(input())

takeInput()

smallest = 0  # shortest job
done = [] # done processes
for j in range(n):
    if aarivalTime[j] < [smallest]:
        smallest = j
time = AT[smallest]
waitingtime = 0 
turnaroundtime = 0 
for i in range(n):
    for j in range(n):
        if(j==0):
            if (arrivalTime[j] <= time) and (burstTime[j] < burstTime[smallest]) and (burstTime[j] > 0):
                smallest = j
        if(isDone(j) == False):    
            if (burstTime[j] <= time) and (burstTime[j] < burstTime[smallest]) and (burstTime[j] > 0):
                smallest = j
        computewaitingTime(time)
        print('process', smallest + 1, ' Waiting_time:', waitingtime + 1, 'Turnaround_time:', turnaroundtime)
