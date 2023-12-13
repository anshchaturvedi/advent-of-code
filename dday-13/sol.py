from pprint import pprint

def read_file(filename):
  buffer = []
  with open(filename) as f:
      line = f.readline()
      while line:
          buffer.append(line.strip())
          line = f.readline()

  acc, result = [], []
  for line in buffer:
    if line != '': acc.append(line)
    else:
      result.append(acc)
      acc = []

  result.append(acc)
  return result

def check_coords(coords, is_rows=False):
  for i in range(1, len(coords)):
    if coords[i-1] == coords[i]:
      top, bottom = i-1, i

      valid = True
      while top >= 0 and bottom < len(coords):
        if coords[top] != coords[bottom]: 
          valid = False
          break
        top -= 1
        bottom += 1

      if valid: 
        return 100 * i if is_rows else i

  return None

def solve(pattern):
  # first check rows
  row_coords = {}
  for r, row in enumerate(pattern):
    row_coords[r] = []
    for c, elem in enumerate(row):
      if elem == '#': row_coords[r].append(c)

  row_ans = check_coords(row_coords, True)
  if row_ans: return row_ans

  # check cols
  col_coords = {}
  for c in range(len(pattern[0])):
    col = [pattern[i][c] for i in range(len(pattern))]
    col_coords[c] = []
    for r, elem in enumerate(col):
      if elem == '#': col_coords[c].append(r)

  col_ans = check_coords(col_coords)
  if col_ans: return col_ans

  return "IF YOU GOT HERE SOMETHINGS BROKEN"

def solution(filename):
  patterns = read_file(filename)
  
  ans = 0
  for pattern in patterns:
    ans += solve(pattern)
  return ans

if __name__ == "__main__":
  small = "input_small.txt"
  large = "input_large.txt"

  print(solution(small))
  print(solution(large))
