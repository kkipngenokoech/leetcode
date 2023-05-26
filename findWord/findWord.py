#!/usr/bin/python

print("Hello Multiverse!")

haystack = "Hello multiverse!"
needle = "multiverse"

if needle in haystack:
    index = haystack.find(needle)
    print(needle)
    print(index)
else:
    print("Haystack does not contain needle!")