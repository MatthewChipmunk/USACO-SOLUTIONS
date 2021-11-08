num = open("teleport.in", 'r')
answer = open("teleport.out", "w")
#__________________________________________
nums = num.readlines()
nums = nums[0].split()
print(nums)
for i in range(len(nums)):
    nums[i] = int(nums[i])

start, end = nums[0], nums[1]
# 3 10 8 2
a = abs(nums[2]-start)+abs(end-nums[3])
b = abs(nums[3]-start)+abs(end-nums[2])
print(a, b)
c = abs(end-start)
answer.write(str(min(a,b, c)))
#__________________________________________
num.close()
answer.close()
