import requests
from bs4 import BeautifulSoup as bss4
URL=requests.get("https://www.amazon.eg/-/en/s?k=lipstick&crid=31IP6JI0NIWK2&qid=1671302382&sprefix=li%2Caps%2C608&ref=sr_pg_1")

soup = bss4(URL.text,'lxml')
lipstick_Description=[]
lipstick_price=[]
lipstick_review=[]
shipping_expenses=[]



lipstick_file=soup.findAll("div",{"class":"s-matching-dir sg-col-16-of-20 sg-col sg-col-8-of-12 sg-col-12-of-16"})
#print(lipstick_file)
lipstick_Description=soup.findAll("span",{"class":"a-size-base-plus a-color-base a-text-normal"})
#print(lipstick_Description)

lipstick_price=soup.findAll("span",{"class":"a-price-whole"})
#print(lipstick_price)

lipstick_review=soup.findAll("div",{"class":"a-row a-size-small"})
#print(lipstick_review)

shipping_expenses=soup.findAll("span",{"class":"a-color-base"})
#print(shipping_expenses)
for x in range(46):
    print("lipstick_Description ")
    print(lipstick_Description[x].text, "\n")
    print("lipstick_price  ")
    print(lipstick_price[x].text, "\n")
    print("lipstick_review ")
    print(lipstick_review[x].text, "\n")
    print(shipping_expenses[x].text, "\n")


'''


import bs4
import requests
from bs4 import BeautifulSoup as bss4
URL=requests.get("https://www.amazon.eg/-/en/s?k=lipstick&crid=31IP6JI0NIWK2&qid=1671302382&sprefix=li%2Caps%2C608&ref=sr_pg_1")
#print(URL.text)

#soup = bss4(URL.text,'lxml')
soup=bs4.BeautifulSoup(URL.content,"html.parser")
Description=[]
price=[]
review=[]
expenses=[]

page_number=1
for x in range(1,9):
    page_number=page_number+1
    URL="https://www.amazon.eg/-/en/s?k=lipstick&crid=31IP6JI0NIWK2&qid=1671302382&sprefix=li%2Caps%2C608&ref=sr_pg_1"
    URL= URL + str(page_number)


lipstick_file=soup.findAll("div",{"class":"s-matching-dir sg-col-16-of-20 sg-col sg-col-8-of-12 sg-col-12-of-16"})
#print(lipstick_file)
lipstick_Description=soup.findAll("h2",{"class":"a-size-mini a-spacing-none a-color-base s-line-clamp-4"})
#print(lipstick_Description)

lipstick_price=soup.findAll("span",{"class":"a-price-whole"})
#print(lipstick_price)

lipstick_review=soup.findAll("span",{"class":"a-size-base"})
#print(lipstick_review)`                                                1   `

shipping_expenses=soup.findAll("span",{"class":"a-color-base"})
#print(shipping_expenses)
for y in range(len(lipstick_Description)):
    Description.append(lipstick_Description[y].text)
    print(lipstick_Description,"/n")

for y in range(len(lipstick_price)):
     price.append(lipstick_price[y].text)
     print(lipstick_price,"/n")

for y in range(len(lipstick_review)):
    review.append(lipstick_review[y].text)
    print(lipstick_review, "/n")

for y in range(len(shipping_expenses)):
    expenses.append(shipping_expenses[y].text)
    print(shipping_expenses, "/n")
print(y)
'''


















