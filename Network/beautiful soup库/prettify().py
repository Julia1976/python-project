from bs4 import BeautifulSoup

label = "<html><body><p><data></p></body></html>"

soup = BeautifulSoup(label, 'html.parser')
print(soup.tile)