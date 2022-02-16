import re

txt = "The rain in Spain"


###METACHARACTERS###
# []	A set of characters	"[a-m]"
# \	Signals a special sequence (can also be used to escape special characters)	"\d"
# .	Any character (except newline character)	"he..o"
# ^	Starts with	"^hello"
# $	Ends with	"planet$"
# *	Zero or more occurrences	"he.*o"
# +	One or more occurrences	"he.+o"
# ?	Zero or one occurrences	"he.?o"
# {}	Exactly the specified number of occurrences	"he{2}o"
# |	Either or	"falls|stays"
# ()	Capture and group

###SEQUENCES###
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
# r"ain\b"
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
# r"ain\B"
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
# \D	Returns a match where the string DOES NOT contain digits	"\D"
# \s	Returns a match where the string contains a white space character	"\s"
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

# x = re.findall("ai", txt)
#
# print(x)

#will print out ai 2 times in a list since there is "ai" in rain and spain

# y = re.findall("Portugal", txt)
#
# print(y)

#will print an empty list because there is no "Portugal" in this string
#
# x = re.search("\s", txt)
#
# print("The first white space character is located at: ", x.start())

#search will simply look through the string and find what params are required. If true, will return which number char it is through x.start
#searches for the first white space character and returns the starting whitespace character in the string which is represented by
#x.start()
#
# x = re.search("Portugal", txt)
# print(x)

#it will print out "none" since there is no portugal in the string
#
# x = re.split("\s", txt)
# print(x)

#this turns the txt from string to list and splits every time there is a whitespace
#
# x = re.split("\s", txt, 1)
# print(x)

#will only split on the first occurence of the whitespace character
#
# x = re.sub("\s", "9", txt)
# print(x)

#var.sub(param, subsituted, string) will simply subsitute whatever you want with another char of your choice
#In this case, this replaces every whitespace in the string with the number 9
#
# x = re.sub("\s", "9", txt, 2)
# print(x)

#this will replace the first 2 instances of whitespaces with the number 9

#back to the match object
#
# x = re.search("ai", txt)
# print(x) #prints the match object, its span and the match
#
x = re.search(r"\bS\w+", txt)
# print(x.span())
# print(x.string)
print(x.group())
#.span looks for the uppercase S in the string and will print it's start and end position in a tuple
#.string will simply return what the string was passed into the function
#.group will print out what word the parameter is part of if there is a match. In this case, it will print out the word Spain since the capital S is part of it

