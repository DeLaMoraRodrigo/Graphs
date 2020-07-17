from collections import deque

def earliest_ancestor(ancestors, starting_node):
    tree = dict()
    for pair in ancestors:
        tree[pair[1]] = tree.get(pair[1], []) # Initialize child key with empty list if not in dictionary
        tree[pair[1]].append(pair[0]) # Append parent to child key
        tree[pair[0]] = tree.get(pair[0], []) # Initialize parent key with empty list if not in dictionary
    # print(tree.items())

    if tree[starting_node] == []: # If starting node has no parents
        return -1

    s = deque()
    visited = set()
    paths = list()
    s.append([starting_node])

    while len(s) > 0:
        path = s.pop()
        last_node = path[-1]

        if last_node not in visited:
            visited.add(last_node)

            for parent in tree[last_node]:
                copy_path = path.copy()
                copy_path.append(parent)
                s.append(copy_path)
                paths.append(copy_path) # Append each path to list of paths
    print("Paths: ", paths)
    answers = list()

    for path in paths: # Search all valid paths
        longest = max(paths, key=len) # Finds longest path
        if len(path) == len(longest): # Checks paths that have same length as longest path
            answers.append(path)

    answers.sort(key = lambda e: e[-1]) # Sorts arrays by last index ascendingly
    print("Answers: ", answers)
    return answers[0][-1] # Returns last node in first array





test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (11, 5), (11, 8), (8, 9), (4, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 9))