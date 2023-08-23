#!/usr/bin/env python3

list = open("list.txt", "w")

running = True
while running:
    usrinput = input("> ")

    if usrinput in ["i", "I", "info"]:
      print("missing")
    
    if usrinput in ["exit", "Exit", "EXIT"]:
      running = False
    
    if usrinput in ["W", "w", "write", "Write"]:
      print("You have entered write mode")

      while True:
        write_mode_input = input(": ")
        
        if write_mode_input in ["exit", "Exit", "EXIT"]:
          break
        
        else:
          list.write(write_mode_input + "\n")
          print(f"'{write_mode_input}' has been added")

