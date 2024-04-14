def f (x):
    ans = 16 -(x**2)
    return ans

answer = 0.0
n = 4
for i in range(n):
    answer += f(i+0.5)

print answer
x = 5
temp = 16-(x**2)
print temp
