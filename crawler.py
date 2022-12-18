import sys
import json
import requests
import validators
from bs4 import BeautifulSoup
from collections import defaultdict


class Crawler:
    def __init__(self, start_url, max_depth):
        self.start_url = start_url
        self.max_depth = max_depth

        self.images = []

        self.url_depth_map = defaultdict(list)
        self.url_depth_map[0].append(self.start_url)

        self.visited = {}

    def crawl(self):
        depth = 0
        while depth<= self.max_depth and self.url_depth_map[depth]:
            for url in self.url_depth_map[depth]:
                print(f"Crawling Request Received for {url}")
                if self.visited.get(url) or not self.validate_crawl_request(url, depth):
                    continue
                self.visited[url] = True
                try:
                    soup = self.get_url_soup_object(url)
                    if isinstance(soup, BeautifulSoup):
                        self.images += self.extract_images(soup, url, depth)
                        if depth< self.max_depth:
                            self.url_depth_map[depth+1]+=self.extract_urls(soup, url)
                except Exception as e:
                    print(f"Error while crawling url {url}: {e}")
            depth+=1

    def extract_urls(self, soup, url):
        urls = []
        for link in soup.find_all('a'):
            if not link.get('href'):
                continue
            if validators.url(link.get('href')):
                urls.append(link.get('href'))
            else:
                if link.get('href').startswith('/'): 
                    urls.append(url+link.get('href'))
                else:
                    urls.append(url + '/' + link.get('href'))
        return urls

    def extract_images(self, soup, url, depth):
        return [{ "imageUrl": link.get('src'), "sourceUrl": url, "depth":depth} for link in soup.find_all('img')]

    def get_url_soup_object(self, url):
        soup = None
        r = requests.get(url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    def validate_crawl_request(self, url, depth):
        if not url or not validators.url(url):
            print(f"Invalid url {url} provided for crawling")
            return False
        if depth > self.max_depth:
            print(f"Maximum crawling depth reached")
            return False
        return True

def validate_arguments(arguments):
    start_url, max_depth = None, None
    if len(arguments)<3 \
            or not validators.url(arguments[1]) \
            or not arguments[2].isdigit() \
            or int(arguments[2])<0 \
            or int(arguments[2])>100:
        print("Invalid Crawling Request Received")
        return start_url, max_depth
    start_url, max_depth = arguments[1], int(arguments[2])
    return start_url, max_depth
    
if __name__ == "__main__":
    start_url, max_depth = validate_arguments(sys.argv)
    if start_url and max_depth:
        crawler = Crawler(start_url, max_depth)
        crawler.crawl()
        # print(crawler.url_depth_map)
        data = {
            "results": crawler.images
        }
        with open('results.json', 'w') as f:
            json.dump(data, f, indent=2)


