__author__ = 'vz'

def main():
    left, right = input(">> Enter the words being launched: ").split(' ')

    left_points = 0
    right_points = 0
    leftovers = ""

    right_len_init = len(right)

    for l in left:
        if l in right:
            right = right.replace(l, '', 1)
            left = left.replace(l, '', 1)
        else:
            left_points += 1

    left_points = len(left)
    right_points = len(right)
    leftovers = left + right

    print("Right score: ", right_points)
    print("Left score: ", left_points)
    print("Letters in the valley: ", leftovers)




if __name__ == '__main__':
    main()