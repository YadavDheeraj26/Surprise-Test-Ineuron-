s = "loveleetcode"

for i,c in enumerate(s):
    if s.count(c)==1:
        print(i)
        break
print(-1)