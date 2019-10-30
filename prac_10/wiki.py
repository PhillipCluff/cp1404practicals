import wikipedia

search_item = input("please enter a search item: ")
while search_item != "":
    try:
        print(wikipedia.summary(search_item))
    except wikipedia.exceptions.DisambiguationError as e:
        for item in e.options[:5]:
            print(item, end=", ")

    print("---Cool stuff----")
    search_item = input("please enter a search item: ")