import my_library as ml

def print_details(name, age):
    """
    This function accept arameters name and age.
    """
    print(f"Hello, {name}.\nI guess you are {age} year old !")

print(print_details.__doc__)
print_details("Sonu", 10)
result = ml.make_total_double(20, 30.5)
print(result)

print(ml.my_list)
new_list = list(map(lambda x:x+5, ml.my_list))
print(new_list)
