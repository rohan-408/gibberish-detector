def unique_chars(input_string):
  unique_chars = set()
  unique_chars.update(input_string)  # getting number of unique characters in the input string
  try:
    percent =  (len(unique_chars)/len(input_string))*100  # Finding % of unique characters
  except:
    percent=0
  if percent < 73:  # If % of unique characters is less than 73%, then classify it as gibberish
    return 0
  else:
    return 1