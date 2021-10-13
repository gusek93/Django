import os
import shutil

file_path = os.path.abspath("../media/employeeList/")
# shutil.rmtree(file_path)

file_name = os.path.basename("../media/employeeList/*")

# os.remove(file_path)
os.mkdir(file_path)
