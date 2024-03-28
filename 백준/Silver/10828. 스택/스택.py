N = int(input())

stack = []
answer = []
e = 0

for _ in range(N):
    line = input()
    cmd = line.split(' ')[0]
    if cmd == 'push':
        x = int(line.split(' ')[-1])
        stack.extend([x])
    elif cmd == 'top':
        if stack == []:
            answer.extend([-1])
        else: answer.extend([stack[-1]])
    elif cmd == 'size':
        answer.extend([len(stack)])
    elif cmd == 'empty':
        if stack == []:
            answer.extend([1])
        else: answer.extend([0])
    elif cmd == 'pop':
        if stack == []:
            answer.extend([-1])
        else: 
            answer.extend([stack[-1]])
            stack = stack[:-1]

    
for i in range(len(answer)):
    print(answer[i])        