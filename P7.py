# 20CE118 KHUSHI RANPARIYA
# AIM
# Lapindrome is defined as a string which when split in the middle,
# gives two halves having the same characters and same frequency of each character.
# If there are odd number of characters in the string, we ignore the middle character
# and check for lapindrome. For example gaga is a lapindrome, since the two halves
# ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy
# are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves
# contain the same characters but their frequencies do not match. Your task is simple.
# Given a string, you need to tell if it is a lapindrome.
# REPOSITORY LINK:
# https://github.com/KhushiRanpariya/PIP_Practicals

#input the number of words.
N = int(input())
# input the word
for i in range(N):
    word = input()
    #divding the word into 2 parts a and b by length (even and odd)
    l = len(word)
    if l % 2 == 0:
        a = word[:l//2]
        b = word[l//2:]
    else:
        a = word[:l//2]
        b = word[l//2+1:]
    # printing the result if or not the word is a lapindrome
    if sorted(a) == sorted(b):
        print("YES")
    else:
        print("NO")
