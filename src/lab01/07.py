inp="thisisabracadabraItww1 qewwwajodawwjjnww12twwjh plkjmqqqqaqqqqrqqqqkqqqq kmbg5kvay bztgpyhazlhdyxskopl."
#I want mark 5 pls.
og=""
m1=0
m2=0
p=0
for i in range(0,len(inp)):
    if inp[i] in ("QWERTYUIOPASDFGHJKLZXCVBNM"):
        m1=i
        for t in range(i,len(inp)):
            if inp[t] in ("0123456789") and p==0:
                m2=t
                p=1
                for k in range(m1,len(inp),(m2-m1+1)):
                    og+=inp[k]
print(og)

