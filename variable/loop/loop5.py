# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)
# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)

i = 1
while i<=10:
    if(i%2 ==0):
        i +=1
        continue #skip
    print(i)
    i +=1
