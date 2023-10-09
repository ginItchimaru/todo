#!/usr/bin/env python3

file_path = ""
list_was_changed = False

def change_list(list="list.txt"):
  global file_path
  file_path = str(list)


def choose_list():
  global list_was_changed
  global file_path

  while True:
    list_input = input(": ")

    if list_input in ["exit", "Exit", "EXIT"]:
      print("Exited.\n")
      break

    if list_input in ["file", "File", "FILE"]:
      print(f"Current file in use: '{file_path}'")

    else:
      if not list_input.endswith((".txt")):
        list_input += ".txt"

      try:
        with open(list_input, "a+") as file:
          pass
        
        list_was_changed = True
        change_list(list_input)
        print(f"File has been changed to: '{file_path}'")
        break

      except Exception as e:
        print("An error occurred:", e)
      


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
      print("Exited write mode.\n")
      break
    
    else:
      with open(file_path, "a") as list:
        list.write(write_input + "\n")
        print(f"'{write_input}' has been added.")


def delete_list(file_path):

  while True:
    delete_input = input(">> ")

    if delete_input in ["exit", "Exit", "EXIT"]:
      print("Exited delete mode.\n")
      break

    elif delete_input in ["display", "Display", "DISPLAY"]:
      print()
      display_list(file_path)
      print()

    elif delete_input in ["clear", "Clear", "CLEAR"]:
      with open(file_path, "w") as list:
        pass

    else:
      try:
        line_to_remove = int(delete_input) - 1
      except ValueError:
        print("Input must be a valid number.")
        print("Exited delete mode.\n")
        break

      with open(file_path, "r") as list:
        lines = list.readlines()

      if 0 <= line_to_remove < len(lines):
        print(f"'{lines[line_to_remove]}' has been removed.")
        del lines[line_to_remove]

        with open(file_path, "w") as list:
          list.writelines(lines)

      
      else:
        print("Line number is out of range.")


running = True
while running:
  usrinput = input("> ")

  if not list_was_changed:  
    change_list()
  
  if usrinput in ["i", "I", "info", "Info", "INFO"]:
      print("To exit type 'exit'\nTo see what file is being used, type 'file'\n"
          "DISPLAY LIST:\n  'display' to display the list\n"
          "WRITE MODE:\n  Anything you enter here will be added to the list\n  'write' to enter Write Mode\n"
          "  'exit' to exit write mode\n"
          "DELETE MODE:\n  enter the number of the line you want to delete to delete it from the list\n"
          "  'delete' to enter Delete Mode\n  'display' to display the list in Delete Mode\n"
          "  'clear' to clear the whole list of its contents\n  'exit' to exit the Delete Mode\n"
          "HOW TO CHANGE THE FILE:\n"
          "  Default file is the file list.txt.\n  'change' to change file thats being used for the list\n"
          "  'exit' to exit\n  'file' to see what file is currently in use")
  
  if usrinput in ["change", "Change", "CHANGE"]:
    print("Enter new file name to create or use an already existing file.\nOnly enter .txt files.")
    choose_list()
  
  if usrinput in ["file", "File", "FILE"]:
    print(f"Current file in use: '{file_path}'")

  if usrinput in ["exit", "Exit", "EXIT"]:
    running = False

  if usrinput in ["display", "Display", "DISPLAY"]:
    print()
    display_list(file_path)
    print()

  if usrinput in ["write", "Write", "WRITE"]:
    print("\nWrite Mode")
    write_list(file_path)
  
  if usrinput in ["delete", "Delete", "DELETE"]:
    print("\nEnter the number of the line you want to delete.\nDelete Mode")
    delete_list(file_path)
