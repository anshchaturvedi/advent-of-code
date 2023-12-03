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

def is_part(point):
  return point != BLANK and not point.isdigit()

def is_valid_part(schematic, rows, cols, x, y):
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

def solution():
  schematic = read_file("input_large.txt")
  rows = len(schematic)
  cols = len(schematic[0])

  # create a set of all numbers which are adjacent to parts where
  # each element is a tuple representing index (eg. (a, b))
  adj_to_parts = set()

  for x in range(rows):
    for y in range(cols):
      point = schematic[x][y]
      if point != BLANK and point.isdigit():
        if is_valid_part(schematic, rows, cols, x, y): adj_to_parts.add((x, y))

  # get sum of non-parts
  non_parts = []
  for x in range(rows):
    y = 0
    while y < cols:
      point = schematic[x][y]
      if point.isdigit():
        acc, good = [], True
        while point.isdigit() and y < cols:
          if (x, y) in adj_to_parts: good = False
          point = schematic[x][y]
          acc.append(point)
          y += 1
        if good: non_parts.append(acc)
      else:
        y += 1

  # get sum of everything
  everything = []
  for x in range(rows):
    y = 0
    while y < cols:
      point = schematic[x][y]
      if point.isdigit():
        acc = []
        while point.isdigit() and y < cols:
          point = schematic[x][y]
          acc.append(point)
          y += 1
        everything.append(acc)
      else:
        y += 1

  ans = 0
  for num in everything:
    if not num[-1].isdigit(): num.pop()
    ans += int("".join(num))
  for num in non_parts:
    if not num[-1].isdigit(): num.pop()
    ans -= int("".join(num))

  return ans

def solution2():
  schematic = read_file("input_large.txt")
  rows = len(schematic)
  cols = len(schematic[0])

  # create a set of all numbers which are adjacent to parts where
  # each element is a tuple representing index (eg. (a, b))
  adj_to_parts = set()

  for x in range(rows):
    for y in range(cols):
      point = schematic[x][y]
      if point != BLANK and point.isdigit():
        if is_valid_part(schematic, rows, cols, x, y): adj_to_parts.add((x, y))

  # get sum of non-parts
  non_parts = []
  for x in range(rows):
    y = 0
    while y < cols:
      point = schematic[x][y]
      if point.isdigit():
        acc, good = [], True
        while point.isdigit() and y < cols:
          if (x, y) in adj_to_parts: good = False
          point = schematic[x][y]
          acc.append(point)
          y += 1
        if good: non_parts.append(acc)
      else:
        y += 1

  # get sum of everything
  everything = []
  for x in range(rows):
    y = 0
    while y < cols:
      point = schematic[x][y]
      if point.isdigit():
        acc = []
        while point.isdigit() and y < cols:
          point = schematic[x][y]
          acc.append(point)
          y += 1
        everything.append(acc)
      else:
        y += 1

  ans = 0
  for num in everything:
    if not num[-1].isdigit(): num.pop()
    ans += int("".join(num))
  for num in non_parts:
    if not num[-1].isdigit(): num.pop()
    ans -= int("".join(num))

  return ans

if __name__ == "__main__":
  print(solution())
