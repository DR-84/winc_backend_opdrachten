def contains_only_ints(lst):
    int_list = [e for e in lst if isinstance(e, int)]
    return sum_list(int_list)


def sum_list(int_list):
    sum_of_list = sum(int_list)

    return sum_of_list
