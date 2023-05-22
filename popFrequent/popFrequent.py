print("Hello multiverse")
arrayGiven = [1, 2, 3, 4, 2, 4, 1, 1, 1, 3, 4,-1, -1, -1, -1, -1, -1]
testArrayGiven = [4,1,-1,2,-1,2,3]
sortedArrayGiven = sorted(testArrayGiven)
dictionary = {}
while len(sortedArrayGiven):
    character = sortedArrayGiven.pop(0)
    count = 1
    while sortedArrayGiven and sortedArrayGiven[0] == character:
        sortedArrayGiven.pop(0)
        count += 1
    
    dictionary[character] = count
    sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
frequentKeys = list(sorted_dict.keys())[:2]
print(frequentKeys)

