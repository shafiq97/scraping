import csv
import requests
from bs4 import BeautifulSoup

# Download the webpage
url = "http://insideairbnb.com/explore"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

# Open a CSV file for writing
with open('airbnb_locations.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['City', 'Region', 'Country'])

    # find the data based on DOMs
    for continent_container in soup.find_all('div', class_='continentContainer'):
        for country_label in continent_container.find_all('p', class_='countryLabel'):
            country = country_label.text.strip()

            for city_label in country_label.find_all_next('p', class_='cityLabel'):
                city_link = city_label.find('a')
                # remove commented code
                if city_link:
                    city = city_link.text.strip()
                    region = city_label.text.split(
                        city)[1].strip().lstrip("<!-- -->")
                else:
                    city = city_label.text.strip()
                    region = ""

                # Write the data row
                writer.writerow([city, region, country])
