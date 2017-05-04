AT = []
BT = []
axes = []
priority= []
print("Enter Number of processes:")
n=int(input())
for i in range(n):
    print("Priority for process: ",i+1)
    priority.append(int(input()))
    print("Arrival time for process :", i+1)
    AT.append(int(input()))
    print("Burst time for process :", i+1)
    BT.append(int(input()))

for i in range(n):
    axes.append(i+1)

for k in range(n):
     for l in range(n):
         if(priority[k] < priority[l]):
           index = burst_time[l]
           temp = arr_time[l]
           arr_time[l] = arr_time[k]
           arr_time[k] = temp
           burst_time[l] = burst_time[k]
           burst_time[k] = index
           b = priority[l]
           priority[l] = priority[k]
           priority[k] = b
           a = axes[l]
           axes[l] = axes[k]
           axes[k] = a
print ("ProcessNo.","TurnaroundTime","  ","WaitingTime")
finishtime=arr_time[0]
starttime=arr_time[0]
for i in range(n):
    finishtime += burst_time[i]
    starttime += arr_time[i]
    print(axes[i], "  \t\t", finishtime - arr_time[i], "  \t\t\t", (finishtime - arr_time[i]) - burst_time[i])