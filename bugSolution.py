def calculate_average(numbers):
    if not numbers:
        return None  # Or raise an exception: raise ValueError("Input list cannot be empty")
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}") #Prints None. A more descriptive message can be added here.