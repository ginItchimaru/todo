#!/usr/bin/env python3

file_path = ""

def change_list(list="list.txt"):
  global file_path
  file_path = list


def display_list(file_path):
  try:
      with open(file_path, "r") as list:
        lines = list.readlines()
      
        line_number = 0            
        for line in lines:
          line_number += 1
          print(f"{line_number}. {line.strip()}")
        
  except Exception as e:
      print("An error occurred:", e)
  

def write_list(file_path):

  while True:
      write_input = input(": ")

      if write_input in ["exit", "Exit", "EXIT"]:
        break

      else:
        with open(file_path, "a") as list:
          list.write(write_input + "\n")
          print(f"'{write_input}' has been added")


def delete_list(file_path):

  while True:
    delete_input = input(">> ")

    if delete_input in ["exit", "Exit", "EXIT"]:
      break

    elif delete_input in ["display", "Display", "DISPLAY"]:
      display_list(file_path)

    elif delete_input in ["clear", "Clear", "CLEAR"]:
      with open(file_path, "w") as list:
        pass
    
    else:
      try:
        line_to_remove = int(delete_input) - 1
      except ValueError:
        print("Input must be a valid number.")

      with open(file_path, "r") as list:
        lines = list.readlines()

      if 0 <= line_to_remove < len(lines):
        print(f"'{lines[line_to_remove]}' has been removed")
        del lines[line_to_remove]

        with open(file_path, "w") as list:
          list.writelines(lines)

      else:
        print("Line number is out of range.")


running = True
while running:
  usrinput = input("> ")
  change_list()

  if usrinput in ["i", "I", "info"]:
    print("To exit type 'exit'\n"
          "DISPLAY LIST:\n  'display' to display the todo list\n"
          "WRITE MODE:\n  Anything you enter here will be added to the todo list\n  'write' to enter Write Mode\n"
          "  'exit' to exit write mode\n"
          "DELETE MODE:\n  enter the number of the line you want to delete to delete it from the list\n"
          "  'delete' to enter Delete Mode\n  'display' to display the list in Delete Mode\n"
          "  'clear' to clear the whole list of its contents\n  'exit' to exit the Delete Mode")
    
  if usrinput in ["exit", "Exit", "EXIT"]:
    running = False

  if usrinput in ["display", "Display", "DISPLAY"]:
    display_list(file_path)

  if usrinput in ["write", "Write", "WRITE"]:
    print("You have entered write mode")
    write_list(file_path)
  
  if usrinput in ["delete", "Delete", "DELETE"]:
    print("You have entered delete mode")
    delete_list(file_path)