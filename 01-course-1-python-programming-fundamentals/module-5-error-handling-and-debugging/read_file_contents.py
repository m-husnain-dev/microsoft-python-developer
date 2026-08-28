def read_file_contents(file_path):
  try:
    with open(file_path, "r") as file:
      contents = file.read()
      print(contents)
  except FileNotFoundError:
    print(f"Error: File not found - {file_path}")