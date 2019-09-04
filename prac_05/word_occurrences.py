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
for word in words_dict:
    print("{}:{}".format(word, words_dict[word]))

# add to words_dict check if in dict dict[key] = value
