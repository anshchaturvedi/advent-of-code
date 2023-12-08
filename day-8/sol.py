from pprint import pprint
import re

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

def solution(filename):
  instructions, nodes = read_file(filename)
  graph = create_graph(nodes)  
  instructions = [instruction for instruction in instructions]

  cur_node, cur_instr = 'AAA', 0
  count = 0
  while cur_node != 'ZZZ':
    if instructions[cur_instr] == 'L':
      cur_node = graph[cur_node][0]
    else:
      cur_node = graph[cur_node][1]
    count += 1
    cur_instr += 1
    if cur_instr >= len(instructions):
      cur_instr = 0

  return count

if __name__ == "__main__":
  small = "input_small.txt"
  small2 = "input_small2.txt"
  large = "input_large.txt"

  print(solution(small))
  print(solution(small2))
  print(solution(large))
