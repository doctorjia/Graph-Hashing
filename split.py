import os


def train_test_split(input_name, stop_val):
    infile = open("data/" + input_name + ".bss", "r")
    train_file = open("data/" + input_name + "/train/graphs.bss", "w")
    test_file = open("data/" + input_name + "/test/graphs.bss", "w")
    all_lines = infile.readlines()
    count_graphnum = 0
    writing_in_train = True
    for each_line in all_lines:
        num_of_spaces = each_line.count(" ")
        if num_of_spaces == 0:
            content = int(each_line.strip("\n"))
            if content > 50:
                count_graphnum += 1
            if count_graphnum == stop_val:
                writing_in_train = False
        if writing_in_train:
            train_file.write(each_line)
        else:
            test_file.write(each_line)

    infile.close()
    train_file.close()
    test_file.close()

    return count_graphnum


AIDS_num = train_test_split("AIDS", 42587)
ALCHEMY_num = train_test_split("ALCHEMY", 24087)
linux_num = train_test_split("linux15", 99676)

print("AIDS: ", AIDS_num, "ALCHEMY: ", ALCHEMY_num, "linux15: ", linux_num)