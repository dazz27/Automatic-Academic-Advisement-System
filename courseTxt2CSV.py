import pandas as pd
import requests
import openpyxl
from bs4 import BeautifulSoup
import numpy as np
import re

# file_name = r"‪E:\genEdCourses.txt"
# file_name = file_name.lstrip('\u202a')

# read_file = pd.read_csv(file_name)

# f = open("E:\genEdCourses.txt", "r")
f = pd.read_csv(r'E:\genEdCourses.txt', header = None, error_bad_lines=False)
f.columns = ['Course Name']
f.to_csv (r'E:\courses.xlsx', index=None)
# print(f.read())

# results = pd.DataFrame(columns=('Category', 'Course Name'))

