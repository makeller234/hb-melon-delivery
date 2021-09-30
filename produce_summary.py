## Code Re-vamp with function

def melon_delivery(file_name):
    """Input Uber-Melon Delivery File, prints it in a prettier form"""

    the_file = open(file_name)
    prettier_version = []
    for line in the_file:
        line = line.rstrip()
        word = line.split('|')

        melon = word[0]
        count = word[1]
        amount = word[2]

        prettier_version.append(f'Delivered {count} {melon}s for a total of {amount}.')

    return prettier_version


files = ['um-deliveries-20140519.txt', 'um-deliveries-20140520.txt', 'um-deliveries-20140521.txt']

day = 1
for one_file in files:
    print(f'Day {day}.')
    print(melon_delivery(one_file))
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
