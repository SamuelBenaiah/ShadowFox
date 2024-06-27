# Define the lists of cities per country
cities_by_country = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

# Function to find the country of a given city
def find_country(city_name):
    for country, cities in cities_by_country.items():
        if city_name in cities:
            return country
    return None

# Main program
def main():
    # Ask the user for input
    city_name = input("Enter a city name: ")

    # Find the country for the given city
    country = find_country(city_name)

    # Output the result
    if country:
        print(f"{city_name} is in {country}")
    else:
        print(f"{city_name} is not in the list")

# Run the main program
if __name__ == "__main__":
    main()