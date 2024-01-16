def vowel_count(input_string):
  count = 0
  for i in [char for char in input_string]:
    if i in ['a','e','i','o','u']:
      count = count+1
  if count >2:  # If vowel count more than equal to 2, then classify it as non gibberish
    return 1
  else:
    return 0