s = "this is a string"
a : str = "Specifically defined string"
print(s)
print(a)
print(type(s))

multiline = """I guess this is a
                multiline comment maybe?"""
print(multiline)
print(s[0]) #First character of s hahah similar to C
print(s[1])
print(s*2) # This is so odd yet interesting!
print(s + " " + s)

print(len(s))

for x in s:
    print(x) # Print every letter in s

print(s[0:5]) # Prints the 0th to the 5th index in string interest...
print(s[0:])
print(s[:8])
x : str = "abcdefghijklmnopqrstuvwxyz"
print(x[0::2]) # Prints every other character
print(x[::2]) # Prints every other character

print(x[-4:-1]) #Interesting, -1 represents last element and it goes backwards

print(x[0:9:2])
print(x[15::-1]) #Step backwards interesting
print(x[::-1]) #Step totally backwards

print(x.replace("a","A"))

print(x)
print(x.strip())

print(x.find("abc"))
print(x.find("def")) # Returns the index at which it found the first character of the string
print(x.find("dff")) # Returns -1 since not found
print(x.find("abc",0,5))
print(x.find("abc",0))
print(x.find("abc",3))

print(x.count("abc")) # Returns the number of tiems abc appears in x