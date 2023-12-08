from pprint import pprint
import re
import math

def read_file(filename):
  buffer = []
  with open(filename) as f:
      line = f.readline()
      while line:
          if line.strip() != '': 
            buffer.append(line.strip())
          line = f.readline()

  return buffer[0], buffer[1:]

def extract_parts(input_string):
    pattern = r'(\w+)\s=\s(\(.*\))'
    match = re.match(pattern, input_string)

    if match:
        tuple_str = match.group(2)
        pattern_elements = r'\b\w+\b'
        elements = re.findall(pattern_elements, tuple_str)
        tuple_elements = tuple(elements)
        return match.group(1), tuple_elements

    return None, None

def create_graph(nodes):
  graph = {}
  for node in nodes:
    start, end = extract_parts(node)
    graph[start] = end
  return graph

def get_count_for_node(graph, instructions, cur_node):
  cur_instr, count = 0, 0
  is_not_end = True

  while is_not_end:
    not_end_for_loop = False

    if instructions[cur_instr] == 'L':
      cur_node = graph[cur_node][0]
      if cur_node[2] != 'Z': not_end_for_loop = True
    else:
      cur_node = graph[cur_node][1]
      if cur_node[2] != 'Z': not_end_for_loop = True
    
    count += 1
    cur_instr += 1
    if cur_instr >= len(instructions): cur_instr = 0
    is_not_end = not_end_for_loop

  return count

def solution(filename):
  instructions, nodes = read_file(filename)
  graph = create_graph(nodes)  
  instructions = [instruction for instruction in instructions]

  cur_nodes = []
  for node in graph.keys():
    if node[2] == 'A': cur_nodes.append(node)

  counts = []
  for node in cur_nodes:
    counts.append(get_count_for_node(graph, instructions, node))

  return math.lcm(*counts)

if __name__ == "__main__":
  small = "input_small.txt"
  small2 = "input_small2.txt"
  large = "input_large.txt"

  print(solution(small))
  # print(solution(small2))
  print(solution(large))
