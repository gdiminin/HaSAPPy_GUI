# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 08:04:13 2016

@author: GDM
"""
import re
         
def read_txt(informations,text):
    
    def get_TRUE(section,task,line,informations):    
        if not informations.has_key(section):
            informations[section] = {}
        if re.search('^\s*@\d[A-Z]\).*([YyNn]).*',line):
            value = re.findall ('^\s*@\d[A-Z]\).*([YyNn]).*',line)[0]
            if value.lower() == 'y':
                informations[section][task] = True
            else:
                informations[section][task] = False
        else:
            informations[section][task] = False
        return informations
        
    def get_NUMBER(section,task,line,informations):
        if not informations.has_key(section):
            informations[section] = {}
        if re.search ('^\s*@\d[A-Z]\)\D*([\d.]+)\D*',line):
            value = re.findall ('^\s*@\d[A-Z]\)\D*([\d.]+)\D*',line)[0]
            if value:
                informations[section][task] = float(value)
            else:
                informations[section][task] = 'n.d.'
        else:
             informations[section][task] = 'n.d.'
        return informations
    
    def get_STRING(section,task,line,informations):
        if not informations.has_key(section):
            informations[section] = {}
    
        string = re.findall ('^\s*@\d[A-Z]\)\s*(.*)',line)[0]
        if string:
            informations[section][task] = string
        else:
            informations[section][task] = 'n.d.'
        return informations
        
    def get_LIST(section,task,line,informations):
        if not informations.has_key(section):
            informations[section] = {}
        if not informations[section].has_key(task):
            informations[section][task] = []
        string = re.findall ('^\s*@\d[A-Z]\)\s*(.*)',line)[0]
        if string:
            informations[section][task].append(string)
        return informations
        
    def extract_line (section,task,line,informations,true=[],number=[],list_=[],string=[]):
        if task in number:
            informations = get_NUMBER(section,task,line,informations)    
        elif task in true:
            informations = get_TRUE(section,task,line,informations)
        elif task in list_:
            informations = get_LIST(section,task,line,informations)
        elif task in string:  
            informations = get_STRING(section,task,line,informations)
        return informations    
    
    hand = open(text,'rb')
    line_count = 0
    for line in hand:
        
        line_count +=1
        line = line.rstrip()
        
        find = re.findall('^\s*@(\d)([A-Z])\)',line)
        
        if find:
            section, task = find[0]
            section = int(section)


            if section == 0:
                informations = get_TRUE(section,task,line,informations)
                
            elif section == 1:
                informations = get_STRING(section,task,line,informations) 
            
            elif section == 2:
                informations = extract_line (section,task,line,informations,true =['B','K'],number =['A','H','J'],list_=['C','D','E'],string=['F','G'])
            
            elif section == 3:        
                informations = extract_line (section,task,line,informations,true =['B','D'],number =['C'],list_=['E','F','G'],string=['A'])
                            
            elif section == 4:        
                informations = extract_line (section,task,line,informations,true =['C','E'],number =['D'],list_=['F','G','H'],string=['A','B'])  
             
            elif section == 5:        
                informations = extract_line (section,task,line,informations,true =['B','C','F'],number =['A','D','E'],list_=['G','H'],string=[])  
        
            elif section == 6:        
                informations = extract_line (section,task,line,informations,true =['B','C','D','E','G'],number =['F'],list_=['H','I'],string=['A'])  
            
            elif section == 7:
                informations = extract_line (section,task,line,informations,true =['F','G','H','I','J','K','L','M','N','O','P'],number =['A','Q','R'],list_=['D','S','T'],string =['B'])  
                if task in ['C']:
                    if re.search('^\s*@\d[A-Z]\)\s*(\S+.*\S*)', line):
                        string = ','.join([n.lstrip().rstrip() for n in re.findall('^\s*@\d[A-Z]\)\s*(\S+.*\S*)', line)[0].split(',')])
                        informations[section][task] = string
                    else:
                        informations[section][task] = 'n.d.'
                        
                
                if task in ['E']:
                    if not informations[section].has_key(task):
                            informations[section][task] =[]
                    if re.search('^\s*@\d[A-Z]\)\s*(\S+.*\S*)', line):
                        string = ','.join([n.lstrip().rstrip() for n in re.findall('^\s*@\d[A-Z]\)\s*(\S+.*\S*)', line)[0].split(',')])
                        informations[section][task].append(string)
                    
            elif section == 8:
                informations = extract_line (section,task,line,informations,number = ['A'],list_=['B'],string =['E'])
                if task == 'C':
                    if not informations[section].has_key(task):
                        informations[section][task] =[]    
                    string = re.findall('(\(.*?\))',line)
                    informations[section][task].append(','.join(string))
                elif task == 'D':
                    if not informations[section].has_key(task):
                        informations[section][task] =[]
                    items = re.findall('(\[.*?\])',line)
                    informations[section][task].append(','.join(items))
        
            elif section == 9:
                informations = extract_line (section,task,line,informations,true =['A','B','E','G'],number =['F'],string=['C','D','H','I'])           
    
    return informations

        
       
       

                
                
                
            
            
            
