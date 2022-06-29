# Task 1
# Create a function that takes an array of numbers as a parameter and returns the number of
# values that are a multiplier of either 4 or 6 (or, of course, both).

# To understand whether it is a multipler for the number 4 and 6,
# we need to divide our number by 4 or 6, and if we get an integer, then
# #4 or 6, respectively, will be multipler

print('Enter a array of numbers')
a = [int (i) for i in input().split()]
k = 0
for item in a:
    if item % 4  == 0 or item % 6 == 0:
# if we need to comply with the condition that both 6 and 4 are factors,
# then we need to replace or with and
        k += 1
print (k)

#Write a function that tests if a string is a palindrome.

def polindrome(s):
    print('enter a word or number')
    s = input()
    return s == s[::-1] # an easy way to check is to reverse the string and compare it with the original

print(polindrome('level'))

# but when we have entered something with spaces for example "Was it a cat I saw"?
# we need to replace spaces with empty characters and make all letters the same case

def polindrome1(s):
    print('enter a phrase')
    s = input()
    s = s.lower()  # make all letters the same case
    s = s.replace(' ', '') #replace spaces with empty characters
    s = s.replace('?', '')
    return s == s[::-1]  # compare it with the original

print(polindrome1('Was it a cat I saw?'))


