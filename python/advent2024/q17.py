from collections import defaultdict


def part1(reg_a, reg_b, reg_c, instructions):
    i = 0

    def operand(val):
        if val <= 3:
            return val
        if val == 4:
            return reg_a
        if val == 5:
            return reg_b
        if val == 6:
            return reg_c
        return 'invalid value'

    output = []
    while i < len(instructions):
        incr = 2
        operator = instructions[i]
        cmb_operand = operand(instructions[i + 1])
        lit_operand = instructions[i + 1]

        if operator == 0:
            # adv
            reg_a = int(reg_a / (2 ** cmb_operand))
        elif operator == 1:
            # bxl
            reg_b = reg_b ^ lit_operand
        elif operator == 2:
            # bst
            reg_b = cmb_operand % 8
        elif operator == 3:
            # jnz
            if reg_a != 0:
                i = lit_operand
                incr = 0
        elif operator == 4:
            # bxc
            reg_b = reg_b ^ reg_c
        elif operator == 5:
            # out
            # print(f"outputing {cmb_operand}")
            out = cmb_operand % 8
            output.append(out)
            # if output[0] != 2:
            #     return 0, [0]
        elif operator == 6:
            reg_b = int(reg_a / (2 ** cmb_operand))
        elif operator == 7:
            reg_c = int(reg_a / (2 ** cmb_operand))

        # print(f"a={reg_a} b={reg_b} c={reg_c}")
        i += incr

    # print(f"a={reg_a} b={reg_b} c={reg_c}")
    return reg_a, output


def part2(instructions):
    ra = 57752929045

    for i in range(0o1000000000000):
        a = ra * 0o10000 + i
        reg_a, z = part1(a, 0, 0, instructions)
        if z == [2, 4, 1, 3, 7, 5, 4, 7, 0, 3, 1, 5, 5, 5, 3, 0]:
            print(len(z), z, a, oct(a))
            return a
        # print(len(z), z, a, oct(a))

    return -1


# print(part2(0, 0, [0,3,5,4,3,0]))
print(part2([2, 4, 1, 3, 7, 5, 4, 7, 0, 3, 1, 5, 5, 5, 3, 0]))

# test
# print(part1(729, 0, 0, [0,1,5,4,3,0]))

# print(part1(0,0,9,[2,6]))
# print(part1(10,0,0,[5,0,5,1,5,4]))
# print(part1(2024,0,0,[0,1,5,4,3,0]))
# print(part1(0,29,0,[1,7]))
# print(part1(0,2024,43690,[4,0]))


# actual
# print(part1(52884621, 0, 0, [2,4,1,3,7,5,4,7,0,3,1,5,5,5,3,0]))

# print(part2(input_data))
# a 2024
# a 1012
#  out 4
#  a 506
# out 2
