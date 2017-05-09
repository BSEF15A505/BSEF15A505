BT = []  # burst time
AT = []  # arrival time

print('Enter total number of process', end = ' ')
n = int(input())

for i in range(n):
    print('Arrival time of process P', i + 1,  end = ' ')
    AT.append(int(input()))
    print('Burst time of process P', i + 1,  end = ' ')
    BT.append(int(input()))

smallest = 0  # shortest job
done = [] # done processes
for j in range(n):
    if AT[j] < AT[smallest]:
        smallest = j;
time = AT[smallest]
w_time = 0 # waiting time
t_time = 0 # turnaroud time
for i in range(n):
    for j in range(n):
        if(j==0):
            if (AT[j] <= time) and (BT[j] < BT[smallest]) and (BT[j] > 0):
                smallest = j
        for k in range(len(done)):
            if(j != done[k]):
                if (AT[j] <= time) and (BT[j] < BT[smallest]) and (BT[j] > 0):
                    smallest = j
        time = time + 1
        BT[smallest] = BT[smallest] - 1
        w_time = time - AT[smallest] - BT[smallest]
        t_time = w_time + BT[smallest]
        if(BT[smallest] == 0):
            done.append(smallest)
        print('process', smallest + 1, ' Waiting_time:', w_time + 1, 'Turnaround_time:', t_time)
