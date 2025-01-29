def find_largst_and_smallest(arr):
    if not arr:
     return none, none #return none if the array is empty
    largest =arr[0]
    smallest =arr[0]
    for num in arr:
        if num>largest:
            largest=num 
        if num<smallest:
            smallest=num
                
    return largest,smallest
               # example usage:
array =[10,89,9,56,4,80,8]
largest,smallest=find_largst_and_smallest(array)
print("largest element:",largest)
print("smallest element:",smallest)
 