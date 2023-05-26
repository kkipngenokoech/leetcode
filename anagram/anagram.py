print("Hello multiverse")

word = "a"
anagram = "ab"
anagramArray = list(anagram)
print(anagramArray)

for letter in word:
    if letter in anagramArray:
        anagramArray.remove(letter)
        flag = True
        continue
    else:
        flag = False
        break
print(anagramArray)
print(flag)
if anagramArray == [] and flag:
    print("this is an anagram")
else:
    print("No Anagram array")