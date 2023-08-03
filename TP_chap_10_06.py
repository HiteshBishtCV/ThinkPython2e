def is_anagram(str1,str2):

    return set(list(str1))==set(list(str2))

str1= 'abcdefghijkl'
str2= 'abcdefglkjih'

print(is_anagram(str1,str2))


str1= 'abcdefghijkl'
str2= 'abcdefglkjh'
print(is_anagram(str1,str2))