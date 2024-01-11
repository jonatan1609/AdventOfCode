from sys import argv
from re import compile
from itertools import cycle
from math import lcm
from os.path import join, exists
from os import mkdir


CIRCLE_DIR = 'circles'
GRAPH_LINE_PATTERN = compile(r'(\w+) = \((\w+), (\w+)\)')
LEFT_DIRECTION = 'L'
RIGHT_DIRECTION = 'R'
START_NODE = 'AAA'
END_NODE = 'ZZZ'
START_NODE_SUFFIX = 'A'
END_NODE_SUFFIX = 'Z'


def read_file(filename: str = argv[1]) -> str:
    with open(filename, "r") as f:
        return f.read()


def generate_graph(graph_lines: str) -> dict[str, tuple[str, str]]:
    return {source: (left, right) for source, left, right in GRAPH_LINE_PATTERN.findall(graph_lines)}


def part_1() -> str:
    directions, graph_lines = read_file().split("\n\n")
    graph = generate_graph(graph_lines)
    current_node = START_NODE
    number_of_steps = 0
    for direction in cycle(directions):
        if current_node == END_NODE:
            break
        if direction == LEFT_DIRECTION:
            current_node = graph[current_node][0]
        elif direction == RIGHT_DIRECTION:
            current_node = graph[current_node][1]
        else:
            raise ValueError('Invalid direction')
        number_of_steps += 1
    return f"The result for part 1 is {number_of_steps}"


def part_2_generate_circle_files() -> None:
    """
    Get the circles that each 'ghost' is going through.
    This functions generates files which each contains the circle that each node will eventually go through.
    """
    directions, graph_lines = read_file().split("\n\n")
    graph = generate_graph(graph_lines)
    start_nodes = {node for node in graph if node.endswith(START_NODE_SUFFIX)}
    if not exists(CIRCLE_DIR):
        mkdir(CIRCLE_DIR)
    for node in start_nodes:
        with open(join(CIRCLE_DIR, f'{node}-circle.txt'), 'w') as circle_out_file:
            number_of_steps = 0
            checkpoints = list()
            for idx, direction in enumerate(cycle(directions)):
                idx = idx % len(directions)
                print(idx, node, file=circle_out_file)
                if (idx, node) in checkpoints:
                    checkpoints.append((idx, node))
                    break
                checkpoints.append((idx, node))
                if direction == LEFT_DIRECTION:
                    node = graph[node][0]
                elif direction == RIGHT_DIRECTION:
                    node = graph[node][1]
                else:
                    raise ValueError('Invalid direction')
                number_of_steps += 1


def part_2_slow() -> str:
    directions, graph_lines = read_file().split("\n\n")
    graph = generate_graph(graph_lines)
    current_nodes = {node for node in graph if node.endswith(START_NODE_SUFFIX)}
    end_nodes = {node for node in graph if node.endswith(END_NODE_SUFFIX)}
    number_of_steps = 0
    for direction in cycle(directions):
        if current_nodes <= end_nodes:
            break
        if direction == LEFT_DIRECTION:
            current_nodes = {graph[current_node][0] for current_node in current_nodes}
        elif direction == RIGHT_DIRECTION:
            current_nodes = {graph[current_node][1] for current_node in current_nodes}
        else:
            raise ValueError('Invalid direction')
        number_of_steps += 1
    return f"The result for part 2 is {number_of_steps}"


def part_2() -> str:
    """
    After viewing the circle files, we noticed that the number of steps it takes to get in the circle
    is equal to the number of steps it takes to reach the beginning of the circle from the target node.
    Which means that the final number of steps must be divided by the length of the circle.
    This means that the answer to this part is the least common multiple (lcm) of all the circle lengths.
    """
    directions, graph_lines = read_file().split("\n\n")
    graph = generate_graph(graph_lines)
    start_nodes = {node for node in graph if node.endswith(START_NODE_SUFFIX)}
    circle_lengths = []
    circle_start = None
    for source_node in start_nodes:
        number_of_steps = 0
        checkpoints = []
        node = source_node
        for idx, direction in enumerate(cycle(directions)):
            idx = idx % len(directions)
            if (idx, node) in checkpoints:
                circle_start = (idx, node)
                break
            checkpoints.append((idx, node))
            if direction == LEFT_DIRECTION:
                node = graph[node][0]
            elif direction == RIGHT_DIRECTION:
                node = graph[node][1]
            else:
                raise ValueError('Invalid direction')
            number_of_steps += 1
        target_node = [cp for cp in checkpoints if cp[1].endswith(END_NODE_SUFFIX)][0]
        source_to_circle_start = checkpoints.index(circle_start)
        target_node_index = checkpoints.index(target_node)
        circle_length = len(checkpoints) - source_to_circle_start 
        target_to_circle_start = len(checkpoints) - target_node_index
        # This will always be true for the given input, because of the observation that was mentioned before
        assert source_to_circle_start == target_to_circle_start, "Source to circle start != target to circle"
        circle_lengths.append(circle_length)
    return f"The result for part 2 is {lcm(*circle_lengths)}"


def main() -> None:
    print(part_1())
    # part_2_generate_circle_files()
    print(part_2())


if __name__ == "__main__":
    main()