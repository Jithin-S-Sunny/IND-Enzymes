# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:25:59 2020

@author: dell
"""
#To extract every enzyme saperately, use the example files given in the folder               
import pandas as pd
import glob
out1=open("lipaseout.txt","wt")
pd.set_option('max_colwidth',None)
for f in glob.glob("*.xls"):
        df=pd.read_excel(f)
        p=df[df['function'].str.contains("esterase")]
        for label, row in p.iterrows():
                x=label
                y=row
                print(x,y, file=out1)
    
x=open("lipaseout.txt","r")
z=open("only_seq.txt","wt")
y=["function","nucleotide_sequence","aa_sequence"]
for lines in x:
        for i in y:
                if i in lines:
                        print(lines.replace(" ",""), file=z)
                        