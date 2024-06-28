'''
the process will be a quick code menu - no gui - where the user for now will be able to load up a quick project
 or custom make own with variables such as a project folder name a main file name (default main.py)
  maybe  links into my py template project
  code first then gui
  shouldn't take more than a day
'''
import os

while True:
 print("Main Menu")
 print("1. Create quick project")
 reaction = int(input("Choose an option by number\n"))

 if reaction == 1:
  project_name = input("What is the name of your project")
  response = input(f"I have the name as {project_name} is this ok? Y for yes and N for No")
  if response.lower() == "y" or response.lower() == "yes":

   if not os.path.exists(project_name):
    os.mkdir(project_name)
    with open(f"{project_name}/main.py", 'w') as f:
        pass
    print(f"quick project file named {project_name} created")

  pass
