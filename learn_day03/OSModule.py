import os

path = "/RISHI/H2K/H2KProjects/SEDAP/CustomerWatchTime_04052021.csv"

if os.path.exists(path):
    print("THis File Exists")
else:
    print("You might need to create this file")

