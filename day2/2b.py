# # # Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the "1202 program alarm" state it had just before the last computer caught fire. To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?

# import sys

# def get_input():
#     File_object = open("input.txt","r+")
#     file_content = File_object.read().split(',')
    
#     # convert each to int
#     for i in range(0, len(file_content)): 
#         if(i == 1):
#             file_content[i] = 12
#         elif(i == 2):
#             file_content[i] = 2
#         else:
#             file_content[i] = int(file_content[i]) 
#     return file_content

# def get_end_value_for_first():
#     input_array = get_input()
#     for i in range(0, len(input_array)):
        
#         if(i % 4 != 0):
#             continue
#         if(input_array[i] == 1):
#             input_array[input_array[i+3]] = input_array[input_array[i+1]] + input_array[input_array[i+2]]
#         elif(input_array[i] == 2):
#             input_array[input_array[i+3]] = input_array[input_array[i+1]] * input_array[input_array[i+2]]
#         elif(input_array[i] == 99):
#             break
#         else:
#             sys.exit("Operation result errors!")
#     return input_array[0]

# print(get_end_value_for_first())