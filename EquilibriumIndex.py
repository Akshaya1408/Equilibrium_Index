def find_equilibrium_index(A):
    total_sum = sum(A)
    left_sum = 0

    for i, num in enumerate(A):
        right_sum = total_sum - left_sum - num

        if left_sum == right_sum:
            return i

        left_sum += num

    return -1

A = list(map(int,input().split()))
output = find_equilibrium_index(A)
print(output) 
