# Elsie Ward and Anastacia Aguirre

#Part B: Looping over strings
def Os(word):
    total_o= 0
    for letter in word:
        if letter=="o":
            total_o= total_o + 1
    return total_o

print(Os("bonobos"))
print(Os("loose"))


#Indexing
"abc"[0]
#'a'
"waffles"[1]
#'a'
dinner="falafels"
dinner[4]
#'f'
[1, 2, 3, 4][0]
#1
"frog"[-1]
#'g'

#A negative index backwards from character 0
#If you don't know the length of a string but you know you want one of the last few characters"




