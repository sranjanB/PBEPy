my_list = [1, 2, 3, 4]

try:
    assert len(my_list) >= 5, "List length is less than 5."
except AssertionError as e:
    print(f"error details:\n{e}")