import requests
import pp

def printsearches(showlist):
    for show in showlist:
        print("Show: " + show["show"]["name"])
        summary = show["show"]["summary"]
        summary = summary.replace("<p>", "")
        summary = summary.replace("</p>", "")
        print("Summary: " + summary)
        print("Rating: " + str(show["show"]["rating"]["average"]))
        print()

def titlesearch(search):
    response = requests.get("http://api.tvmaze.com/search/shows?q=" + search)
    showlist = response.json()
    if showlist == []:
        print("Error: No shows available")
        print()
    else:
        printsearches(showlist)
    
def datesearch(search):
    response = requests.get("https://api.tvmaze.com/schedule?country=US&date=" + search)
    showlist = response.json()
    if showlist == []:
        print("Error: No shows available")
        print()
    else:
        printsearches(showlist)