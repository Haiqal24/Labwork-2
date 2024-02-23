"""
    Program Purpose: To ask user to input data and calculate the surface area based on the given formula
    and types of shapes (cube, sphere & cylinder).
    Programmer: Haiqal
    Date: 2 February 2024
"""

# Function to calculate the total cost of the reservation
def calculate_cost(room_type, num_rooms, num_nights):
    # Dictionary containing room rates for different room types
    room_rates = {
        "Single": 100,
        "Double": 150,
        "Suite": 250
    }
    # Discount threshold for the number of rooms
    discount_threshold = 5
    # Discount rate for eligible reservations
    discount_rate = 0.1
    # Minimum number of nights required for a Suite reservation
    min_suite_nights = 3
    # Number of nights required for a complimentary breakfast voucher for Single room
    complimentary_breakfast_nights = 7

    # Check if the provided room type is valid
    if room_type not in room_rates:
        print("Invalid room type.")
        return None

    # Check if the number of rooms or nights entered is less than or equal to 0
    if num_rooms <= 0 or num_nights <= 0:
        print("Please enter at least 1 night or 1 room.")
        return None

    # Get the room rate for the selected room type
    room_rate = room_rates[room_type]
    # Calculate the total cost of the reservation
    total_cost = room_rate * num_nights * num_rooms

    # Apply discount if the number of rooms exceeds the discount threshold
    if num_rooms > discount_threshold:
        total_cost *= (1 - discount_rate)
        print("You are eligible for a 10% discount on the total cost!")

    # Check if the selected room type is a Suite and the number of nights is less than the minimum required
    if room_type == "Suite" and num_nights < min_suite_nights:
        print("Minimum stay for a Suite is 3 nights.")
        return None

    # Check if the selected room type is Single and the number of nights exceeds the complimentary breakfast threshold
    if room_type == "Single" and num_nights > complimentary_breakfast_nights:
        print("You get a complimentary breakfast voucher!")

    return total_cost

# Welcome message and room types information
print()
print(f"Welcome to Hotel Transylvania!")
print()
print("Your Number 1 Hotel choice in Malaysia!")
print("Room Types:")
print("1. Single (RM100 per night)")
print("2. Double (RM150 per night)")
print("3. Suite (RM250 per night)")

# Prompt the user to select a room type
room_type = input("Enter room type (1 , 2 , 3 ): ")
room_types = {1: "Single", 2: "Double", 3: "Suite"}
while room_type not in ["1", "2", "3"]:
    print("Invalid room type. Please enter 1, 2, or 3.")
    room_type = input("Enter room type (1 for Single, 2 for Double, 3 for Suite): ")

room_type = room_types[int(room_type)]

# Prompt the user to enter the number of rooms and nights
num_rooms = int(input("Enter number of rooms: "))
num_nights = int(input("Enter number of nights: "))

# Calculate the total cost of the reservation
total_cost = calculate_cost(room_type, num_rooms, num_nights)
if total_cost is not None:
    print(f"Total cost of reservation: RM{total_cost:.2f}")
