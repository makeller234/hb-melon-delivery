## Code Re-vamp with function

def melon_delivery(file_name):
    """Input Uber-Melon Delivery File, prints it in a prettier form"""

    # assigns the file with the name given in the function parameter to the variable the_file
    the_file = open(file_name)

    #create an empty list variable to eventually hold the correctly formatted contents of the file
    prettier_version = []

    #loop through each row in the file
    for line in the_file:

        #remove all the extra whitespace characters that are to the right on the line
        line = line.rstrip()

        #split the line apart into words with the word breaks being at the | symbol
        word = line.split('|')

        #use indexing to reference the placement of the word and assign it to it's corresponding variable name
        melon = word[0]
        count = word[1]
        amount = word[2]

        #add each line to "empty" list (empty in quotes becuase once it gets here once it's not empty anymore)
        prettier_version.append(f'Delivered {count} {melon}s for a total of {amount}.')

    #return the correctly formatted list of melons and prices
    # formatting help from StackOverflow: https://stackoverflow.com/questions/22695171/print-list-elements-line-by-line-is-it-possible-using-format
    # towards the bottom, surprisingly 0 upvotes, but it worked for what I needed.
    return ("\n".join(prettier_version))

#creat a list of all the file names
files = ['um-deliveries-20140519.txt', 'um-deliveries-20140520.txt', 'um-deliveries-20140521.txt']

#assign a variable for the day value, so that we can update it in our final list to keep track of which 
# orders happened on which days
day = 1

#loop over all the file names in the files list variable
for one_file in files:

    #print off what day number it is
    print(f'Day {day}.')

    #call the above function and print it
    print(melon_delivery(one_file))

    #increment the day variable so that it is updated for the next time through the loop.
    day += 1


## Initial Code

# print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()
