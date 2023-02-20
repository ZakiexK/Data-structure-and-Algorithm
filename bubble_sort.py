def bubblesort (arr):
    n = len(arr)

    for i in range(n):
        for j in range(0 , n-i-1):
            if(arr[j] > arr[j + 1]):
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j]

if __name__ == "__main__":

    arr = [0, 9, 3, 4, 5, 6, 1 ,7 ,8, 2]

bubblesort(arr)

print(arr)
