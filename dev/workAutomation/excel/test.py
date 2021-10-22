import os
import glob

#file_path = os.listdir('../media/result')

file_path = glob.glob('../media/result/*')
list_excel = [file for file in file_path if file.endswith(".xlsx")]

print(list_excel[0])