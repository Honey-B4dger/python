import json
import matplotlib.pyplot as myplt 

# Explore the structure of the data.
filename = r'eq_data_1_day_m1.json'
#print (filename)
#filename = filename.replace('\\','/')
#print (filename)
with open(filename) as f:
    all_eq_data = json.load(f)
    

#print(type(all_eq_data))                                  # detect type of data from json file
                                                           # oh, it is a dictionary. 
#print(all_eq_data.keys())                                 # let's look at it's key entries.
#print(json.dumps(all_eq_data, indent=4, sort_keys=True))  # pretty print json data
#print(json.dumps(all_eq_data, indent=4))                  # pretty print json data


all_eq_dicts = all_eq_data['features']                    # enthält den key "Features", der die interesssierenden Daten enthält
#print(type(all_eq_dicts))                                # Alle Daten aus "Features" sind jetzt in all_eq_dicts.
print(all_eq_dicts[0].keys())
print(all_eq_dicts[0]['geometry']['coordinates'][0])

mags, plas, lons, lats = [], [], [], []              
for eq_dict in all_eq_dicts:                              # all_eq_dicts enthält Liste. Diese kann durchlaufen werden.
    mag = eq_dict['properties']['mag']                    # 
    pla = eq_dict['properties']['place']                  # 
    lon = eq_dict['geometry']['coordinates'][0]           # Ausgabe durch Angabe der passenden Keys und "subkeys". 
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    plas.append(pla)
    lons.append(lon)
    lats.append(lat)

print(mags[0:5])
print(plas[0:5])
print(lons[0:5])
print(lats[0:5])
#myplt.scatter(mags,lats,s=10)
# #myplt.scatter(mags,lats,marker="^",color="0.4",s=40,alpha=0.5)       # c= Graustufenwert  
# #myplt.scatter(mags,lats,marker="^",color=(0.4,0.7,0.9,1.0),s=40)     # color= RGBA-Wert 
# #myplt.scatter(mags,lats,marker="^",color='b',s=40,alpha=0.5)         # color= single letter
# #myplt.scatter(mags,lats,marker="^",color='teal',s=40,alpha=1.0)      # color= CSS Name
# #myplt.scatter(mags,lats,marker="^",color='tab:blue',s=40,alpha=0.5)  # color= Tableau palette
# #for i in range(len(lats)):
# #    print(lons[i],lats[i],mags[i])
mags[:]= [entry *20 for entry in mags]  # Multiply a List with a constant factor 
myplt.scatter(lons,lats,marker="o",color=(0.4,0.7,0.9,1.0),s = mags,label = "eqs magnitude",edgecolor="k")  # color= CN Farbzyklus ('C0-C9')
myplt.grid()   
myplt.legend()
myplt.xlabel("longitude")
myplt.ylabel("latitude")
myplt.tick_params(axis="both", which="major", labelsize=12)
myplt.tick_params(axis="both", which="minor", labelsize=10)
myplt.xticks()
myplt.yticks()
#myplt.show()
mng = myplt.get_current_fig_manager() 
mng.window.showMaximized()

myplt.show()
