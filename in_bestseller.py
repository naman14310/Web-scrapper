from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

url1="https://www.amazon.in/gp/bestsellers/books/"
url2="https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_2?ie=UTF8&pg=2"
url_pg=urlopen(url1)
page=url_pg.read()
url_pg.close()
url_pg2=urlopen(url2)
page2=url_pg2.read()
url_pg2.close()

page_soup=soup(page,"html.parser")
books=page_soup.findAll("div",{"class":"a-section a-spacing-none aok-relative"})
page2_soup=soup(page2,"html.parser")
books2=page2_soup.findAll("div",{"class":"a-section a-spacing-none aok-relative"})

for book in books:
    try: 
        title=book.find("div", {"class" : "p13n-sc-truncate p13n-sc-line-clamp-1 p13n-sc-truncate-desktop-type2"}).string.strip()
    except AttributeError:
        title="Not Available"
        
    try:
        author=book.find("a",{"class" : "a-size-small a-link-child"}).string.strip()
    except AttributeError:
        author="Not Available"

    try:
        url = book.find("a",{"class":"a-link-normal"})['href']
    except AttributeError:
        url="Not Available"
    

    try:
        rating=book.find("a",{"class" : "a-size-small a-link-normal"}).string.strip()
    except AttributeError:
        rating="Not Available"

    try:
        avgrating=book.find("i",{"class" : "a-icon a-icon-star a-star-4 aok-align-top"}).string.strip()
    except AttributeError:
        avgrating="Not Available"
        
    try:
        price=book.find("span",{"class" : "p13n-sc-price"}).string.strip()
    except AttributeError:
        price="Not Available"
        
    try:
        rating=book.find("a",{"class" : "a-size-small a-link-normal"}).string.strip()
    except AttributeError:
        rating="Not Available"
    
    out=open("in_book.csv",'a')
    out.write(str(title)+";"+str(url)+";"+str(author)+";"+str(price)+";"+str(rating)+";"+str(avgrating))
    out.write("\n")

for book in books2:
    try: 
        title=book.find("div", {"class" : "p13n-sc-truncate p13n-sc-line-clamp-1 p13n-sc-truncate-desktop-type2"}).string.strip()
    except AttributeError:
        title="Not Available"
        
    try:
        price=book.find("span",{"class" : "p13n-sc-price"}).string.strip()
    except AttributeError:
        price="Not Available"
        
    try:
        author=book.find("a",{"class" : "a-size-small a-link-child"}).string.strip()
    except AttributeError:
        author="Not Available"

    try:
        rating=book.find("a",{"class" : "a-size-small a-link-normal"}).string.strip()
    except AttributeError:
        rating="Not Available"        

    try:
        url = book.find("a",{"class":"a-link-normal"})['href']
    except AttributeError:
        url="Not Available"

    try:
        rating=book.find("a",{"class" : "a-size-small a-link-normal"}).string.strip()
    except AttributeError:
        rating="Not Available"
        
    try:
        avgrating=book.find("i",{"class" : "a-icon a-icon-star a-star-4 aok-align-top"}).string.strip()
    except AttributeError:
        avgrating="Not Available"
    
    out=open("in_book.csv",'a')
    out.write(str(title)+";"+str(url)+";"+str(author)+";"+str(price)+";"+str(rating)+";"+str(avgrating))
    out.write("\n")




