num = int(input("Enter a number: "))

odd_numbers = [i for i in range(1, num + 1) if i % 2 != 0]

fruits = ["apple", "banana", "cherry", "mango", "orange"]

updated_fruits = [fruit.capitalize() for fruit in fruits]

print("\nList of odd numbers:", odd_numbers)
print("Original fruits list:", fruits)
print("Updated fruits list:", updated_fruits)
