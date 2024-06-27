# Function to determine BMI category
def determine_bmi_category(bmi):
    if bmi >= 30:
        return "Obesity"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Underweight"

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Main program
def main():
    # Ask the user for input
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Determine BMI category
    bmi_category = determine_bmi_category(bmi)

    # Output the result
    print(f"Output: \"{bmi_category}\"")

# Run the main program
if __name__ == "__main__":
    main()
