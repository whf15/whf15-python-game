# coding=utf-8

"""A Simple Crawler using wangzhe heros as seed
Author: Js
Python Version: 3.6+

Changes:
--------

"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pymysql
import pymysql.cursors
import logging.config
import os
from indexer import add_to_index
from pagerank import compute_ranks
import logging
import settings

logger = logging.getLogger("crawler")
logging.config.dictConfig(settings.LOGGING)
logger.setLevel(logging.DEBUG)

def seed_generator():
    with open('tasks\wangzhe.html', 'rb') as html_data:
        page_content = html_data.read()

    wangzhe_soup = BeautifulSoup(page_content, 'lxml')

    all_heros = [item['href']
                 for item in wangzhe_soup.findAll('a')
                 if 'href' in item.attrs and item['href'].startswith("http")]

    return all_heros


class SimpleCrawler(object):
    def __init__(self, seeds):
        self.seeds = seeds
        self.all_page_info =[]
        self.crawled = []
        self.graph = {}
        self.ranks = {}

    def union(self,p,q):
        """
        merge two data set togehter
        :param p:
        :param q:
        :return:
        """
        for e in q:
            if e not in p:
                p.append(e)

    def get_page(self,page_url):
        """
        based on the url, get the page information
        """
        try:
            if not page_url.startswith("http"):
                page_url = "http://" + page_url
            r = requests.get(page_url)
            if 'Content-Type' in r.headers and r.headers['Content-Type'] == 'text/html':
                return page_url, r.content
            else:
                return None,None
        except Exception as inst:
            return None,None

    def extract_information(self, page_url, page_content):
        """
        extract all the page information
        :param page_url:
        :param page_content:
        :return:
        """
        page_soup = BeautifulSoup(page_content, 'lxml')
        page_info = {}
        for script in page_soup(["script", "style"]):
            script.extract()

        try:
            page_info= {
                "url": page_url,
                "title":   page_soup.title.text.strip('\n') if page_soup.title else "" ,
                "image":   "http://"+page_soup.find('img')['src'],
                "content": page_soup.text.strip('\n')}
        except:
            page_info= {
                "url": page_url,
                "title": page_soup.title.text.strip('\n') if page_soup.title else "",
                "image": "",
                "content":page_soup.text.strip('\n')}
        return page_info

    def get_all_links(self, page):
        soup = BeautifulSoup(page, 'lxml')

        all_links = [item['href']
                     for item in soup.find_all('a')
                     if 'href' in item.attrs]
        if all_links:
            all_links = [link.strip("/") for link in all_links
                         if link.startswith("http") or link.startswith("//")]

            for link in all_links:
                parsed_url = urlparse(link)
                if parsed_url.path:
                    file_path, ext_name = os.path.splitext(parsed_url.path)
                    if ext_name in ('.mp4', '.avi', '.asf',
                                    '.mov', '.flv', '.pdf',
                                    '.mpg', '.mpeg', '.wmv',
                                    '.exe','.rar','.zip','.apk'):
                        all_links.remove(link)
                        logger.debug('skip file download ' + link)
            return all_links
        else:
            return None

    def crawl_web(self, max_depth):
        """

        :param max_depth: restrict by depth
        :return:
        """
        tocrawl = self.seeds
        next_depth = []
        depth = 0

        while tocrawl and depth <= max_depth:
            page_url = tocrawl.pop()
            logger.debug('crawling '+ page_url)
            if page_url not in self.crawled:
                get_url, page_content = self.get_page(page_url)
                if page_content:
                    page_info = self.extract_information(get_url, page_content)
                    all_links_onpage = self.get_all_links(page_content)
                    if all_links_onpage:
                        self.graph[page_url] = all_links_onpage
                        self.union(next_depth, all_links_onpage)
                    self.all_page_info.append([page_url, page_info])
                self.crawled.append(page_url)

            if not tocrawl:
                logger.debug('next round start')
                tocrawl, next_depth = next_depth, []
                depth = depth + 1

        return True

    def save_to_db(self):

        connection = pymysql.connect(host='localhost',
                                     user='seuser',
                                     password='se!@#$',
                                     db='dalsearch',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            for item in self.all_page_info:
                query_sql = \
                    'INSERT INTO document_page (url,title,image,description,pagecontent) ' \
                    'VALUES ("{}", "{}","{}","{}","{}");'.format(
                    item[1]['url'], item[1]['title'], item[1]['image'].strip('/'),
                    item[1]['content'][:140],item[1]['content'])
                connection.commit()
                sta = cursor.execute(query_sql)
        connection.close()

    def run(self):
       self.crawl_web(max_depth=2)
       self.ranks = compute_ranks(self.graph)
       logger.debug('rank built',self.ranks)
       self.save_to_db()


if __name__ == "__main__":
    seeds = seed_generator()
    logger.info('starting to crawl')

    new_crawler = SimpleCrawler(seeds)
    new_crawler.run()
    logger.info('finish crawl')
