def is_anagram(lst):
    result=[]
    for i in range(len(lst)-1):
        # print(sorted(lst[i]))
        # print(sorted(lst[i+1]))
        # input()
        if sorted(lst[i]) == sorted(lst[i+1]):
            result.append((lst[i],  lst[i+1]))

    return result

lst=["heart","earth", "act","tac","cat","rahul","imran",
"stones","tones","god","dog"]

print(is_anagram(lst))



def is_anagram2(a,b):
    return sorted(a)==sorted(b)

print(is_anagram2("earth","heart"))