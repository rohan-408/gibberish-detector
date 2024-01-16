def calculate_average_distance(input_string):
  input_string = input_string.lower()
  keyboard_layout = {
      'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4),
      'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4),
      'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3), 'b': (2, 4),
      ' ': (3, 0),
      'y': (0, 5), 'u': (0, 6), 'i': (0, 7), 'o': (0, 8), 'p': (0, 9),
      'h': (1, 5), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8),
      'n': (2, 5), 'm': (2, 6),
      'e': (3, 2), 'r': (3, 3),
      'w': (4, 1), 't': (4, 4),
      ' ': (3, 0)
  }
  def distance(char1, char2):
    if char1 in keyboard_layout and char2 in keyboard_layout:
        x1, y1 = keyboard_layout[char1]
        x2, y2 = keyboard_layout[char2]

        return abs(x1 - x2) + abs(y1 - y2)
    return float('inf')

  total_distance = 0
  num_pairs = 0
  midpoint_x, midpoint_y = None, None

  # Convert the input string to lowercase for case insensitivity
  input_string = input_string.lower()

  for i in range(len(input_string) - 1):
    char1 = input_string[i]
    char2 = input_string[i + 1]
    if midpoint_x is None or midpoint_y is None:
      midpoint_x, midpoint_y = keyboard_layout[char1]

    midpoint_distance = distance(char1, char2)
    total_distance += midpoint_distance
    num_pairs += 1
    midpoint_x, midpoint_y = (midpoint_x + keyboard_layout[char2][0]) / 2, (midpoint_y + keyboard_layout[char2][1]) / 2
  if num_pairs == 0:
    return 0  # Avoid division by zero

  average_distance = total_distance / num_pairs
  return average_distance