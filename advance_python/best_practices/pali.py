def pali_for(s):
    n = len(s)
    return all([s[i]==s[n-i-1] for i in range(n)])             
print(pali_for("nitin"))