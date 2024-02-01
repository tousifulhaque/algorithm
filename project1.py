import random 
class InsertionSort():
    def __init__(self,num_list:int, num_list_ele: list ) -> None:
        assert len(num_list_ele) == num_list, "Missing Input for array elements"
        self.num_list_ele = num_list_ele
        self.num_list = num_list
        self.list_of_list = [[random.randint(0, 100) for j in range(self.num_list_ele[i])] for  i in range(self.num_list)]
        self.timing = []
        self.sorted = []

    def sort(self, array: list) -> list:
        count = 0
        n = len(array) 
        count +=1
        for i in range(1, n):
            count +=1
            key = array[i]
            count +=1
            j = i - 1
            count +=1 
            while j >= 0 and array[j] > key :
                count +=1 
                array[j+1] = array[j]
                count +=1
                j = j - 1
                count += 1
            array[j+1] = key
            count +=1
        self.timing.append(count)
        return array 

    def sort_all(self):
        for arr in self.list_of_list:
            print('Unsorted list \n {}'.format(arr)) 
            sorted_arr = self.sort(arr)
            print('Sorted list \n {}'.format(sorted_arr))
            self.sorted.append(sorted_arr)




if __name__ == "__main__":
    insort = InsertionSort(10, [5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
    insort.sort_all()