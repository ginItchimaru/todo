#!/usr/bin/env python3

file_path = "list.txt"
list = open(file_path, "w")

running = True
while running:
    usrinput = input("> ")
    line_count = 0

    if usrinput in ["i", "I", "info"]:
      print("missing")
    
    if usrinput in ["exit", "Exit", "EXIT"]:
      running = False
    
    if usrinput in ["d", "D", "display", "Display"]:
      file = open(file_path, "r")

      for line in file:
        print(f"- {line.rstrip()}")
        line_count += 1
        print(line_count)
    
    if usrinput in ["W", "w", "write", "Write"]:
      print("You have entered write mode")

      while True:
        write_mode_input = input(": ")
        
        if write_mode_input in ["exit", "Exit", "EXIT"]:
          break
        
        else:
          list.write(write_mode_input + "\n")
          print(f"'{write_mode_input}' has been added")

