numbers = [4,2,1]

def average(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum / len(nums)

print(average(numbers))