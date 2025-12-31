# This is for the main loop of the FKC Conversion Module
# Housing all the calls for the temp_request

# import clauses
from f_temp_tri import fcswap, cfswap, kfswap, fkswap
from c_k_pair import ckswap, kcswap
# aliases

def temp_request(temp, unit):
    """This is for taking temperature request, 
    and a logic block to prevent non-integer usage"""
    temp = float(input("Number of Temp: "))
    unit = input("Unit Type (F, C, K): ").upper()
    return temp, unit
        
# 'req'uest 'conv'ersion is for final temp piece

def req_conv(temp, unit):
    """This is the code block for handling
      final request conversion to be consolidated to print"""
    request = input("Convert to (F, C, K): ").upper()
    if request == 'F' and unit == 'C':
        return cfswap(temp, unit)
    elif request == 'C' and unit == 'F':
        return fcswap(temp, unit)
    elif request == 'K' and unit == 'F':
        return fkswap(temp, unit)
    elif request == 'F' and unit == 'K':
        return kfswap(temp, unit)
    elif request == 'C' and unit == 'K':
        return kcswap(temp, unit)
    elif request == 'K' and unit == 'C':
        return ckswap(temp, unit)
    else:
        while(request not in ['F', 'C', 'K'] or request == unit):
            print("Invalid request, try again.")
            request = input("Convert to (F, C, K): ").upper()
# insert usage of temp_request to requested modules
    def main():
        """Main loop for temp conversion module."""
        temp, unit = temp_request(temp, unit)
        new_temp, new_unit = req_conv(temp, unit)
        print(f"Converted Temperature: {new_temp:.2f} {new_unit}")
    if __name__ == "__main__":
        main()          
# end result displayed