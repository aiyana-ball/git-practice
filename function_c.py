def merge_lists(list_a, list_b):
    new_list = list_a + list_b
    final_list = set(new_list)
    return final_list


if __name__ == "__main__":
    print(merge_lists([1, 1, 2, 3], [3, 4, 5]))
