import requests
import random
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def return_random_link(url):
    """
    Return random url link contained in url given

    Args:
        url
        sub_folder_name 
    """
    # Use requests to send a get request to the webpage
    response = requests.get(url)

    # Use BeautifulSoup to parse the webpage response
    soup = BeautifulSoup(response.text, 'html.parser')

    # get the urls from the hrefs in the achor tags
    links = [urljoin(url, link.get('href')) for link in soup.find_all('a') if link.get('href')]

    # Get all the links and chose one randomly
    link_list = []
    for link in links:
        link_list.append(link)
    link_chosen = random.choice(link_list)
    
    return link_chosen
