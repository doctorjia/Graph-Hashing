import os


def train_test_split(input_name):
    infile = open("data/" + input_name + ".bss", "r")
    all_lines = infile.readlines()
    count_graphnum = 0
    for each_line in all_lines:
        num_of_spaces = each_line.count(" ")
        if num_of_spaces == 0:
            content = int(each_line.strip("\n"))
            if content > 50:
                count_graphnum += 1

    return count_graphnum


AIDS_num = train_test_split("AIDS")
ALCHEMY_num = train_test_split("ALCHEMY")
linux_num = train_test_split("linux15")

print("AIDS: ", AIDS_num, "ALCHEMY: ", ALCHEMY_num, "linux15: ", linux_num)