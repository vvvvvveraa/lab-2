def display_main_menu():
    print("Welcome to the main menu!")
    print("Enter some numbers separated by commas(e.g. 5,67,32)")

def get_user_input():
    # Prompt the user to enter the minimum and maximum temperatures
    user_input = input("Please enter the values of the temperature: ")
    # Split the input and convert each value to an integer
    num_list = [int(num) for num in user_input.split(",")]
    return num_list

def calc_average(num_list):
    # Calculate the average of the two numbers in the list
    average = sum(num_list) / len(num_list)
    return average

def find_min_max(num_list):
    # Find the minimum and maximum values in the list
    min_temp = min(num_list)
    max_temp = max(num_list)
    # Return the minimum and maximum values as a tuple
    return min_temp, max_temp

def sort_temperature(num_list):
    # Sort the list of float numbers from smallest to largest
    sorted_list = sorted(num_list)
    
    # Return the sorted list
    return sorted_list

def calc_median_temperature(sorted_list):
    # Calculate the length of the list
    length = len(sorted_list)
    
    # Determine whether the length is odd or even
    if length % 2 == 1:
        # If the list length is odd, the median is the middle element
        median = sorted_list[length // 2]
    else:
        # If the list length is even, the median is the average of the two middle elements
        mid_index = length // 2
        median = (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
    
    # Return the median temperature
    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    # Display the main menu
    display_main_menu()
    # Get user input
    num_list = get_user_input()
    print("You entered the list of numbers:", num_list)
    # Calculate the average
    average = calc_average(num_list)
    # Print the average
    print(f"The average weather is {average} degree celsius")
    
    # Call the function to find the min and max temperatures
    min_temp, max_temp = find_min_max(num_list)
    
    # Print the minimum and maximum temperatures
    print(f"The minimum temperature is: {min_temp} degree celsius")
    print(f"The maximum temperature is: {max_temp} degree celsius")
    # Call the function to sort the list of temperatures
    sorted_list = sort_temperature(num_list)
    
    # Print the sorted list of temperatures
    print("The sorted list of temperatures from smallest to largest is:", sorted_list)

    # Call the function to calculate the median temperature
    median_temperature = calc_median_temperature(sorted_list)
    
    # Print the median temperature
    print(f"The median temperature is: {median_temperature} degree celsius")

# Run the main function
if __name__ == "__main__":
    main()

