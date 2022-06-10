import sys

input= sys.stdin.readline
N= int(input())
array=[]
for i in range(N):
    e=int(input())
    array.append(e)


def bubble_sort(arr):
    button=0
    for end in range(len(arr),0,-1):
        for i in range(1,end):
            if arr[i]<arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
                button=1
            elif button==0:
                break
        if button==0:
            break
def bubble_sort_extreme(arr):
    end=len(arr)
    while end>0:
        last_swap = 0
        for i in range(end-1):
            if arr[i]>arr[i+1]:
                arr[i+1],arr[i]=arr[i],arr[i+1]
                last_swap= i
        end=last_swap


bubble_sort(array)
print(array)