import requests
import pprint
import searches

searching = True

print("Welcome to Robert's TV show search program!")
print("Enter a show below to search: ")

while searching == True:
    method = input("Would you like to search by scheduled release date or name? ('date' or 'name'): ")
    if method == "date":
        print("<><>Make sure to enter your input in a yyyy-mm-dd format.<><>")
        print()
    search = input("Search: ")
    search = search.lower()
    print()
    
    if method == "name":
        searches.titlesearch(search)
    elif method == "date":
        searches.datesearch(search)
        
    ask = input("Would you like to continue searching? 'y/n':")
    if ask == "n":
        searching = False
    else:
        print()