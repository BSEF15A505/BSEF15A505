AT = []
BT = []
pID = []
done = []

def swap(a,b):
    temp = a
    a = b
    b = temp


def availableProcess(cpuTime):
    minBT = 0
    j = 0
    print("cpu time:",cpuTime)
    for i in range(nP):
        for k in range(len(done)):
            if(i!=done[k]):
                if(AT[i]<=cpuTime):
                    j = j + 1
                    if(j< 1):
                        minBT = i
                    else:
                        if(BT[i]<BT[minBT]):
                            minBT = i
    done.append(minBT)
    return minBT

print("Enter number of processes:", end = ' ')
nP = int(input())

for i in range(nP):
    print("Enter arrival time for process ", i + 1, end = ": ")
    AT.append(int(input()))
    print("Enter burst time for process ", i + 1, end = ": ")
    BT.append(int(input()))
    pID.append(i+1)


for i in range(nP):
    for j in range(nP-1):
        if(AT[j] > AT[j+1]):
            swap(AT[j],AT[j+1])
            swap(BT[j],BT[j+1])
            swap(pID[j],pID[j+1])

print("\n\n")

cpuTime = 0
w_time = 0

for i in range(nP):
    minBT = availableProcess(cpuTime)
    if(AT[minBT]>cpuTime):
        w_time = AT[minBT] - cpuTime
    else:
        w_time = cpuTime - AT[minBT]
    print("Waiting time for process ", pID[minBT], "with arrival time ",BT[minBT],": ", w_time)
    print("Turn around time for process ", "with arrival time ",BT[minBT],": ", w_time + BT[minBT])
    cpuTime = cpuTime + BT[minBT]

print(len(done))