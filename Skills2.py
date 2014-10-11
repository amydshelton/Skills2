string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
f = open("twain.txt")
twainstring = f.read()

def count_unique(string1):
    word_list = string1.split()
    word_dict = {}
    for word in word_list:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict
#print count_unique(twainstring)

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
    a = set(list1)
    b = set(list2)
    common_list = list(a.intersection(b))
    return common_list

#print common_items(list1,list2)

"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
    common_list = []
    list1_dict = {}
    for item in list1:
        list1_dict[item] = 1

    for item in list2:
        if list1_dict.setdefault(item,2) == 1:
            common_list.append(item)
    return common_list

#print common_items2(list1, list2)

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
    newlist = [number*-1 for number in list1]
    return newlist

#print sum_zero(list1)

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    return list(set(words))

#print find_duplicates(words)

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""



def word_length(words):
    word_dict = {}
    # my_key = word_dict.get
    for item in words:
        word_dict[item] = len(item)

    word_dict = word_dict.items()

    word_dict_into_reverse_tuple = []
    for i in range(len(word_dict)):
        word = word_dict[i][0]
        count = word_dict[i][1]
        word_dict_into_reverse_tuple.append((count, word))

    sorted_word_dict = sorted(word_dict_into_reverse_tuple)

    for i in range(len(sorted_word_dict)):
        print sorted_word_dict[i][1], sorted_word_dict[i][0]

twainlist = twainstring.split()

#word_length(twainlist)


"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""

def eng_to_piraat():
    eng_to_piraat_dict = {
    "sir" : "matey",
    "hotel" : "fleabag inn",
    "student" : "swabbie",
    "boy" : "matey",
    "madam" : "proud beauty",
    "professor" : "foul blaggart",
    "restaurant" : "galley",
    "your" : "yer",
    "excuse" : "arr",
    "students" : "swabbies",
    "are" : "be",
    "lawyer" : "foul blaggart",
    "the" : "th'",
    "restroom" : "head",
    "my" : "me",
    "hello" : "avast",
    "is" : "be",
    "man" : "matey",
    "Sir" : "Matey",
    "Hotel" : "Fleabag inn",
    "Student" : "Swabbie",
    "Boy" : "Matey",
    "Madam" : "Proud beauty",
    "Professor" : "Foul blaggart",
    "Restaurant" : "Galley",
    "Your" : "Yer",
    "Excuse" : "Arr",
    "Students" : "Swabbies",
    "Are" : "Be",
    "Lawyer" : "Foul blaggart",
    "The" : "Th'",
    "Restroom" : "Head",
    "My" : "Me",
    "Hello" : "Avast",
    "Is" : "Be",
    "Man" : "Matey"
    }
    sentence = raw_input("What sentence do you want translated?  ")
    words = sentence.split()
    translation = []
    for word in words:
        if eng_to_piraat_dict.get(word, "woooo") == "woooo":
            translation.append(word)
        else:
            translation.append(eng_to_piraat_dict[word])

    string_translation = " ".join(translation)

    print string_translation

eng_to_piraat()