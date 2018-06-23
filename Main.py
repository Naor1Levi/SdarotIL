import sys
import SearchSeries

SidraName = input("Series Name: ")
SidraSeason = input ("Season: ")
SidraEpisode = input ("Episode: ")

k = SearchSeries.SearchSeries(SidraName, SidraSeason, SidraEpisode)
WatchList, DownList = k.DoIt()






