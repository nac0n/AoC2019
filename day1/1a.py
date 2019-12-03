# Day 1
# The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.
# What is the sum of the fuel requirements for all of the modules on your spacecraft?

def get_raw_mass_input():
    File_object = open("input.txt","r+")
    file_content = File_object.read()
    file_content = file_content.split('\n')
    return file_content

def calc_module_fuel_amount(module_mass):
    return int(int(module_mass)/3 - 2)

def fuel_sum():
    fuel_total = 0
    module_array = get_raw_mass_input()
    for module in range(0, len(module_array)):
        fuel_total += calc_module_fuel_amount(module_array[module])
    return fuel_total

print(fuel_sum())