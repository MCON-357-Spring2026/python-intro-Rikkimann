"""
TODO:
Create and unpack a tuple
Create a tuple named 'coordinates' that contains three values: latitude, longitude, and altitude.
Unpack the tuple into three separate variables: lat, lon, and alt.
Create a tuple with mixed data types
Create a tuple named 'person_info' that contains a string (name), an integer (age), and a float (height).
Unpack the tuple into three separate variables: name, age, and height.
Demonstrate tuple immutability
Create a tuple named 'immutable_tuple' with three integer values.
Attempt to change the first element of the tuple to a different value and handle the exception that arises
"""

"""
Create and unpack a tuple
"""
letters = ("A","B")
x, y = letters

"""
Create a tuple named 'coordinates' that contains three values: latitude, longitude, and altitude.
"""
coordinates = ("latitude", "longitude", "altitude")

"""
Unpack the tuple into three separate variables: lat, lon, and alt
"""
lat, lon,  alt= coordinates

"""
Create a tuple with mixed data types
"""
person = ("Alice", 30, 5.5)

"""
Create a tuple named 'person_info' that contains a string (name), an integer (age), and a float (height).
"""
person_info=("Rikki", 20, 5.6)

"""
Unpack the tuple into three separate variables: name, age, and height.
"""
name, age,  height=person_info

"""
Create a tuple named 'immutable_tuple' with three integer values.
"""
immutable_tuple=(20, 21, 22)

"""
Attempt to change the first element of the tuple to a different value and handle the exception that arises
"""
try:
    immutable_tuple[0] = 10
except TypeError as e:
    print(f"Error: {e}")
