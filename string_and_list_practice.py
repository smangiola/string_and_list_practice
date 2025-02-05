#Strings
#A. Donuts
def donuts(count):
    if count <= 9: #if the number of donuts is 9 or less
        return count #the number given is returned
    elif count >= 10: #if the number of donuts is 10 or more
        return 'Many' #'Many' is returned instead of the number

print("Number of donuts:", donuts(5))
print("Number of donuts:", donuts(23))

#B. both_ends
def both_ends(s):
    if len(s) >= 2: #if the string length is 2 or more
        return s[0:2]+s[-2:] #returns a string made of the first two and last two characters of the original string
        #s[0:2] = the first two, s[-2:] = the last two
    elif len(s) < 2: #returns the empty string if the length is less than 2
        return None

print(both_ends("spring"))
print(both_ends("hello"))
print(both_ends("h"))

#C. fix_start
def fix_start(s):
    first_character = s[0]
    other_characters = s[1:] #the characters other than the first one are given their own value
                             #so the first character doesn't change
    replaced_characters = other_characters.replace(first_character, '*') #replaces the other characters with '*'
    return first_character + replaced_characters
    
print(fix_start("babble"))
print(fix_start("sassy"))


#Lists
#A. match_ends
def match_ends(words):
    count = 0
    for i in words:
        if len(i) >= 2 and i[0] == i[-1]: #checks if each string's length is 2 or more
                                          #and if its first and last characters are the same
            count += 1 #adds to the count if the previous conditions are true
    return count

print(match_ends(['aka', 'lol', 'banana', 'l']))

#B. front_x
def front_x(words):
    words_1 = [] #the list containing the strings starting with x
    words_2 = [] #the list containing the strings that don't start with x
    for i in words:
        if i.startswith('x'): #checks if any of the strings in words start with x
            words_1.append(i) #if they do, they are added to words_1
        else:
            words_2.append(i) #if they do not start with x, they are added to words_2
    return sorted(words_1) + sorted(words_2) #returns a list that combines the sorted versions of words_1 and words_2

print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))

#C. sort_last
def last(i): #function that extracts the second element in each tuple 
    return i[-1] #-1 is the position of the second element

def sort_last(tuples):
    return sorted(tuples, key=last) #sorted returns the list with its elements in order, also calls the last function
                                    #so it is ordered by the last element in each tuple

print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))
    