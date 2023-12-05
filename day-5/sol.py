from pprint import pprint

def read_file(filename):
  buffer = []
  with open(filename) as f:
      line = f.readline()
      while line:
          buffer.append(line.strip())
          line = f.readline()

  acc, result = [], [buffer[0]]

  for i in range(2, len(buffer)):
    if buffer[i] == '':
      result.append(acc)
      acc = []
    else: acc.append(buffer[i])

  # append final acc
  result.append(acc)
  return result

def generate_maps(lines):
  seeds = list(map(lambda x: int(x), lines[0].split()[1:]))

  info = {}
  for i in range(1, len(lines)):
    line = lines[i]
    name = line[0].split()[0]
    line_info = {}

    for j in range(1, len(line)):
      data = list(map(lambda x: int(x), line[j].split()))
      dest, start, rnge = data[0], data[1], data[2]
      line_info[start] = (dest, rnge)

    info[name] = line_info

  return seeds, info

keys = [
  'seed-to-soil', 
  'soil-to-fertilizer', 
  'fertilizer-to-water', 
  'water-to-light', 
  'light-to-temperature', 
  'temperature-to-humidity', 
  'humidity-to-location'
]

def get_map_val(mymap, mapping, key):
  lines = mymap[mapping]
  val = None
  for start, rest in lines.items():
    dest, rnge = rest
    if start <= key and key <= (start + rnge - 1):
      val = dest + (key - start)
      return val

  return key if val is None else val

def solution(filename):
  lines = read_file(filename)
  seeds, info = generate_maps(lines)

  mini = float('inf')
  for seed in seeds:
    cur_val = seed
    for key in keys:
      cur_val = get_map_val(info, key, cur_val)
    mini = min(mini, cur_val)

  return mini

def solution2(filename):
  lines = read_file(filename)
  seeds, info = generate_maps(lines)

  mini = float('inf')
  seen = {}

  for seed in range(1500000000):
    if seed in seen:
      mini = min(mini, seen[seed])

  # for i in range(0, len(seeds), 2):
  #   start_seed, end_seed = seeds[i], seeds[i] + seeds[i + 1]
  #   for seed in range(start_seed, end_seed):
  #     if seed in seen:
  #       mini = min(mini, seen[seed])
  #     else:
  #       cur_val = seed
  #       for key in keys: cur_val = get_map_val(info, key, cur_val)
  #       seen[seed] = cur_val
  #       mini = min(mini, cur_val)

    # print("got through bunch")

  return mini

if __name__ == "__main__":
  filename1 = "input_small.txt"
  filename2 = "input_large.txt"
  print(solution2(filename1))
  # print(solution2(filename2))
