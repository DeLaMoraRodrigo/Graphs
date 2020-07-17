from room import Room
from player import Player
from world import World
from util import Graph

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def start():
    graph = Graph()
    # CACHE ALL ROOMS WITH NEIGHBOR ID AS KEY AND DIRECTION AS VALUE
    dft_rooms = graph.dft(player.current_room)
    # MAKE LIST OF ROOMS
    rooms = [room for room in dft_rooms]
    print(dft_rooms)
    print("HOW MANY ROOMS", len(dft_rooms.keys()), "********")
    print(rooms)
    print("HOW MANY ROOMS", len(rooms), "********")
    # FIND SHORTEST PATH TO EACH ROOM
    path = graph.bfs(rooms[0], rooms[1])
    print("SHORTEST", path, "PATH")
    # CHECK NEIGHBORING ROOMS OF PATH AT INDEX 0
    neighbors = dft_rooms[path[0]]
    print("NEIGHBORS OF", neighbors, "SHORTEST AT INDEX 0")
    # FIND THE DIRECTION VALUE OF THE ROOM AT INDEX 1 SO IT CAN BE APPENDED TO TRAVERSAL PATH
    value = neighbors[path[1]]
    print("VALUE OF", value, "SHORTEST AT INDEX 1 IN NEIGHBORS OF SHORTEST AT INDEX 0")

# start()


def single_traverse():
    graph = Graph()
    visited = set()
    mapped_rooms = graph.dft(player.current_room)
    rooms = [room for room in mapped_rooms]

    while len(visited) < len(room_graph) - 1:
        # print(rooms[0])
        path = graph.bfs(rooms[0], rooms[1])

        while len(path) > 1:
            cur_room = path[0]
            adj_room = path[1]
            if adj_room in mapped_rooms[cur_room]:
                traversal_path.append(mapped_rooms[cur_room][adj_room])
            path.remove(cur_room)
        rooms.remove(rooms[0])
        visited.add(rooms[0])
    

single_traverse()


def traverse():
    graph = Graph()
    visited = set()
    test_path = list()
    mapped_rooms = graph.dft(player.current_room)
    rooms = [room for room in mapped_rooms]

    while len(visited) < len(room_graph) - 1:
        # print(rooms[0])
        path = graph.bfs(rooms[0], rooms[1])

        while len(path) > 1:
            cur_room = path[0]
            adj_room = path[1]
            if adj_room in mapped_rooms[cur_room]:
                test_path.append(mapped_rooms[cur_room][adj_room])
            path.remove(cur_room)
        rooms.remove(rooms[0])
        visited.add(rooms[0])
    
    return test_path


def get_that_960():
    global traversal_path
    traversal_path = traverse()
    print(f"TESTS PASSED: {len(traversal_path)} moves")

    old_length = len(traversal_path)
    # print(old_length)

    while len(traversal_path) > 957:
        traversal_path = traverse()
        if len(traversal_path) < old_length:
            print(f"TESTS PASSED: {len(traversal_path)} moves")
            old_length = len(traversal_path)

# get_that_960()

# traverse()
# print("TRAVERSAL PATH \n", traversal_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
