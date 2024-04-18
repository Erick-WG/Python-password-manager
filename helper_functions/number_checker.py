def is_number(user_input):
  """Checks if the input string is a number (integer or float)."""
  try:
    # Try converting to float first for wider range of numbers
    float(user_input)
    return True
  except ValueError:
    pass
  try:
    int(user_input)
    return True
  except ValueError:
    return False

# # Get user input
# user_input = input("Enter a number: ")

# # Check if it's a number
# if is_number(user_input):
#   print("The input is a number.")
# else:
#   print("The input is not a number.")
