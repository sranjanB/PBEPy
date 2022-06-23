givenTuple = (1, 2, 2, 3, 4, 4, 4, 5)
print(f"Given Tuple:\n{givenTuple}")
revTuple = tuple(reversed(givenTuple))
print(f"Reversed Tuple:\n{revTuple}")
count = 0
for item in range(len(revTuple)):
    if revTuple[item] == 4:
        count += 1
print(f"4 appears {count} times.")
