my_list = [1, 2, 3, 4, 5]
print(f"Original List:\n{my_list}")
del(my_list[-1])
print(f"After removing last element by del:\n{my_list}")
my_list.remove(4)
print(f"After remving last element by remove:\n{my_list}")
