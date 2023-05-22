word = "abcd"
word2 = "abecd"
convertToArray = list(word2)
for character in word2:
    if character not in word:
        print (character)

for character in word:
    if character  in convertToArray:
        convertToArray.remove(character)
        print(character)
print(convertToArray)

