#!/usr/bin/python3
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
def best_score(a_dictionary):
    return dict(sorted(a_dictionary.items(), key=lambda item: item[1])).popitem()

print (best_score(a_dictionary))
