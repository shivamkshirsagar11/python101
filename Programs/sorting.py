class Array:
    def __init__(self, arr) -> None:
        self.arr = arr
        self.n = len(arr)
        self.before = arr.copy()

    def selection_sort(self)->None:
        for i in range(self.n):
            mini = i
            for j in range(i + 1, self.n):
                if self.arr[mini] > self.arr[j]:
                    mini = j
            self.arr[mini], self.arr[i] = self.arr[i], self.arr[mini]
    def bubble_sort(self)->None:
        for i in range(self.n):
            for j in range(self.n - i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
    def quick_sort(self)->None:
        def part(arr, low, high):
            if low < high:
                pivot = arr[high]
                i = low - 1
                for j in range(low, high):
                    if arr[j] < pivot:
                        i += 1
                        arr[i], arr[j] = arr[j], arr[i]
                i += 1
                arr[i], arr[high] = arr[high], arr[i]
                return i
        def quicksort(arr, low, high):
            if low < high:
                pivot = part(arr, low, high)
                quicksort(arr, low, pivot-1)
                quicksort(arr, pivot+1, high)
        quicksort(self.arr, 0, self.n-1)
    
    def merge_sort(self)->None:
        def helper(arr):
            if len(arr) > 1:
                middle = len(arr) // 2
                L, R = arr[:middle], arr[middle:]
                helper(L)
                helper(R)
                i, j, k = 0, 0, 0

                while i < len(L) and j < len(R):
                    if L[i] <= R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1
                
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1
                
                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1
        helper(self.arr)
    
    def __str__(self)->str:
        return "Before: "+self.before.__str__()+" After sorting: "+self.arr.__str__()


def main():
    inp = input("Enter array elements: ")
    arr = []
    inp = inp.split(" ")
    for i in inp:
        arr.append(int(i))
    arrObj = Array(arr)
    # arrObj.selection_sort()
    # arrObj.bubble_sort()
    # arrObj.quick_sort()
    arrObj.merge_sort()
    print(arrObj)

if __name__ == "__main__":
    main()