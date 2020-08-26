from list_node import Lists
from add_two_numbers02 import AddTwoNumbers02


def create_list():
    # list1 = [3, 5, 1, 7, 9]
    # list2 = [4, 6, 2, 1]
    list1 = [5]
    list2 = [5]
    link_list1 = (Lists().createList(list1))
    link_list2 = (Lists().createList(list2))
    return link_list1, link_list2


if __name__ == '__main__':
    l1, l2 = create_list()
    list = AddTwoNumbers02().add_two_numbers(l1, l2)
    print(list)

    # Lists().createList()
