# Module for Fahrenheit temperature input to be made to Celsius / Kelvin
# Tri is to represent the extra step for exchange .

def fcswap(temp, unit):
    """Converts F input to C, and returns C for push."""
    temp = (temp - 32) / 1.8
    unit = 'C'
    return temp, unit

def cfswap(temp, unit):
    """Converts C to F and returns F to push."""
    temp = (temp * 1.8) + 32
    unit = 'F'
    return temp, unit
# At first was gonna make separate, but since it uses C, can utilize fcswap and cfswap for F—K/K—F

def kfswap(temp, unit):
    """Directly Convert Kelvin to Fahrenheit."""
    temp = ((temp - 273.15) * 1.8) + 32
    unit = 'F'
    return temp, unit

def fkswap(temp, unit):
    """Takes F returns to K for push."""
    temp = ((temp -32) / 1.8) + 273.15
    unit = 'K'
    return temp, unit