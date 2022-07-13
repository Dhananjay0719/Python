'''input func helps to take input from user regardless
of what the user enters it is converted to string
that is output of input func is a string'''
a=input("Enter Something:")
print(type(a))
print(a)

a=int(a)
print(type(a)) #conversion of str to int(if possible as possible only when str has some nos)
print(a)