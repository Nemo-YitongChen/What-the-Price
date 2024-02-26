import requests
from bs4 import BeautifulSoup

def scrape_coles_product_page(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    categories = [x.text.strip() for x in soup.findAll('span', itemprop='name')]
    name = [x.text.strip() for x in soup.findAll('h1', class_='LinesEllipsis product__title')]
    price = [x.text.strip() for x in soup.findAll('span', class_='price__value')]
    pprice = [x.text.strip() for x in soup.findAll('div', class_='price__calculation_method')]
    image_url = [x['src'] for x in soup.findAll('img', alt=name)]

    print("Categories: ", categories,
          "\n name : ", name, 
          "\n price: ", price, 
          "\n Price per gram: ", pprice,
          "\n Image Sources: ", image_url)

def scrape_coles_category_page(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    products = soup.findAll('section', attrs = {'data-testid': 'product-tile'})
    
    for product in products:
        image = product.find('img', attrs={'data-testid':"product-image"})
        image_url = image['src']
        # name = image['alt']
        # name = product.find('h2', class_='LinesEllipsis  product__title').text.strip()
        name = product.find('h2').text.strip()
        price = product.find('span', class_='price__value').text.strip()
        pprice = product.find('div', class_='price__calculation_method').text.strip()
        oprice_ = product.find('span', class_= 'price__was')
        if oprice_ != None:
            oprice = oprice_.text.split(' ')[-1].strip()
        
        print("\n\nname: ", name, 
              "\n price: ", price, 
              "\n Price per gram: ", pprice,
              "\n Original Price: ", oprice if oprice_ != None else price,
              "\n Image Sources: ", image_url
        )

# Call the function to start scraping
URL = 'https://www.coles.com.au/product/only-organic-strawberry-yoghurt-rice-cakes-30g-3772451'
# scrape_coles_product_page(URL)
URL = 'https://www.coles.com.au/browse/baby/baby-toddler-food/baby-toddler-snacks'
scrape_coles_category_page(URL)