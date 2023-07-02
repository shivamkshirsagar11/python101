s = input("give str: ")
n = len(s)
def perm(i, t):
    if i == n:
        print(t)
        return 
    perm(i+1, t+s[i])
    perm(i+1, t)
perm(0, '')