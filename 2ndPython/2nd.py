# myStringOne = 'single Quote'
# myStringTwo = "Double Quote"
# myStringThree = "Mix Quotes 'Double for variable declarrtion and single inside'"
# print(myStringOne)
# print(myStringTwo)
# print(myStringThree)
# myStringFive = '''The message will be printed as it
# and It will ignore the "" ''
# Also I can add new lines with it.
# and It will also print \\\ '''
# print(myStringFive)
## built-in method##
# myString = "     Test Strip Function 1st       "
# print(myString.strip())
# print(myString.lstrip())
# print(myString.rstrip())
# myStringHash = "@#@#@#@#Test Strip Function@#@#@#@#"
# print(myStringHash.strip('@#'))
# print(myStringHash.lstrip('@#'))
# print(myStringHash.rstrip('@#'))
# print(myString.title())
# print(myString.capitalize())
# a, b, c, d = "1", "11", "111", "1111"
# print(a.zfill(4))
# print(b.zfill(4))
# print(c.zfill(4))
# print(d.zfill(4))

# endswith, startswith, swapcase, center, count, rsplit, split

# tSplit = "Split-the-string-by-removing-sadh-seperator"
# print(tSplit.split('-', 3))       #split using - only the first 3 dashes
# print(tSplit.rsplit('-', 3))      #split using - only the last 3 dashes
# tCenter = "Center Islam"
# print(tCenter.center(26, "!"))    #center banner from 26 characters by using !
# tCount = "Count-the-string-by-removing-dash-seperator"
# print(tCount.count('t', 11, 29))        #find t in the string from 11 upto 29
# print(tCount.count('t'))                #find t in the string
# tSwapSpace = "sWAPsPACE-tHE-sTRING-BY-rEMOVING-dASH-sEPERATOR"
# print(tSwapSpace.swapcase())            #CHANGE FROM UPPER-CASE TO LOWER-CASE AND FROM LOWER-CASE TO UPPER-CASE
# tStart = "cutting the text by its Start"
# print(tStart.startswith('t', 2, 10))        #Does string start with in the 2nd index?
# tEnd = "cutting the text by its End"
# print(tEnd.endswith('d'))
# print(tEnd.endswith('h', 2, 10))
# print(tEnd.endswith('H', 2, 10))  # Does string end with in the 2nd index?
# print(tEnd[10])

# index, find, rjust, ljust, splitlines, expandtabs, istitle, isspace, islower, isidentifier, isalpha, isalnum

# tIndex = "Detect the index of the string"
# print(tIndex.index('tr', 0, 27))
# print(tIndex.index('tr', 0, 24))
# print(tIndex.index('tr'))

# tFind = "Detect the index of the string"
# print(tFind.find('tr', 0, 27))
# print(tFind.find('tr', 0, 24))
# print(tFind.find('tr'))

# trJust = "Detect the index of the string"
# print(trJust.rjust(40, '%'))

# tlJust = "Detect the index of the string"
# print(tlJust.ljust(40, '%'))

# tsplitLines = "Detect\nthe\nindex\nof\nthe\nstring"
# print(tsplitLines)

# tsplitLines = "Detect\tthe\tindex\tof\tthe\tstring"
# print(tsplitLines)

# tistitle = "string method to check About If all the letters are UPPER-case"
# print(tistitle.istitle())

# tislower = "string method to check about if all the letters are lower-case"
# print(tislower.islower())

# tisspace = " "
# print(tisspace.isspace())

# tisidentifier = "!string--method"
# print(tisidentifier.isidentifier())

# tisidentifier = "stringMethod"
# print(tisidentifier.isidentifier())

# tisalpha = "string method to check 9about if they are all letters"
# print(tisalpha.isalpha())

# tisalpha = "stringAllLetters"
# print(tisalpha.isalpha())

# tisalnum = "stringAndNumeric#"
# print(tisalnum.isalnum())

# tisalnum = "stringAndNumeric5"
# print(tisalnum.isalnum())

# replace, join

# treplcae = "Numbers in order are one, two, one, three, four, five, six, seven"
# print(treplcae.replace('one', '1'))
# print(treplcae.replace('one', '1', 1))

# tJoin = ['Islam', 'Gamal', 'Muhammed', 'Eltally']
# print("-".join(tJoin))

#
