good_chars = "аоуэыеяюиё"
word = input()
start_word = ''.join(["1" if i in good_chars else "0" for i in word])
start_word = start_word[:start_word.rfind("1")+1]
num_of_words = int(input())
words = [input() for _ in range(num_of_words)]
for i in words:
    final_i = ''.join(["1" if j in good_chars else "0" for j in i])
    final_i = final_i[:final_i.rfind("1")+1]
    if start_word == final_i:
        print(i)
