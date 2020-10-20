from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import xlwt

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.nike.com/in/w/new-tops-t-shirts-3n82yz9om13')

all_shirts = []
last_height = browser.execute_script("return document.body.scrollHeight")
while True:
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(5)
	new_height = browser.execute_script("return document.body.scrollHeight")
	all_hover_elements = browser.find_elements_by_css_selector(".product-card__body") 
	all_shirts = all_shirts + all_hover_elements
	if new_height == last_height:
		break
	last_height = new_height
	
rows=[[]]
print("Scrapping the data....")

for each_shirt in all_shirts:
	title_element = each_shirt.find_element_by_css_selector(".product-card__title")
	print(title_element.get_attribute("id"))
	id_element = each_shirt.find_element_by_css_selector(".product-card__link-overlay")
	print(id_element.get_attribute("href"))
	row=[]
	row.append(title_element.get_attribute("id"))
	row.append(id_element.get_attribute("href"))
	rows.append(row)
	

workbook = xlwt.Workbook()  
sheet = workbook.add_sheet("Products")
r = 0
c = 0
for i in rows:
	c=0
	for x in i:
		sheet.write(r, c, x)
		c = c + 1
		r = r + 1
		
workbook.save("nike.xls")
