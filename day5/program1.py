# Replace all '0' with '5' in an input integer.

n=int(input(" Enter the number:"));
s=str(n)
g=""
for i in s:
    if(i=='0'):
        g=g+'5'
    else:
        g=g+i
t=int(g);
print(t)


