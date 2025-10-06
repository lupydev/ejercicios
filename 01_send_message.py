""" "
For day three of Space Week, you are given an array of numbers representing distances (in kilometers) between yourself, satellites, and your home planet in a communication route. Determine how long it will take a message sent through the route to reach its destination planet using the following constraints:
• The first value in the array is the distance from your location to the first satellite.
• Each subsequent value, except for the last, is the distance to the next satellite.
• The last value in the array is the distance from the previous satellite to your home planet.
• The message travels at 300,000 km/s.
• Each satellite the message passes through adds a 0.5 second transmission delay.
• Return a number rounded to 4 decimal places, with trailing zeros removed.
"""


def send_message(route: list) -> float:
    message_speed = 300000  # km/s
    transmission_delay_per_satellite = 0.5  # seconds

    total_distance = sum(route)
    travel_time = total_distance / message_speed
    total_time = travel_time + (transmission_delay_per_satellite * (len(route) - 1))

    return round(total_time, 4)


print(send_message([1000000, 2000000, 3000000]))  # ➞ 21.0
print(send_message([500000, 1000000, 2000000, 3000000]))  # ➞ 23.1667
