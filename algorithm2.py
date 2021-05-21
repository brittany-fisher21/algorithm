def bubble_sort(nums):
    
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                
                swapped = True
    return nums


random_list_of_nums = [3, 1, 4, 2,] 

print(bubble_sort(random_list_of_nums))
print(random_list_of_nums)

#worked
            
