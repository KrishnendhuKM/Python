def is_anagram(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    return sorted(word1) == sorted(word2)
word1 = input("enter word 1:")
word2 = input("enter word 2:")

if is_anagram(word1, word2):

    print("anagram")
else:
    print("not anagram")   
