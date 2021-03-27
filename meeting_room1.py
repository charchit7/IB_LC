A =  [     [1, 18],
        [18, 23],
        [15, 29],
        [4, 15],
        [2, 11],
        [5, 13]
    ]

# Two pointers to iterator start array and end array. Iterate the time line, the current time active meeting is num of start minus num of end.

from collections import defaultdict

def solve(A):
    d = defaultdict(int)
    for a, b in A:
        d[a] += 1
        d[b] -= 1
    print(d)    
    ans = 0
    cnt = 0
    times = sorted(list(d.keys()))
    print(times)
    for t in times:
        cnt += d[t]
        ans = max([ans, cnt])
    
    return ans

#same as above method
from collections import defaultdict

def practice_meeting(arr):
    #create a dictionary
    # defaultdict(int) will also work
    meetings = defaultdict(lambda : 0)
    #we cannot sort the dictionary
    count = 0
    ans = 0

    for start_time, end_time in arr:
        meetings[start_time] += 1
        meetings[end_time] -= 1
    
    temp = sorted(list(meetings.keys()))
    print(temp)
    for i in temp:
        count += meetings[i]
        ans = max(count,ans)
    return ans

print(practice_meeting(A))

def solve1(A):
    
    end_times = []
    for meeting in A:
        end_times.append(meeting[1])
        
    A = sorted(A, key=lambda x:x[0])
    end_times.sort()
    
    max_overlapping = 0
    overlapping = 0
    curr_end = A[0][1]
    j = 0
    for meeting in A[1:]:
        start=meeting[0]
        end =  meeting[1]
        if start<curr_end:
            overlapping+=1
        while start>=end_times[j]:
            overlapping-=1
            if overlapping<0:overlapping=0
            j+=1
        if overlapping>max_overlapping:
            max_overlapping=overlapping
            
        if end>curr_end:
            curr_end = end
            
    return max_overlapping+1

print(solve(A))