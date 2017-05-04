
BT = [] # burst time
AT = []   #  arrival time
WT = 0 # waiting time
TT = 0 # turnaround time

print('enter total number of process')
n = int(input())


for i in range(n):
    print('Arrival time of process P',i+1)
    AT.append(int(input()))
    print('Burst time of process P',i+1)
    BT.append(int(input()))

b=[] # burst time
for i in range(n):
    b.append(BT[i])

smallest=0 # shortest job
b_time=0 # burst time variable
for j in range(n):
   if AT[j] < AT[smallest]:
         smallest=j;
time = AT[smallest]

i=0
for i in range(n):
    smallest = n
    for j in range(n):

        if (AT[j] <= time) and (BT[j] < BT[smallest]) and (BT[j] > 0):
             smallest = j
    BT[smallest] = BT[smallest]-1
    time = time + 1
    if BT[smallest] is 0:
        WT = time - AT[smallest] - b[smallest]
        TT = WT + b[smallest]
        iA=i+1
        print('process', smallest+1, ' Waiting_time:', WT, 'Turnaround_time:', TT)