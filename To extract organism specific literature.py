# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:30:14 2020

@author: jithin
"""

#The following python script was used to extract PubMed id’s and parse the output JSON files to identify organism with thermophilic or psychrophilic nature


#to extract from pubmed

from Bio import Entrez 
import xmltodict 
import pandas as pd 
import csv
file1=open("trail1.txt","wt") 
Entrez.email="XXXXXXXXXXX@gmail.com" db="PubMed"
paramEutils={'usehistory':'Y'} 
df=pd.read_csv("ex.csv") 
for i in df.index:
        x=df["species"][i]
        eSearch=Entrez.esearch(db=db, term= x, **paramEutils) 
        res=Entrez.read(eSearch)
        print(res, file=file1)


#to parse into

import json 
f=open("trail.json") 
data=json.load(f) 
print(data["IdList"]) 
print(data["TranslationSet"]) 
print(data["TranslationStack"])

#to loop it over all the results

import json 
f=open("psychroCGCB.json")
compost=open("psychroCGCBresult.txt","wt") 
data=json.load(f)
print(data) 
for i in data:
        a=(i["IdList"]) 
        b=(i["TranslationStack"]) 
        print(a,b, file=compost)



#Python script for network generation using nodes (node size: species count) and edges(species to Thermophilic/Psychrophilic as target)
import networkx as nx
import matplotlib.pyplot as plt 
import pandas as pd
import warnings 
warnings.filterwarnings('ignore') 
G=nx.Graph(day="Stackoverflow") 
df_nodes=pd.read_csv("nodes.csv") 
df_edges=pd.read_csv("edges.csv") 
for index, row in df_nodes.iterrows():
        G.add_node(row['name'], group=row['group'], nodesize=row['nodesize']) 
        for index, row in df_edges.iterrows():
                G.add_weighted_edges_from([(row['source'], row['target'], row['value'])]) color_map = {1:'#e64f4f', 2:'#dc1f1f', 3:'#134262', 4:'#72BCEE', 5:'#629fff', 6:'#bcc2f2',
                7:'#eebcbc', 8:'#f1f0c0', 9:'#d2ffe7', 10:'#caf3a6', 11:'#ffdf55', 12:'#ef77aa', 13:'#d6dcff', 14:'#d2f5f0'}
plt.figure(figsize=(25,25)) 
options = {
'edge_color': '#FFDEA2', 
'width': 1,
'with_labels': True,
'font_weight': 'regular', 
'font_size': 7,
}
colors = [color_map[G.nodes[nodes]['group']] for nodes in G] 
sizes = [G.nodes[nodes]['nodesize']*10 for nodes in G]
nx.draw(G, node_color=colors, node_size=sizes, pos=nx.spring_layout(G, k=0.25, iterations=50),
**options) 
ax = plt.gca()
ax.collections[0].set_edgecolor("#555555") 
plt.show()
