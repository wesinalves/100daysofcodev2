'''
How to program in Python - Chapter 5
Slicing sequences.
'''


def main():
    '''Slicing sequences example'''
    # create sequences
    slice_string = "abcdefghij"
    slice_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    slice_list = ["I", "II", "III", "IV", "V", \
        "VI", "VII", "VIII", "IX", "X"]

    # print strings
    print("slice_string: ", slice_string)
    print("slice_tuple: ", slice_tuple)
    print("slice_list: ", slice_list)
    print()

    # get slices
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))

    # print slices
    print("\nslice_string[", start, ":", end, "] = ",
          slice_string[start:end])
    print("\nslice_tuple[", start, ":", end, "] = ",
          slice_tuple[start:end])
    print("\nslice_list[", start, ":", end, "] = ",
          slice_list[start:end])

main()
