import sys
import SearchSeries
sys.path.append('/usr/lib/python3/dist-packages')

SidraName = input("Series Name: ")
SidraSeason = input ("Season: ")
SidraEpisode = input ("Episode: ")

k = SearchSeries.SearchSeries(SidraName, SidraSeason, SidraEpisode)
WatchList, DownList = k.DoIt()





