
# importing tkinter
from tkinter import *

# initializing tkinter
root = Tk()

# setting geometry
root.geometry("350x350")

# setting title
root.title("Get Covid-19 Data Country Wise")

# function which will get covid data and will show it
def showdata():
    # importing matplotlib which will be used to show data graphically
    from matplotlib import pyplot as plt
    # to scale the data we are importing patches
    import matplotlib.patches as mpatches
    # importing covid library
    from covid import Covid
    # initializing covid library
    covid = Covid()
    # declaring empty lists to store different data sets
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []
    # using try and except to run program without errors

    try:
         # updating root
        root.update()
        # getting countries names entered by the user
        countries = data.get()
        # removing white spaces from the start and end of the string
        country_names = countries.strip()
        # replacing white spaces with commas inside the string
        country_names = country_names.replace(" ", ",")
        # splitting the string to store names of countries
        # as a list 
        country_names = country_names.split(",")
        # for loop to get all countries data
        for x in country_names:
            # appending countries data one-by-one in cases list 
            # here, the data will be stored as a dictionary
            # for one country i.e. for each country
            # there will be one dictionary in the list
            # which will contain the whole information
            # of that country
            cases.append(covid.get_status_by_country_name(x))
            # updating the root
            root.update()
        # for loop to get one country data stored as dict in list cases
        for y in cases:
            # storing every Country's confirmed cases in the confirmed list
            confirmed.append(y["confirmed"])
            # storing every Country's active cases in the active list
            active.append(y["active"])
            # storing every Country's deaths cases in the deaths list
            deaths.append(y["deaths"])
            # storing every Country's recovered cases in the recovered list
            recovered.append(y["recovered"])
        # marking the color information on scaleusing patches
        confirmed_patch = mpatches.Patch(color='green', label='confirmed')
        recovered_patch = mpatches.Patch(color='red', label='recovered')
        active_patch = mpatches.Patch(color='blue', label='active')
        deaths_patch = mpatches.Patch(color='black', label='deaths')
        # plotting the scale on graph using legend()