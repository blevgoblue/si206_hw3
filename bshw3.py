# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

# Import modules
from bs4 import BeautifulSoup
import requests
import re

# BeautifulSoup request for webpage and boilerplate
page = requests.get('http://collemc.people.si.umich.edu/data/bshw3StarterFile.html')
soup = BeautifulSoup(page.text, 'html.parser')

# Find text with "student"
# Use RegEx to find all usages of 'student' and replace with 'AMAZING student'
student_mentions = soup.find_all(text = re.compile('student'))

# Add "AMAZING" to that text
# For each usage:
for usage in student_mentions:
    # Create new string from existing text, and switch 'student' for 'AMAZING student'
    replacement_text = usage.replace('student', 'AMAZING student')
    usage.replace_with(replacement_text)

# Replace photos
# Replace center photo w/ file in 'media' folder
soup.select('#main img')[0]['src'] = 'media/twitter_image.jpg'

# Replace top logo 'src'
soup.find('div', class_='logo').find('img')['src'] = 'media/logo.png'

# Replace footer logo 'src'
soup.find('div', class_='footer-logo').find('img')['src'] = 'media/logo.png'

# Write to file
output = open("part_b_output.html", "w")
output.write(soup.prettify())
output.close()
