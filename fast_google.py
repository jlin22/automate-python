import os, bs4, requests, webbrowser

def search(search_term):
    res = requests.get('https://www.google.com/search?q=' + search_term)
    res.raise_for_status()
    elements = bs4.BeautifulSoup(res.text,features="html.parser")
    links = elements.select('.r a')
    for i in range(5):
        link = links[i].get('href')
        link = link[link.index('http'):]
        webbrowser.open(link)

search('python tutorials')

    
    
