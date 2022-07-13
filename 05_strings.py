a="First"
b="Program"
c=a+b
print(c)

print(c[4])

#string slicing
print(c[0:4]) #prints string from index 0 to (4-1) i.e 3
print(c[-5:-1]) #from back side of string index no as -1,-2......

print(c[0::3]) #slice with a skip value skips every (skip-1) characters from the string

print(len(c))
print(c.endswith('m')) #tells whether string ends with the parameter passed or not
print(c.count(a)) #counts occurance of passed string in str
print(c.find("rst")) #finds whether a string is present or not if present returns the index from where string starts

print(c.replace("st","ts")) #replaces old word with a new word