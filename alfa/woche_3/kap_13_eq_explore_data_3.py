import json
import matplotlib.pyplot as myplt 

# Explore the structure of the data.
filename = '../data/eq_data_1_day_m1.json'
with open(filename) as f:                        # Read JSON Dataset
    all_eq_data = json.load(f)
#print("The following keys are available in the current dataset: ")
#for key in all_eq_data:                          # Investigate JSON structure
#    print(key)
all_eq_dicts = all_eq_data['features']           # Investigate JSON structure: stepping deeper 
#print("The following keys are available under the selected key: ")
#for all_key in all_eq_dicts:                    # Investigate important entities  
#    print(all_key)                              # We notice, that keys contain more keys
#    print("all_key[properties]")                # and notice, which keys contain the interesting entries
#    print(all_key["properties"])                # and notice, which keys contain the interesting entries
#    print("all_key[geometry]")
#    print(all_key["geometry"])
#    print(all_key["properties"]["mag"])
#    print(all_key["geometry"]["coordinates"])

mags, plas, lons, lats = [], [], [], []
#print(all_eq_dicts)
for eq_dict in all_eq_dicts:                     # extract values from determined entities
    mag = eq_dict['properties']['mag']
    pla = eq_dict['properties']['place']
    lon = eq_dict['geometry']['coordinates'][0]  # extracted values may be lists with more than one entry
    lat = eq_dict['geometry']['coordinates'][1]  # here we address the second list entry
    mags.append(mag)                             # and add it to the prepared list
    plas.append(pla)
    lons.append(lon)
    lats.append(lat)

#  myplt.scatter(mags,lats,marker="^",c="0.1",s=40,alpha=0.5) # c= Graustufenwert  
#myplt.scatter(mags,lats,marker="^",color=(0.4,0.7,0.9,0.5),s=40,alpha=0.5)  # color= RGBA-Wert 
#myplt.scatter(mags,lats,marker="^",color='b',s=40,alpha=0.5)  # color= single letter
#myplt.scatter(mags,lats,marker="^",color='teal',s=40,alpha=0.5)  # color= CSS Name
#myplt.scatter(mags,lats,marker="^",color='tab:blue',s=40,alpha=0.5)  # color= Tableau palette
#myplt.scatter(mags,lats,marker="^",color='C0',s=40,alpha=0.5)  # color= CN Farbzyklus ('C0-C9')
                                              # Matplotlib "Scatterplot" plots only points. 
                                              # The x- and y-values are the lists "mags" and "lats". 
                                              # c=colour argument, see "Anhang A.pdf".  
                                              # S is the plot blob "Area". To double the size, we have to 
                                              # increase s by 4.  
#myplt.scatter(mags,lats,c=(0,0,0),s=100)     # c=color can also be RGB or RGBA values in [0,1] like (0.1,0.2,0.3) or (0.1,0.2,0.3,0.5).
                                              # same in hex values: #0f0f0f80
                                              # single value as string for gray level "0.1"
                                              # single key letter from {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}
                                              # X11/CSS4 color name (case-insensitive)
                                              # (omitted) a name from the xkcd color survey, prefixed with 'xkcd:' (e.g., 'xkcd:sky blue'; case insensitive)
                                              # a Tableau color like {'tab:blue', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink'} (case-insensitive)
                                              # a "CN" color spec, i.e. 'C' followed by a number, which is an index into the default property cycle 
                                              # see "Matplotlib doku: specifying colours"  
#print(len(lats),len(lons),len(mags))
for i in range(len(lats)):
    print(lons[i],lats[i],mags[i])
smags = [entry *40 for entry in mags]       # Multiply a List with a constant factor (for a new list) 
#mags[:]= [entry *10 for entry in mags]     # Multiply a List with a constant factor (in-place)

scpl = myplt.scatter(lons, lats, marker="o", color="C1", s = smags, alpha=1.0,label="eqs magnitude", edgecolors = "k",zorder = 1)  # color= RGBA-Wert 
                                            # edgecolors = "k" liefert schwarzen Rand um Marker
for i,txt in enumerate(mags): 
#    print (i,txt,lons[i])
    myplt.annotate(txt,xy=(lons[i],lats[i]),ha="left",va="bottom",
    textcoords="offset points",xytext=(4, 4),clip_on=False, zorder = 2, fontsize =12)
                                            # myplt.annotate( label,  
                                            #                 (x,y),
                                            # textcoords = "offset points",
                                            # xytext(0,10) distance from text to points
                                            # ha="center", horizontal alignment can be "center", "left", "right"
                                            # va="center", vertical alignment can be "center", "bottom", "top"
myplt.grid()                                  
myplt.xlim(-180,180)
myplt.ylim(-90,90)
myplt.xticks(rotation = 20)
myplt.yticks(rotation = 90)
myplt.xlabel("longitude")
myplt.ylabel("latitide")
myplt.legend()
mng = myplt.get_current_fig_manager()
#mng.window.showMaximized()
myplt.show()                                  # Create visible plot window (Navigation Toolbar will appear automatically)
