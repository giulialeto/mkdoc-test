def celsius_to_kelvin(celsius):
    if celsius < -273.15:
        raise ValueError("Invalid temperature")
    return celsius + 273.15

def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        raise ValueError("Invalid temperature")
    return celsius * 9/5 + 32

def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Invalid temperature")
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    if kelvin < 0:
        raise ValueError("Invalid temperature")
    return (kelvin - 273.15) * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    if fahrenheit < -459.67:
        raise ValueError("Invalid temperature")
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    if fahrenheit < -459.67:
        raise ValueError("Invalid temperature")
    return (fahrenheit - 32) * 5/9 + 273.15

def convert_temperature(temperature, unit):
    '''
    Convert temperature between Celsius, Fahrenheit, and Kelvin.
    
    Args:
    temperature (float): Temperature value to convert.
    unit (str): Unit of the input temperature. Can be "C", "F", or "K".
    Returns:
    list: List of converted temperature values.
    list: List of units of the converted temperatures.
    str: Message with the converted temperatures
    '''
    if unit == "F":
        # Convert Fahrenheit to Celsius & Kelvin
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        return [celsius, kelvin], ["C", "K"], f"{temperature} F = {celsius:.2f} C = {kelvin:.2f} K"
    elif unit == "C":
        # Convert Celsius to Fahrenheit & Kelvin
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        return [fahrenheit, kelvin], ["F", "K"], f"{temperature} C = {fahrenheit:.2f} F = {kelvin:.2f} K"
    elif unit == "K":
        # Convert Kelvin to Celsius & Fahrenheit
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        return [celsius, fahrenheit], ["C", "F"], f"{temperature} K = {celsius:.2f} C = {fahrenheit:.2f} F"
    else:
        raise ValueError("Invalid unit")
    
temperature = 350
unit = "K"

print(convert_temperature(temperature, unit))

temperature, units, message = convert_temperature(temperature, unit)

temperature = -500
unit = "C"

print(convert_temperature(temperature, unit))

temperature, units, message = convert_temperature(temperature, unit)