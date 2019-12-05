# # Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the "1202 program alarm" state it had just before the last computer caught fire. To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?

import sys

RESULT_NUMBER = 19690720
stop_loop = False

def check_v_n_n(x, y, init_input ,memory):
    pointer_pos = 0
    memory[1] = x
    memory[2] = y
            
    while(pointer_pos <= len(init_input)-1):
        
        if(memory[pointer_pos] == 1):
            memory[memory[pointer_pos+3]] = memory[memory[pointer_pos+1]] + memory[memory[pointer_pos+2]]
        elif(memory[pointer_pos] == 2):
            memory[memory[pointer_pos+3]] = memory[memory[pointer_pos+1]] * memory[memory[pointer_pos+2]]
        elif(memory[pointer_pos] == 99):
            break
        else:
            sys.exit("Operation result errors!")

        if(memory[0] == RESULT_NUMBER):
            return 100 * memory[1] + memory[2] 
            break
        else:
            pointer_pos = pointer_pos + 4
    return -1
    

def find_verb_and_noun():
    for x in range(0, 99):
        for y in range(0, 99):
            init_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,2,9,19,23,1,23,6,27,1,13,27,31,1,31,10,35,1,9,35,39,1,39,9,43,2,6,43,47,1,47,5,51,2,10,51,55,1,6,55,59,2,13,59,63,2,13,63,67,1,6,67,71,1,71,5,75,2,75,6,79,1,5,79,83,1,83,6,87,2,10,87,91,1,9,91,95,1,6,95,99,1,99,6,103,2,103,9,107,2,107,10,111,1,5,111,115,1,115,6,119,2,6,119,123,1,10,123,127,1,127,5,131,1,131,2,135,1,135,5,0,99,2,0,14,0]
            memory = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,2,9,19,23,1,23,6,27,1,13,27,31,1,31,10,35,1,9,35,39,1,39,9,43,2,6,43,47,1,47,5,51,2,10,51,55,1,6,55,59,2,13,59,63,2,13,63,67,1,6,67,71,1,71,5,75,2,75,6,79,1,5,79,83,1,83,6,87,2,10,87,91,1,9,91,95,1,6,95,99,1,99,6,103,2,103,9,107,2,107,10,111,1,5,111,115,1,115,6,119,2,6,119,123,1,10,123,127,1,127,5,131,1,131,2,135,1,135,5,0,99,2,0,14,0]

            checker = check_v_n_n(x, y, init_input, memory) 
            if(checker != -1):
                return checker
    
print(find_verb_and_noun())
