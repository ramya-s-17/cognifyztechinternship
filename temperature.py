while True:
    try:
        temp = float(input("Enter the temperature value (or type 'exit' to quit): "))
    except ValueError:
        user_input = input("Invalid input. Type 'exit' to quit or try again: ").strip().lower()
        if user_input == "exit":
            break
        else:
            continue

    unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").strip().upper()
    
    if unit == "C":
        converted = (temp * 9/5) + 32
        print(f"{temp}°C is equal to {converted:.2f}°F")
    elif unit == "F":
        converted = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {converted:.2f}°C")
    else:
        print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
