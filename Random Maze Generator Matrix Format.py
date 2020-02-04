from random import randrange

print(randrange(0, 2,1))


def show_maze():
    for i in range(len(Maze)):
        for j in range(len(Maze[i])):
            if Maze[i][j] == -1:
                print("#", end=" ")
            else:
                print(Maze[i][j], end=" ")
        print("")


Maze = [[(randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1))],
        [(randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1))],
        [(randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1))],
        [(randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1))],
        [(randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1))],
        [(randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1)), (randrange(0, 2,1))]]

print("Maze :")
show_maze()