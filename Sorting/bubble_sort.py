"""Count the number of swaps to get the list in order."""

def countSwaps(a):
    swaps = 0
    for i in range(0, len(a)):
        for j in range(0, len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

if __name__ == '__main__':
    
    a = [4, 2, 3, 1]

    countSwaps(a)
