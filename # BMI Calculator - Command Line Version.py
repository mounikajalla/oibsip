# BMI Calculator - Command Line Version

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))
        if weight <= 0 or height <= 0:
            print("Please enter positive values for weight and height.")
            return
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        print(f"Your BMI is {bmi}. Category: {category}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()