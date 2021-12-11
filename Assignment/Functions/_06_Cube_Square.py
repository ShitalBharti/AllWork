import math

def printCubeSquare():
    range_in = int(input("Enter range:"))
    square_list = []
    cube_list = []
    for i in range(1,range_in+1):
        square_list.append(math.pow(i,2))
        cube_list.append(math.pow(i,3))
    print("Squares:{}".format(square_list))
    print("Cubes:{}".format(cube_list))

printCubeSquare()