
def get_input():
    File_object = open("input.txt","r+")
    parsed_input = [x.strip().split(')') for x in File_object.readlines()]

    return parsed_input

def get_number_of_orbits():
    print(get_input())
    return 0


print(get_number_of_orbits())