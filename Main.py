import sys
import SearchSeries

SidraName  = input("Series N ame: ")
SidraSeason = input ("Season: ")
SidraEpisode = input ("Episode: ")

k = SearchSeries.SearchSeries(SidraName, SidraSeason, SidraEpisode)
WatchList, DownList = k.DoIt()






