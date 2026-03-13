from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import matplotlib.pyplot as plt
 
#   Url which contains data
url="https://tatamumbaimarathon.procam.in/results/race-results"

#   pass url to urlopen() to get html of page
html=urlopen(url)
print(type(html),html)

#   construct BeautifulSoup obj using the html
soup=bs(html,'lxml')

# Extract teh title of the Webpage
title=soup.title
print(title)
print(type(title))

# Extract the text of the webpage
text=soup.get_text()
print(soup.text,type(text))
print("\n \n")
# print(text,type(text)) #both are same res

#   Extract the useful html tags within the page
soup.find_all('a')

#   Print the hyperlinks
all_links=soup.find_all('a')
for link in all_links:
    print(link.get('href'))

#   Extract tabular data
rows=soup.find_all('tr')
print(rows)
print("\n")
print(type(rows))

#   Get all table rows in a list form and convert into a DF
for row in rows:
    row_td=row.find_all('td')
print(row_td)
print("\n\n")
print(type(row_td))

#   Extract the data without the html tags
str_cell=str(row_td)
cleantext=bs(str_cell, 'lxml').get_text()
print(cleantext)
print("\n\n")
print(type(cleantext))

#   Extract the Data without html tags using regex
list_row=[]
for row in rows:
    cells=row.find_all('td')
    str_cell=str(cells)
    clean=re.compile('<.*?>')
    clean_l=(re.sub(clean,'',str_cell))
    list_row.append(clean_l)
    print(list_row)

df=pd.DataFrame(list_row)
print(df.head(10))
