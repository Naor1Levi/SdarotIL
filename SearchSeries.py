# -*- coding: utf-8 -*-
import requests
from urllib.parse import urlparse
import os.path
#import VLCplayer
from bs4 import BeautifulSoup

class SearchSeries:

    def __init__(self, SidraName, SidraSeason, SidraEpisode):
        #Initiate VARs
        self.SidraName = SidraName
        self.SidraSeason = SidraSeason
        self.SidraEpisode = SidraEpisode
        self.WatchList = []
        self.DownList = []
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def generate_sections_of_url(self,url):
        path = urlparse(url).path
        sections = []; temp = "";
        while path != '/':
            temp = os.path.split(path)
            path = temp[0]
            sections.append(temp[1])
        return sections

    def get_soup(self, url):
        r = requests.get(url, headers=self.headers)
        return (BeautifulSoup(r.text, 'html.parser'))

    def Tvil(self):
        #Search SidraName in Tvil website
        soup = self.get_soup("http://www.tvil.me/?page=search&key=" + self.SidraName)
        k = soup.find(id='page-right')
        for link in k.find_all('a'):
            URL = link.get('href')

        #Modify the URL components
        path = self.generate_sections_of_url(URL)  #path[4] #Sidra ID
        if (len(path) < 5):
            self.WatchList = 0
            self.DownList = 0
            return None

        NewURL = "http://www.tvil.me/view/" + path[4] + "/"+self.SidraSeason + "/"+self.SidraEpisode + "/v/"+self.SidraName + ".html"
        soup = self.get_soup(NewURL)
        #Check if season/chapter exists
        WatchSoup = soup.find_all("div", class_="view-watch-button")
        DownSoup = soup.find_all("div", class_="view-download-button")
        if (len(WatchSoup) == 0 and len(DownSoup) == 0):
            self.WatchList = 0
            self.DownList = 0
            return None

        #Getting watching URLs from Tvil
        print ("")
        print ("-----------------------------")
        print ("----Direct Watching URL's----")
        print ("-----------------------------")

        for data in WatchSoup:
            for link in data.find_all('a'):
                try:
                    print(link.get('href').lstrip('\r\n'))
                    self.WatchList.append(link.get('href'))
                except AttributeError:
                    continue;

        #Getting download URLs from Tvil
        print ("")
        print ("----------------------")
        print ("----Download URL's----")
        print ("----------------------")

        for data in DownSoup:
            for link in data.find_all('a'):
                try:
                    print(link.get('href').lstrip('\r\n'))
                    self.DownList.append(link.get('href'))
                except AttributeError:
                    continue;

    def DoIt(self):
        self.Tvil()
        if (self.WatchList == 0 and self.DownList == 0):
            print ("")
            print ("*************** ERROR ****************")
            print ("-Make sure you wrote the Series Name correctly.")
            print ("-It's possible that the season is over and there are no more chapters/seasons.")
        return self.WatchList, self.DownList















