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
  project_name = input("What is the name of your project\n")
  response = input(f"I have the name as {project_name} is this ok? Y for yes and N for No\n")
  if response.lower() == "y" or response.lower() == "yes":

#Grabs the parent folder and adds it to the project path
   parent_dir = os.path.join(os.getcwd(), os.pardir)
   project_path = os.path.join(parent_dir, project_name)

#checks if the project name is already the EXACT name of a folder
# if there isn't a new folder is made otherwise a quick kick back to the menu
   if not os.path.exists(project_path):
    os.mkdir(project_path)
    with open(f"{project_path}/main.py", 'w') as f:
        pass
    print(f"quick project file named {project_name} created")
   else:
    print("A folder with that name already exists back to the Menu")
  pass
