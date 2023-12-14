from pprint import pprint

def read_file(filename):
  return [list(line) for line in [line.strip() for line in open(filename)]]

def solution(filename):
  platform = read_file(filename)
  rows, cols = len(platform), len(platform[0])
  i = 1000 # why does this number work?!

  for _ in range(i):
    # north
    for c in range(cols):
      r = 0
      while r < rows:
        if platform[r][c] == 'O':
          up, cur = r - 1, r
          while up >= 0:
            if platform[cur][c] == 'O' and platform[up][c] == '.':
              platform[cur][c], platform[up][c] = platform[up][c], platform[cur][c]
            up -= 1
            cur -= 1
        r += 1

    # west
    for r in range(rows):
      c = 0
      while c < cols:
        if platform[r][c] == 'O':
          left, cur = c - 1, c
          while left >= 0:
            if platform[r][cur] == 'O' and platform[r][left] == '.':
              platform[r][cur], platform[r][left] = platform[r][left], platform[r][cur]
            left -= 1
            cur -= 1
        c += 1

    # south
    for c in range(cols):
      r = rows - 1
      while r >= 0:
        if platform[r][c] == 'O':
          down, cur = r + 1, r
          while down < rows:
            if platform[cur][c] == 'O' and platform[down][c] == '.':
              platform[cur][c], platform[down][c] = platform[down][c], platform[cur][c]
            down += 1
            cur += 1
        r -= 1

    # east
    for r in range(rows):
      c = cols - 1
      while c >= 0:
        if platform[r][c] == 'O':
          right, cur = c + 1, c
          while right < cols:
            if platform[r][cur] == 'O' and platform[r][right] == '.':
              platform[r][cur], platform[r][right] = platform[r][right], platform[r][cur]
            right += 1
            cur += 1
        c -= 1
    
  ans = 0
  for r, row in enumerate(platform):
    for elem in row:
      if elem == 'O': ans += rows - r
  return ans, i

if __name__ == "__main__":
  small = "input_small.txt"
  large = "input_large.txt"

  print(solution(small))
  print(solution(large))
