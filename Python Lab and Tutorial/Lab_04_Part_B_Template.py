import csv

#==============================================================================#
#                                    PART A                                    #
#==============================================================================#

### Paste your answers from Part A below. ###




#==============================================================================#
#                                  Question 3                                  #
#==============================================================================#

# NOTE: There is a difference between ' and " in a string.

# RECALL THAT:
# >>> print("foo")
# 3
# >>> print('"foo"')
# "foo"


# Input: < string > file path to encrypted message csv
# Output: < string > encrypted message
# Hint: This is a helper function.
def read_message(file_path_message):
    ## FILL IN HERE
    return


# Input 1: < dict > translation guide
# Input 2: < string > encrypted message
# Output: < string > decrypted message
def decipher_message(translation_guide, message):
    ## FILL IN HERE
    return 


# Uncomment code below to test (DO NOT paste into Coursemology!)
#print("*** QUESTION 3 ***")
#my_translation_guide = read_translation_guide_into_dictionary('translation.csv')
#my_encrypted_message = read_message('message.txt')
#print(decipher_message(my_translation_guide, my_encrypted_message))


#==============================================================================#
#                                  Question 4                                  #
#==============================================================================#

# Input 1: < string > file path to encrypted map
# Input 2: < string > file path to translation guide csv
# Output: < None >
def decrypt_map(file_path_encrypted_map, file_path_translation_guide):
    ## FILL IN HERE
    return


# Uncomment code below to test (DO NOT paste into Coursemology!)
#print("*** QUESTION 4 ***")
#decrypt_map('encrypted_map.txt', 'map_code.csv')


#==============================================================================#
#                  Additional Practice Questions (Zero marks)                  #
#==============================================================================#

def read_csv_into_2d_array(file_path):
    return


# Input: < sequence of sequences > capulator 2D array
# Output: < float > CAP score
def capculate(capulator_2d_array):
    return


# Input: < sequence of sequences > capulator 2D array
# Input: < float > target CAP
# Output: < string > Message of how many A's
def target(capulator_2d_array, cap_target):
    # Create a duplicate list so that you don't modify the input
    capulator_2d_array_dup = list(capulator_2d_array)
    return
