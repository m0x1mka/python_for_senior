def filter_anagrams(anagram, words):
    final_words = []
    for i in words:
        if sorted(list(i)) == sorted(list(anagram)):
            final_words.append(i)
    return final_words


word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))
