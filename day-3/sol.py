from pprint import pprint

BLANK = '.'

def read_file(filename):
  buffer = []
  with open(filename) as f:
      line = f.readline()
      while line:
          tmp = []
          line = line.strip()
          for char in line: tmp.append(char)
          buffer.append(tmp)
          line = f.readline()

  return buffer

def solution():
  schematic = read_file("input_small.txt")
  rows = len(schematic)
  cols = len(schematic[0])

  def is_part(point):
    return point != BLANK and not point.isdigit()

  def is_valid_part(x, y):
    if x-1 >= 0 and x-1 < rows:
      if y-1 >= 0 and y-1 < cols and is_part(schematic[x-1][y-1]): return True
      if y >= 0 and y < cols and is_part(schematic[x-1][y]): return True
      if y+1 >= 0 and y+1 < cols and is_part(schematic[x-1][y+1]): return True

    if y-1 >= 0 and y-1 < cols and is_part(schematic[x][y-1]): return True
    if y+1 >= 0 and y+1 < cols and is_part(schematic[x][y+1]): return True

    if x+1 >= 0 and x+1 < rows:
      if y-1 >= 0 and y-1 < cols and is_part(schematic[x+1][y-1]): return True
      if y >= 0 and y < cols and is_part(schematic[x+1][y]): return True
      if y+1 >= 0 and y+1 < cols and is_part(schematic[x+1][y+1]): return True

    return False

  # create a set of all numbers which are adjacent to parts where
  # each element is a tuple representing index (eg. (a, b))
  adj_to_parts = set()

  for x in range(rows):
    for y in range(cols):
      point = schematic[x][y]
      if point != BLANK and point.isdigit():
        if is_valid_part(x, y): adj_to_parts.add((x, y))

  pprint(adj_to_parts)
        

if __name__ == "__main__":
  solution()
