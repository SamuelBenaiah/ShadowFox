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
    city1 = input("Enter the first city: ")
    city2 = input("Enter the second city: ")

    # Find the countries for the given cities
    country1 = find_country(city1)
    country2 = find_country(city2)

    # Output the result
    if country1 and country2:
        if country1 == country2:
            print(f"Both cities are in {country1}")
        else:
            print("They don't belong to the same country")
    else:
        print("One or both cities are not in the list")

# Run the main program
if __name__ == "__main__":
    main()
