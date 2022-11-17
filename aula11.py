"""Code made in lesson 11 of IPRP course"""

def negative_image(mega_list):
    """Make negative image"""
    for list in mega_list:
        for i in range(len(list)):
            if list[i] == 1:
                list[i] = 0
            else:
                list[i] = 1
    return mega_list


def rotate_image(mega_list):
    """Rotate matrix 90 degrees
    O(n) = n^2 + n (it sucks)
    """
    rotated_list = []
    for i in range(len(mega_list[0])):
        new_line = []
        rotated_list.append(new_line)
    for list in reversed(mega_list):
        j = 0
        for i in range(len(list)):
            rotated_list[j].append(list[i])
            j += 1
    return rotated_list


if __name__ == "__main__":
    print(negative_image([[0, 1, 0], [1, 1, 1], [0, 1, 0]]))
    print(rotate_image([[2, 1, 0], [1, 1, 1], [0, 1, 2]]))
    print(rotate_image([[2], [1]]))
