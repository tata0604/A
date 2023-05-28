#Selection Sort
def selection_sort(arr):
      for i in range(len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                  if arr[j] < arr[min_index]:
                        min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
      return arr

#a1=[20,10,5,7,9,13]

def main():
    Number = int(input("How many numbers you want to add in array : "))

    print("Insert your elements : ")
    array = []

    for p in range(Number):
        No = int(input())
        array.append(No)

    print()
    print("your array : ",array)

    A = selection_sort(array)

    print("Selection sort : ",A)

if __name__ == "__main__":
    main()
