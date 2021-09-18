 
def find_lower_upper(a: list) -> list:
    """Find lower and upper splis for lists"""
    lower = []
    upper = []
    # If even, take halves
    if len(a)%2 == 0:
        middle = len(a)//2
        lower = a[0:middle]
        upper = a[middle+1:-1]
    # Lower splits should be inclusive of middle numbers and upper lists should not
    else:
        middle = len(a)//2+1 
        lower = a[0:middle]
        upper = a[middle+1:-1]

    return [lower, upper]

def find_median(a: list) -> int:
    """Find median"""
    median = 0
    if len(a)%2 == 0:
        middle = len(a)//2
        median = (a[middle-1]+a[middle])/2
    else:
        median = a[len(a)//2]
    return median
    
def find_median_double(a: list, b:list) -> float:
    """Find median of two sorted lists"""
    median_a = 0
    median_b = 0

    if len(a) == 0 and len(b) == 0:
        return
    elif len(a) == 0:
        return find_median(b)
    elif len(b) == 0:
        return find_median(a)   
    elif len(a) or len(b) <= 2:
        new_list = a + b
        return find_median(new_list)
    else:
        lower_a, upper_a = find_lower_upper(a)
        lower_b, upper_b = find_lower_upper(b)

        median_a = find_median(a)
        median_b = find_median(b)

        if median_a > median_b:
            new_a = lower_a
            new_b = upper_b
        else:
            new_a = upper_a
            new_b = lower_b

        find_median_double(new_a, new_b)


if __name__ == "__main__":

    list1 = [1]
    list2 = [2, 3, 4, 5, 6, 7]
    list3 = [7, 8, 12, 67, 89]
    list4 = [1, 2]
    list5 = [3, 4]

    print(find_median_double(list1, list2))
    print(find_median_double(list2, list3))
    print(find_median_double(list4, list5))

