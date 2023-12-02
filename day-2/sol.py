MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def read_file(filename):
  buffer = []
  with open(filename) as f:
      line = f.readline()
      while line:
          buffer.append(line.strip().split(' '))
          line = f.readline()

  return buffer

def process_lines(lines):
  processed = {}
  for line in lines:
    idx = int(line[1].strip(':'))
    processed_picks = " ".join(line[2:]).split(";")
    processed[idx] = processed_picks

  for game_id, picks in processed.items():
    processed[game_id] = [pick.strip() for pick in picks]
    processed[game_id] = [pick.split(';') for pick in picks]
    processed[game_id] = [pick.strip() for pick in picks]
    processed[game_id] = [pick.split(',') for pick in picks]

  return processed

def check_games(all_games):
  ans = 0

  for game_id, games in all_games.items():
    good = True
    for game in games:
      for pair in game:
        pair = pair.strip().split(' ')
        count, color = int(pair[0]), pair[1]
        if color == "red" and count > MAX_RED: good = False
        if color == "blue" and count > MAX_BLUE: good = False
        if color == "green" and count > MAX_GREEN: good = False

    if good: 
      ans += game_id

  return ans

def solution():
  lines = read_file('input_large.txt')
  games = process_lines(lines)
  ans = check_games(games)

  return ans

# ---------------- PART 2 ----------------
def check_games2(all_games):
  ans = 0

  for game_id, games in all_games.items():
    max_red = max_blue = max_green = float('-inf') 

    for game in games:
      for pair in game:
        pair = pair.strip().split(' ')
        count, color = int(pair[0]), pair[1]
        if color == "red": max_red = max(max_red, count)
        if color == "blue": max_blue = max(max_blue, count)
        if color == "green": max_green = max(max_green, count)

    ans += max_red * max_green * max_blue

  return ans

def solution2():
  lines = read_file('input_large.txt')
  games = process_lines(lines)
  ans = check_games2(games)

  return ans

if __name__ == "__main__":
  print(solution())
