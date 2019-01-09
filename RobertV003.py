#Robert V 0.03

#This script takes a shapefile with a collumn that contains a list of feature classes and adds them to a map document. Now with GUI!
#by Rachel Joseph

#Start: 1/3/2019
#Last Update: 1/9/2019

print("Starting Program")

import arcpy
import tkinter as tk


def clearTheField():
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)

def runThe5KWeCallLife():
    #parameters
    workspace = arcpy.env.workspace = e1.get() #gdb or folder holding feature classes or shapefiles
    mapdoc = e2.get() #map document to view data

    fileList = arcpy.ListFeatureClasses()

    #Set up map document
    mxd = arcpy.mapping.MapDocument(mapdoc)
    df = arcpy.mapping.ListDataFrames(mxd, "*")[0] #may also want to use (df = mxd.activeDataFrame)
    text.insert(tk.INSERT, "Dataframe Found\n")

    fcCount = 1

    for shape in fileList:
        featureClass = "{}\{}".format(workspace, shape)
        newLayer = arcpy.mapping.Layer(featureClass)
        arcpy.mapping.AddLayer(df, newLayer, "BOTTOM")
        text.insert(tk.INSERT, "Feature class number {} added to the data frame\n".format(fcCount))
        fcCount += 1

    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()
    text.insert(tk.INSERT, "View Refreshed\n")

    df.zoomToSelectedFeatures()
    text.insert(tk.INSERT, "Zoomed to Layer\n")

    mxd.save()

    del mxd

    text.insert(tk.INSERT, "Feature Classes added to the following map document: {}\n".format(mapdoc))
    text.insert(tk.INSERT, "Program Completed")

#GUI
master = tk.Tk()
master.title("Robert V 0.03")

tk.Label(master, text="Welcome to Robert. Your Shapefile/Feature Class showing assistant.", font=("System", 14)).grid(row=0)

tk.Label(master, text="Gdb or Folder containing the Feature Classes you want to view:").grid(row=2)
tk.Label(master, text="Path to map document you want to view the feature classes on: ").grid(row=3)

e1 = tk.Entry(master, width=120)
e2 = tk.Entry(master, width=120)

e1.grid(row=2, column=1)
e2.grid(row=3, column=1)

tk.Button(master, text='Run', command=runThe5KWeCallLife).grid(row=7, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Clear', command=clearTheField).grid(row=7, column=1, sticky=tk.W, pady=4)

text = tk.Text(master)
text.grid(row=8)
text.insert(tk.INSERT, "Fill Out Parameters Above Then Hit Run Button To Start Program")

master.mainloop()

