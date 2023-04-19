# This script goes out to the Missouri AG's transgender center concern website and automatically fills the form with garbage data. 

import requests
import random
import string
import urllib.request
import re

# URL of the webpage
url = 'https://ago.mo.gov/file-a-complaint/transgender-center-concerns'

# Generate random text of given length
def generate_random_text(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def generate_random_address():
    # List of common street names
    street_names = ["Main St", "Oak St", "Maple Ave", "Cedar Ln", "Pine St", "Elm St", "Spruce Dr", "Birch Rd", "Willow Ct", "Juniper Way", "Holly St", "Sycamore Rd", "Ash Dr", "Cypress Ln", "Poplar Ave", "Chestnut St", "Dogwood Rd", "Redwood Dr", "Magnolia Ln", "Beech St", "Fir Rd", "Cherry Ave", "Hickory Ln", "Palm Dr", "Locust St", "Birchwood Rd", "Yew Ct", "Cedarwood Ave", "Acacia Ln", "Balsam St", "Alder Rd", "Red Cedar Dr", "Buckeye Ave", "Pecan Ln", "Bamboo Rd", "Boxwood St", "Redbud Ave", "Hemlock Ln", "Cottonwood Dr", "Eucalyptus Ave", "Ginkgo Rd", "Linden St", "Weeping Willow Ln", "Red Maple Ave", "Sweetgum Dr", "White Oak Rd", "Silver Birch Ln", "Sugar Maple Ave", "Yellowwood St", "American Elm Dr"]

    # Generate a random number between 2 and 6 digits for the street number
    street_number = random.randint(10, 999999)

    # Choose a random street name from the list
    street_name = random.choice(street_names)

    # Generate the street address string
    street_address = f"{street_number} {street_name}"

    return street_address
 
# Function that randomly generates a letter to send
def random_paragraph():
    file_path = 'comments.txt'  
    with open(file_path, 'r') as file:
        sentences = file.readlines()
        num_sentences = random.randint(3, 5)  # Randomly select number of sentences
        selected_sentences = random.sample(sentences, num_sentences)  # Randomly select sentences
        paragraph = ' '.join(selected_sentences).strip()  # Join sentences into a paragraph
        
        return paragraph

# Function to generate a fake email address
def generate_fake_email(first_name, last_name):
    # Generate a random string of 5 digits for the email address
    random_digits = ''.join(random.choices(string.digits, k=5))

    # Create the fake email address using the first name, last name, and random digits
    email = f"{first_name.lower()}.{last_name.lower()}{random_digits}@gmail.com"

    return email

# 25 most popular names in the US
first_names = [
'Liam', 'Emma', 'Noah', 'Olivia', 'Isabella', 'Sophia', 'Jackson', 'Lucas', 'Luna', 'Mia', 'Harper', 'Layla', 'Chloe', 'Penelope', 'Riley', 'Zoe', 'Oliver', 'Ava', 'Charlotte', 'Leah', 'Grace', 'Evelyn', 'Aria', 'Scarlett'
]

# 50 popular last names in America
last_names = [
'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Hernandez', 'Martinez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores', 'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell', 'Carter', 'Roberts'
]

# 20 most populous cities in Missouri
mo_cities = [
'Kansas City', 'St. Louis', 'Springfield', 'Independence', 'Columbia', 'Lee\'s Summit', 'O\'Fallon', 'St. Joseph', 'St. Charles', 'Blue Springs', 'St. Peters', 'Florissant', 'Joplin', 'Chesterfield', 'Jefferson City', 'Wentzville', 'Cape Girardeau', 'Wildwood', 'University City', 'Liberty', 'Ballwin', 'Raytown', 'Gladstone', 'Kirkwood', 'Maryland Heights', 'Hazelwood', 'Grandview', 'Webster Groves', 'Belton', 'Nixa', 'Arnold', 'Sedalia', 'Rolla', 'Warrensburg', 'Mexico', 'Moberly', 'Neosho', 'Ferguson', 'Creve Coeur', 'Clayton', 'Republic', 'Lake St. Louis', 'Ozark', 'Manchester', 'Kirksville', 'Hannibal', 'Poplar Bluff', 'Overland', 'Sikeston'
]

# Missouri ZIP codes
mo_zip_codes = [
    63011, 63129, 64118, 63376, 63021, 63031, 63123, 63304, 63033, 64119, 
    63042, 63136, 63034, 63043, 63122, 63044, 63128, 63126, 63045, 63127, 
    63125, 63049, 63051, 63124, 63131
]

# Store randomly generated first name and last name in variables
first_name = random.choice(first_names)
last_name = random.choice(last_names)

# Data to be submitted in the form
data = {
    'FirstName': first_name,
    'LastName': last_name,
    'Address': generate_random_address(),
    'City': random.choice(mo_cities),
    'State': 'MO',
    'ZipCode': random.choice(mo_zip_codes),
    'Email': generate_fake_email(first_name, last_name),
    'Comments': random_paragraph()
}

# Send a POST request to submit the form
response = requests.post(url, data=data)

# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    print("Form submitted successfully!")
else:
    print("Form submission failed.")

