import os

current_path = os.getcwd()
print(f"The current directory is : {current_path}")

relative_path = "AnotherDirectory\\SubDirectory"
new_path = os.path.join(os.getcwd(), relative_path)
print(f"The new path is : {new_path}")
