# JTSK-350111
# a6 p8.py
# Dushan Terzikj
# d.terzikj@jacobs-university.de

my_dict = {
    "merry":"god", 
    "christmas":"jul", 
    "and":"och", 
    "happy":"gott",
    "new":"nytt", 
    "year":"\u00E5r"
}

def translate(list_en):

    """ This function translates list of words from english to swedish using 
    dictionary my_dict """

    ret = []
    for word in list_en:
        word = word.lower()
        exists = my_dict.get(word, None)
        if exists == None:
            # if the word does not exists in the dictionary
            # then append the english word
            ret.append(word)
        else:
            ret.append(my_dict[word])
    return " ".join(ret)

# the code below is used for testing
string = input("Enter a string to be translated:\n")
print(translate(string.split()))