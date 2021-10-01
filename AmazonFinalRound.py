


def find_words(words: list, key: str)->list:
    output_list = []
    
    words = sorted(words)
    
    for word in words:
        if key in word:
            output_list.append(word)

    return output_list


words = ["angel", "artistic", "although", "brain", "bully", "baracuda", "bar", "barcode", "climb"]

key = "bar"

print(find_words(words, key ))
