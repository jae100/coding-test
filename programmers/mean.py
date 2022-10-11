arr = [1,2,3,4]

def solution1(arr):
   return (sum(arr)/len(arr))

print(solution1(arr))

def solution2(arr):
    answer = 0

    for i in arr:
        answer += i

    return answer / len(arr)
print(solution2(arr))