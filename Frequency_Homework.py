my_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20, 'f': 10}
value_to_check = 10
frequency = list(my_dict.values()).count(value_to_check)
print(f"The value {value_to_check} appears {frequency} times in the dictionary.")
