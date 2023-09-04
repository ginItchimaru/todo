#!/usr/bin/env python3

file_path = "list.txt"
line_count = 0

def display_list(file_path):
  try:
      with open(file_path, "r") as list_read:
        lines = list_read.readlines()
            
        for line in lines:
          print(f"- {line.strip()}")
        
  except Exception as e:
      print("An error occurred:", e)
  
def write_list(file_path):

  while True:
      write_mode_input = input(": ")

      if write_mode_input in ["exit", "Exit", "EXIT"]:
        break

      else:
        with open(file_path, "a") as list_append:
          list_append.write(write_mode_input + "\n")
          print(f"'{write_mode_input}' has been added")


running = True
while running:
  usrinput = input("> ")

  if usrinput in ["i", "I", "info"]:
    print("missing")
    
  if usrinput in ["exit", "Exit", "EXIT"]:
    running = False

  if usrinput in ["d", "D", "display", "Display"]:
    display_list(file_path)

  if usrinput in ["W", "w", "write", "Write"]:
    print("You have entered write mode")
    write_list(file_path)