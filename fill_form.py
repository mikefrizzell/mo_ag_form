# This script goes out to the Missouri AG's transgender center concern website
# and automatically fills the form with garbage data. 
# Edit 'num_submissions = 500' to change how many times the script runs.

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
    
# Generate random address
def generate_random_address():
    num_digits = random.randint(2, 5)
    num_letters = random.randint(10, 20)
    return str(random.randint(10**(num_digits-1), (10**num_digits)-1)) + ' ' + generate_random_text(num_letters)    

# Function that randomly selects a passage of 1,000 words from Shakespeare
def random_passage():
    # Download the text file
    url = "https://www.gutenberg.org/cache/epub/100/pg100.txt"
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8-sig')

    # Split the text into words
    words = re.findall('\w+', text)

    # Choose a random starting word index
    start_index = random.randint(0, len(words) - 1000)

    # Extract the passage of 1000 words
    passage = ' '.join(words[start_index:start_index+1000])

    return passage

# 25 most popular names in the US
top_25_names = [
'Liam',
'Emma',
'Noah',
'Olivia',
'Isabella',
'Sophia',
'Jackson',
'Lucas',
'Luna',
'Mia',
'Harper',
'Layla',
'Chloe',
'Penelope',
'Riley',
'Zoe',
'Oliver',
'Ava',
'Charlotte',
'Leah',
'Grace',
'Evelyn',
'Aria',
'Scarlett'
]

# 20 most populous cities in Missouri
mo_cities = [
'Kansas City',
'St. Louis',
'Springfield',
'Independence',
'Columbia',
'Lee\'s Summit',
'O\'Fallon',
'St. Joseph',
'St. Charles',
'Blue Springs',
'St. Peters',
'Florissant',
'Joplin',
'Chesterfield',
'Jefferson City',
'Wentzville',
'Cape Girardeau',
'Wildwood',
'University City',
'Liberty',
'Ballwin',
'Raytown',
'Gladstone',
'Kirkwood',
'Maryland Heights',
'Hazelwood',
'Grandview',
'Webster Groves',
'Belton',
'Nixa',
'Arnold',
'Sedalia',
'Rolla',
'Warrensburg',
'Mexico',
'Moberly',
'Neosho',
'Ferguson',
'Creve Coeur',
'Clayton',
'Republic',
'Lake St. Louis',
'Ozark',
'Manchester',
'Kirksville',
'Hannibal',
'Poplar Bluff',
'Overland',
'Sikeston'
]

# Missouri ZIP codes
mo_zip_codes = [
    63011, 63129, 64118, 63376, 63021, 63031, 63123, 63304, 63033, 64119, 
    63042, 63136, 63034, 63043, 63122, 63044, 63128, 63126, 63045, 63127, 
    63125, 63049, 63051, 63124, 63131
]


# Data to be submitted in the form
data = {
    'FirstName': random.choice(top_25_names),
    'LastName': generate_random_text(5),
    'Address': generate_random_address(),
    'City': random.choice(mo_cities),
    'State': 'MO',
    'ZipCode': random.choice(mo_zip_codes),
    'Email': generate_random_text(7) + '@gmail.com',
    'Comments': random_passage()
}

# Set the number of form submissions
num_submissions = 500  

# Loop for the specified number of form submissions
for i in range(num_submissions):
    # Send a POST request to submit the form
    response = requests.post(url, data=data)

    # Check if the request was successful (status code 200 indicates success)
    if response.status_code == 200:
        print(f"Form submitted successfully! Submission {i+1}/{num_submissions}")
    else:
        print(f"Form submission failed for submission {i+1}/{num_submissions}")
