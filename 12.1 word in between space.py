#Function that right-justifies a string 's' so its last letter is at column 70
def right_justify(s):
    #step 1: find how many total spaces are needed on the left
    #we subtract the length of the string from 70
    num_spaces = 70-len(s)

    #step 2: create the leading spaces by repeating the space character " " 
    leading_space = " "*num_spaces
    #step 3: add the leading spaces and the string s together.
    result=leading_space + s
    #step 4: print the final right aligned string to the screen.
    print(num_spaces)
    print(result)

right_justify('pa')





#Function that centers a string s within an 80 character wide line
def center_justify(s):
    #calculate total empty space (80-string length)
    #then divide by 2 to get only the left side spaces
    left_spaces = (80-len(s))//2
    #create the leading spaces for the left side, and combine left spaces with the string 
    result = (" "*left_spaces)+s

    #print the centered string to the screen
    print(left_spaces)
    print(result)


center_justify("diya")
