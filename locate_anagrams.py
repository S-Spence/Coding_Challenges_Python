


def swap(list, i, j):
    list[i], list[j] = list[j], list[i]
    return list


def find_anagrams(s: str):
    letters = {}
    # fill dictionary with letters and their index values
    for index, val in enumerate(s):

        if val not in letters:
            letters[val] = [index]
        else:
            letters[val].append(index)
            
    # Check if swapping all letters is possible
    half = len(s)/s

    for val in letters.values():
        if len(val) >= half:
            return "IMPOSSIBLE"
            
    extra_letters = []
    # Create a copy of the list
    copy = [i for i in s]
    for i in range(len(copy)-1):
        if copy[-1] != copy[0]:
            copy.append(copy.pop(0))
        else:
            extra_letters.append(copy[i])
            copy.pop(i)

     
        
    if extra_letters:
        for i in range(len(extra_letters)):
            if i not in letters[extra_letters[i]]:
                copy.insert(i, extra_letters[i])
            elif i + 1 not in 
 
    copy = str(copy)

    return copy




if __name__ == "__main__":

    test_one = "start"
    test_two = "jjj"
    test_three = "asrhtma"

    print(find_anagrams(test_one))
    print(find_anagrams(test_two))
    print(find_anagrams(test_three))
