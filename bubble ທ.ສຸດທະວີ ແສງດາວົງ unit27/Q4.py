def is_anagram(word1, word2):
    word1 = word1.lower().replace(" ", "").strip('!,.?')
    word2 = word2.lower().replace(" ", "").strip('!,.?')
    if len(word1) != len(word2):
        return False
    list1 = list(word1)
    list2 = list(word2)
    list1.sort()
    list2.sort()
    return list1 == list2

print(is_anagram("listen", "silent"))
print(is_anagram ("anagram", "nagaram")) 
print(is_anagram ("listen", "silence"))
print(is_anagram ("anagram", "anagrams"))