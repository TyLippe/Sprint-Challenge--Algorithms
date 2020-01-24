'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):
    #base case
    if len(word) == 0 or len(word) == 1:
        return count
    #check first and second character of the word given, if 'th' then add 1 and remove the 'th'
    elif word[0:2] == 'th':
        count += 1
        newWord = word[2:]
        return count_th(newWord, count)
    #if not 'th' then remove the first letter and send the new word
    else:
        newWord = word[1:]
        return count_th(newWord, count)

#removing the return on 14 and 18 makes the function run backwards. 