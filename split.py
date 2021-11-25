import os
import sys


def train_test_split(input_name, stop_val):
    infile = open("data/" + input_name + ".bss", "r")
    train_file = open("data/" + input_name + "/train/graphs.bss", "w")
    test_file = open("data/" + input_name + "/test/graphs.bss", "w")
    all_lines = infile.readlines()
    count_graphnum = 0
    exceed_val = 0
    smallest_graphid = sys.maxsize
    writing_in_train = True
    read_graphid = True
    for each_line in all_lines:
        num_of_spaces = each_line.count(" ")
        if num_of_spaces == 0:
            content = int(each_line.strip("\n"))
            if read_graphid:
                smallest_graphid = min(content, smallest_graphid)
                count_graphnum += 1
                read_graphid = False
            if count_graphnum == stop_val:
                writing_in_train = False
        if num_of_spaces == 1:
            content = each_line.strip("\n").split(" ")
            if int(content[0]) > exceed_val or int(content[1]) > exceed_val:
                exceed_val = max(max(int(content[0]), int(content[1])), exceed_val)
        if num_of_spaces == 2 and not read_graphid:
            read_graphid = True
        if writing_in_train:
            train_file.write(each_line)
        else:
            test_file.write(each_line)

    print("Exceed! Largest threshold should be " + str(exceed_val))
    print("Smallest id for " + input_name + " " + str(smallest_graphid))

    infile.close()
    train_file.close()
    test_file.close()

    return count_graphnum


# AIDS_num = train_test_split("AIDS", 42587)
# ALCHEMY_num = train_test_split("ALCHEMY", 24087)
# linux_num = train_test_split("linux15", 99676)

# print("AIDS: ", AIDS_num, "ALCHEMY: ", ALCHEMY_num, "linux15: ", linux_num)

test = train_test_split("temp", 1)
print(test)