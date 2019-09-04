# text = input("Text: ")
text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
words_dict = {}
for word in words:
    if word not in words_dict.keys():
        words_dict[word] = 1
    else:
        number = words_dict[word]
        number += 1
        words_dict[word] = number

words = list(words_dict.keys())
words.sort()

length_of_longest_word = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, length_of_longest_word, words_dict[word]))
