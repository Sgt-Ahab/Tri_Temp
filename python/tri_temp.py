#Main Project:
#Take and validate numeric-input, and unit: Units (F/C/K)
#Maximum Temperature included, when converted displays all three and asks to run again.
ABS_ZERO_C = -273.15
ABS_ZERO_F = -459.67
ABS_ZERO_K = 0.0

def get_Temp():
    """Read a numeric temperature from user (re-prompts on non-numeric)"""
    while True:
        try:
            temp = float(input("Enter a Temperature: "))
            #print(temp) #Tester Flag Pass{X} --Notes: Number ran through, attempt characters/string; 
            #Manage ValueError for ensure of process. Managed; Function clean.
            break
        except ValueError:
            print("ERROR! Enter a Number/Decimal Only. Try again.")        
    return temp

def get_Unit() -> str:
    """Ask for Temperature Unit (re-prompt when not F/C/K)"""
    while True:
        unit = str(input("Enter Unit: ").strip().upper())       
        while unit != 'F' and unit != 'C' and unit != 'K':
            unit = str(input("Must be 'F/C/K': ").strip().upper())
        break
    #print(unit) #Tester Flag Pass{X} --Notes: Checked the error loop of wrong letter, remove Len
    # this while covered it, no try/except since string validation
    return unit

def abs_Zero(temp: float, unit: str) -> bool:
    """Bool check input is within physical range"""
    if unit == 'K' and temp < ABS_ZERO_K:
        return False
    elif unit == 'K' and temp >= ABS_ZERO_K:
        return True
    elif unit == 'C' and temp < ABS_ZERO_C:
        return False
    elif unit == 'C' and temp >= ABS_ZERO_C:
        return True
    elif unit == 'F' and temp < ABS_ZERO_F:
        return False
    elif unit == 'F' and temp >= ABS_ZERO_F:
        return True
    
def to_Celsius(temp: float, unit: str) -> float:
    """Base conversion to celsius for temp intermission"""
    if unit == 'K':
        temp = temp - 273.15
        return temp
    elif unit == 'F':
        temp = (temp - 32) * 5.0 / 9.0
        return temp
    elif unit == 'C':
        temp = temp
        return temp

def celsFahr(celsius: float) -> float:
    """'cels'ius convert to 'Fahr'enheit for slick application"""
    celsius = celsius * 9.0 / 5.0 + 32.0
    return celsius

def celsKelv(celsius:float) -> float:
    """'cels'ius convert to 'Kelv'in for slick application"""
    celsius = celsius + 273.15
    return celsius

def disp_Res(orig_temp: float, unit: str):
    """'disp'lays 'Res'ults for user interpretation, all three conversions."""
    print(f"{orig_temp:,.2f}° {unit} converted is:\n")
    if unit == 'C':
        print(f"Kelvin: {celsKelv(orig_temp):,.2f}° K\n")
        print(f"Fahrenheit: {celsFahr(orig_temp):,.2f}° F")
    elif unit == 'F':
        orig_temp = to_Celsius(orig_temp, unit)
        print(f"Kelvin: {celsKelv(orig_temp):,.2f}° K\n")
        print(f"Celsius: {orig_temp:,.2f}° C")
    elif unit == 'K':
        orig_temp = to_Celsius(orig_temp, unit)
        print(f"Fahrenheit: {celsFahr(orig_temp):,.2f}° F\n")
        print(f"Celsius: {orig_temp:,.2f}° C")

def runAgain() -> bool:
    """Ask for Y/N only to restart program."""
    while True:
        ask = str(input("Would you like to convert a new number or leave? (Y/N): ").strip().upper())
        while ask != 'Y' and ask != 'N':
            ask = str(input("ERROR! Must be Y/N to Y: Redo; N: Leave; Choice: ").strip().upper())
        break
    if ask == 'Y':
        return True
    elif ask == 'N':
        return False
    
def main():
    """Main Function of the Program"""


#Need to Unit Test and Run:
#Input, Errors, Temps <F:{};C:{};K:{}>
#Run the loop, and make it happen for User Extension of Permission. {}
#Clean Up VSCode CoPilot advisory {}