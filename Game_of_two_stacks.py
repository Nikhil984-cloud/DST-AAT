def two_Stacks(max_sum, a, b):
    sum_so_far = 0
    max_count = 0
    i = 0

    while i < len(a) and sum_so_far + a[i] <= max_sum:
        sum_so_far += a[i]
        i += 1
    max_count = i

    j = 0
    while j < len(b):
        sum_so_far += b[j]
        j += 1
        while sum_so_far > max_sum and i > 0:
            i -= 1
            sum_so_far -= a[i]
        if sum_so_far <= max_sum:
            max_count = max(max_count, i + j)

    return max_count

max_sum = 10
a = [4, 2, 4, 6, 1]
b = [2, 1, 8, 5]

result = two_Stacks(max_sum, a, b)
print(result)
