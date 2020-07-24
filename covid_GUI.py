
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