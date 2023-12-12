from pprint import pprint

def read_file(filename):
  buffer = []
  with open(filename) as f:
      line = f.readline()
      while line:
          buffer.append([c for c in line.strip()])
          line = f.readline()

  return buffer

def get_galaxy_coords(graph):
  coords = []
  for x in range(len(graph)):
    for y in range(len(graph[0])):
      if graph[x][y] == '#': coords.append([x, y])

  return coords

def expand_graph(graph):
  rows_to_expand, cols_to_expand = [], []
  for i, row in enumerate(graph):
    if all(elem == '.' for elem in row): rows_to_expand.append(i)

  for i in range(len(graph[0])):
    col = [graph[x][i] for x in range(len(graph))]
    if all(elem == '.' for elem in col): cols_to_expand.append(i)

  all_coords = get_galaxy_coords(graph)
  
  counter = 0
  # first shift rows
  for row in rows_to_expand:
    for i in range(len(all_coords)):
      if all_coords[i][0] > (row + counter):
        all_coords[i][0] += 1
    counter += 1

  counter = 0
  # then shift columns
  for col in cols_to_expand:
    for i in range(len(all_coords)):
      if all_coords[i][1] > (col + counter):
        all_coords[i][1] += 1
    counter += 1
        
  return all_coords

def solution(filename):
  graph = read_file(filename)
  coords = expand_graph(graph)
  
  ans = 0
  for i in range(len(coords)):
    for j in range(i+1, len(coords)):
      ans += abs(coords[j][0] - coords[i][0]) + abs(coords[j][1] - coords[i][1])
      
  return ans

if __name__ == "__main__":
  small = "input_small.txt"
  large = "input_large.txt"

  print(solution(small))
  print(solution(large))

  #9799681
