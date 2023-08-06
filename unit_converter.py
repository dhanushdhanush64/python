def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_feet(meters):
    return meters / 0.3048

def main():
    print("Unit Converter: Feet to Meters and Meters to Feet")
    choice = input("Select conversion:\n1. Feet to Meters\n2. Meters to Feet\nEnter choice (1/2): ")

    if choice == '1':
        feet = float(input("Enter length in feet: "))
        meters = feet_to_meters(feet)
        print(f"{feet} feet is approximately {meters:.2f} meters.")
    elif choice == '2':
        meters = float(input("Enter length in meters: "))
        feet = meters_to_feet(meters)
        print(f"{meters} meters is approximately {feet:.2f} feet.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
