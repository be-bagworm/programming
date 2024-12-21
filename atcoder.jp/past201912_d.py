n = int(input())

args = [0 for i in range(n)]
for i in range(n):
    args[int(input())-1] += 1

# 存在しない数字
zero = -1
# 重複している数字
two  = -1

for i in range(n):
    if args[i] == 0:
        zero = i+1
    if args[i] == 2:
        two = i+1

if zero == -1:
    print('Correct')
else:
    print(f"{zero} {two}")
