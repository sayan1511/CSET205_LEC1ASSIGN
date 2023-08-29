def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def get_input():
    input_str = input("Enter a list of numbers separated by spaces: ")
    input_list = [int(x) for x in input_str.split()]
    return input_list

def main():
    input_list = get_input()
    bubble_sort(input_list)
    print("Sorted list:", input_list)

if __name__ == "__main__":
    main()
