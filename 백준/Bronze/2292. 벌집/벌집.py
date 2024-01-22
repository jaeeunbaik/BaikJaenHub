N= int(input())

layer=1
cnt = 1

while N > layer:
    layer += cnt*6
    cnt += 1
    
print(cnt)