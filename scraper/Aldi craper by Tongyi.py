# write a python script to analyse the tag structure of a website
import requests
from bs4 import BeautifulSoup

url = "https://www.aldi.com.au/groceries/price-reductions/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())
# get product name
product_names = soup.find_all("div", class_="box--description--header")
# print([x.text.strip() for x in product_names])
# get former price
former_prices = soup.find_all("span", class_="box--former-price")
# print([x.text.strip() for x in former_prices])
# get current price
current_prices = soup.find_all("span", class_="box--value")
current_decimal_prices = soup.find_all("span", class_="box--decimal")
# print([x.text.strip() for x in soup.find_all("span", class_="current_prices")])

# group the product names, former price, current price and print them in a role
p_func = lambda x,y,z,a: print('\nProduct :', x.text.strip(), 
       '\nFormer Price:', y.text.strip(),
       '\nCurrent Price:', z.text.strip(),'.', a.text.strip())
[ p_func(x,y,z,a) for x,y,z,a in zip(product_names,former_prices, current_prices,current_decimal_prices)]