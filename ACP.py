numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares) 

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  

list_of_lists = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in list_of_lists for item in sublist]
print(flat_list) 

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_data = [x for x in data if x > 5 and x % 2 != 0]
print(filtered_data) 