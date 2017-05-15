def swap(list,j,j+1):
    temp = list[j]
    list[j] = list[j+1]
    list[j+1] = temp


def availableProcess(cpuTime):
    min = 0
    j = 0
    print("cpu time:",cpuTime)
    for i in range(noProcess):
        for k in range(len(done)):
            if(i!=done[k]):
                if(arrivalTime[i]<=cpuTime):
                    j = j + 1
                    if(j< 1):
                        min = i
                    else:
                        if(burstTime[i]<burstTime[minBT]):
                            min = i
    done.append(min)
    return minBT


def takeInput():
    print("Enter number of processes:", end = ' ')
    noProcess = int(input())

    for i in range(nP):
        print("Enter arrival time for process ", i + 1, end = ": ")
        arrivalTime.append(int(input()))
        print("Enter burst time for process ", i + 1, end = ": ")
        burstTime.append(int(input()))
        processID.append(i+1)


def sortProcess():
    for i in range(noProcess):
        for j in range(noProcess-1):
            if(arrivalTime[j] > arrivalTime[j+1]):
                swap(arrivalTime,j,j+1)
                swap(burstTime,j,j+1)
                swap(processID,j,j+1)


takeInput()
sortProcess()

arriavlTime = []
burstTime = []
processID = []
done = []
noProcess = 0
cpuTime = 0
waitingTime = 0

for i in range(nP):
    minBT = availableProcess(cpuTime)
    if(arrivalTime[minBT]>cpuTime):
        waitingtime = arrivalTime[minBT] - cpuTime
    else:
        waitingTime = cpuTime - arrivalTime[minBT]
    print("Waiting time for process ", processID[minBT], "with arrival time ",arrivalTime[minBT],": ", waitingTime)
    print("Turn around time for process ", "with arrival time ",arrivalTime[minBT],": ", waitingTime + burstTime[minBT])
    cpuTime = cpuTime + burstTime[minBT]
