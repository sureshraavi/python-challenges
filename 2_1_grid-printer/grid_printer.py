"""
Update below functions with code to print different grids based on the input parameters.

NOTE: do not print anything besides the grid boxes in your functions.
"""


# PART 1
def print_grid1():
    for _ in range(2):
        print(("+" + "- " * 4) * 2 + "+")
        for _ in range(4):
            print(("|" + "  " * 4) * 2 + "|")
    print(("+" + "- " * 4) * 2 + "+")

print_grid1()

# PART 2
def print_grid2(size):
    for _ in range(2):
        print(("+" + "- " * size) * 2 + "+")
        for _ in range(size):
            print(("|" + "  " * size) * 2 + "|")
    print(("+" + "- " * size) * 2 + "+")

print_grid2(15)


# PART 3
def print_grid3(box_size, cell_size):
    for _ in range(box_size):
        print(("+" + "- " * cell_size) * box_size + "+")
        for _ in range(cell_size):
            print(("|" + "  " * cell_size) * box_size + "|")
    print(("+" + "- " * cell_size) * box_size + "+")


print_grid3(3, 4)
