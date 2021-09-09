import pandas as pd
import requests
import openpyxl
from bs4 import BeautifulSoup
import numpy as np

URL = "https://www.farmingdale.edu/courses/index.shtml"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='main-content')
#print(results.prettify())

course_names = results.find_all('h2', class_='course-name')
course_descriptions = results.find_all('div', class_='course-description')
course_levels = results.find_all('li', class_='course-level')
course_credits = results.find_all('li', class_='course-credits')

# for course_name in course_names:
#     print(course_name.text.strip())

# course_names.toFile('courses.csv', sep = ' ')

# for course_description in course_descriptions:
#     print(course_description, end='\n'*2)

cn = []
cd = []
#cl = []
cc = []

for _ in course_names:
    cn.append(_.text)

for _ in course_descriptions:
    cd.append(_.text)

# for _ in course_levels:
#     cl.append(_.text)

for _ in course_credits:
    cc.append(_.text)


# print(len(cn))
# print(len(cd))
# #print(len(cl))
# print(len(cc))


dh = []
dh.append([cn, cd, cc])

df = pd.DataFrame({'Course Names': cn, 'Course Descriptions': cd, 'Course Credits': cc})
df.to_excel(r'E:\course info.xlsx', index = False)

print(df)