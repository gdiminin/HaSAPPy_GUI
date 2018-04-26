#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 19:54:45 2018

@author: gdiminin
"""

import re
from loadText import read_txt


def collect(GUI):
    singleLine = {}
    multipleLines = {}
    
    #Analysis to perform
    singleLine['@0A)'] = 'Y' if GUI._0A.isChecked() else 'N'
    singleLine['@0B)'] = 'Y' if GUI._0B.isChecked() else 'N'
    singleLine['@0C)'] = 'Y' if GUI._0C.isChecked() else 'N'
    singleLine['@0D)'] = 'Y' if GUI._0D.isChecked() else 'N'
    singleLine['@0E)'] = 'Y' if GUI._0E.isChecked() else 'N'
    singleLine['@0F)'] = 'Y' if GUI._0F.isChecked() else 'N'
    singleLine['@0G)'] = 'Y' if GUI._0G.isChecked() else 'N'
    singleLine['@0H)'] = 'Y' if GUI._0H.isChecked() else 'N'
    #General Information
    singleLine['@1A)'] = str(GUI._1A.text())
    singleLine['@1B)'] = str(GUI._1B.text())
    #Read
    singleLine['@2A)'] = str(GUI._2A.value())
    singleLine['@2B)'] = 'Y' if GUI._2B.currentText() == 'Yes' else 'N'
    multipleLines['@2C)'] = GUI._2C
    multipleLines['@2D)'] = GUI._2D
    multipleLines['@2E)'] = GUI._2E
    singleLine['@2F)'] = str(GUI._2F.text())
    singleLine['@2G)'] = str(GUI._2G.text())
    singleLine['@2H)'] = str(GUI._2H.value())
    singleLine['@2J)'] = str(GUI._2J.value())
    singleLine['@2K)'] = 'Y' if GUI._0H.isChecked() else 'N'
    #Phix
    singleLine['@3A)'] = str(GUI._3A.text())
    singleLine['@3B)'] = 'Y' if GUI._3B.isChecked() else 'N'
    singleLine['@3C)'] = str(GUI._3C.value())
    singleLine['@3D)'] = 'Y' if GUI._3D.currentText() == 'Yes' else 'N'
    multipleLines['@3E)'] = GUI._3E
    multipleLines['@3F)'] = GUI._3F
    multipleLines['@3G)'] = GUI._3G
    #Alignment
    singleLine['@4A)'] = str(GUI._4A.currentText())
    singleLine['@4B)'] = str(GUI._4B.text())
    singleLine['@4C)'] = 'Y' if GUI._4C.isChecked() else 'N'
    singleLine['@4D)'] = str(GUI._4D.value())
    singleLine['@4E)'] = 'Y' if GUI._4E.currentText() == 'Yes' else 'N'
    multipleLines['@4F)'] = GUI._4F
    multipleLines['@4G)'] = GUI._4G
    multipleLines['@4H)'] = GUI._4H
    #IIdefinition
    singleLine['@5A)'] = str(GUI._5A.value())
    singleLine['@5B)'] = str(GUI._5B.value())
    singleLine['@5C)'] = 'Y' if GUI._4C.isChecked() else 'N'
    singleLine['@5D)'] = str(GUI._5D.value())
    singleLine['@5E)'] = str(GUI._5E.value())
    singleLine['@5F)'] = 'Y' if GUI._5F.currentText() == 'Yes' else 'N'
    multipleLines['@5G)'] = GUI._5G
    multipleLines['@5H)'] = GUI._5H
    #IIingenes
    singleLine['@6A)'] = str(GUI._6A.text())
    singleLine['@6B)'] = 'Y' if GUI._6B.isChecked() else 'N'
    singleLine['@6C)'] = 'Y' if GUI._6C.isChecked() else 'N'
    singleLine['@6D)'] = 'Y' if GUI._6D.isChecked() else 'N'
    singleLine['@6E)'] = 'Y' if GUI._6E.isChecked() else 'N'
    singleLine['@6F)'] = str(GUI._6F.value())
    singleLine['@6G)'] = 'Y' if GUI._6G.currentText() == 'Yes' else 'N'
    multipleLines['@6H)'] = GUI._6H
    multipleLines['@6I)'] = GUI._6I
    #Analysis
    singleLine['@7A)'] = str(GUI._7A.value())
    singleLine['@7B)'] = str(GUI._7B.text())
    singleLine['@7C)'] = str(GUI._7C.text())
    multipleLines['@7D)'] = GUI._7D
    multipleLines['@7E)'] = GUI._7E
    singleLine['@7F)'] = 'Y' if GUI._7F.isChecked() else 'N'
    singleLine['@7G)'] = 'Y' if GUI._7G.isChecked() else 'N'
    singleLine['@7H)'] = 'Y' if GUI._7H.isChecked() else 'N'
    singleLine['@7I)'] = 'Y' if GUI._7I.isChecked() else 'N'
    singleLine['@7J)'] = 'Y' if GUI._7J.currentText() == 'Yes' else 'N'
    singleLine['@7K)'] = 'Y' if GUI._7K.isChecked() else 'N'
    singleLine['@7L)'] = 'Y' if GUI._7L.isChecked() else 'N'
    singleLine['@7M)'] = 'Y' if GUI._7M.isChecked() else 'N'
    singleLine['@7N)'] = 'Y' if GUI._7N.isChecked() else 'N'
    singleLine['@7O)'] = 'Y' if GUI._7O.isChecked() else 'N'
    singleLine['@7P)'] = 'Y' if GUI._7P.isChecked() else 'N'
    singleLine['@7Q)'] = str(GUI._7Q.value())
    singleLine['@7R)'] = str(GUI._7R.value())
    multipleLines['@7S)'] = GUI._7S
    multipleLines['@7T)'] = GUI._7T
    #Tables
    singleLine['@8A)'] = str(GUI._8A.value())
    multipleLines['@8B)'] = GUI._8B
    multipleLines['@8C)'] = GUI._8C
    multipleLines['@8D)'] = GUI._8D
    singleLine['@8E)'] = str(GUI._8E.text())
    #Graphs
    singleLine['@9A)'] = 'Y' if GUI._9A.isChecked() else 'N'
    singleLine['@9B)'] = 'Y' if GUI._9B.isChecked() else 'N'
    singleLine['@9C)'] = str(GUI._9C.text())
    singleLine['@9D)'] = str(GUI._9D.text())
    singleLine['@9E)'] = 'Y' if GUI._9E.currentText() == 'Yes' else 'N'
    singleLine['@9F)'] = str(GUI._9F.value())
    singleLine['@9G)'] = 'Y' if GUI._9G.currentText() == 'Yes' else 'N'
    singleLine['@9H)'] = str(GUI._9H.text())
    singleLine['@9I)'] = str(GUI._9I.text())
    return singleLine,multipleLines

def save (GUI,filePath,LoadModule):
    
    singleLine,multipleLines = collect(GUI)
    
    loadModule = open(LoadModule,'rb')
    newModule = open(filePath,'wb')
    old = []
    
    for line in loadModule:

        find = re.findall('^\s*(@\d[A-Z]\))',line)
        if find:
            if find[0] in singleLine.keys():
                newModule.write(line.rstrip() + singleLine[find[0]] +'\n')
            elif find[0] in multipleLines.keys():
                if find[0] not in old:
                    if multipleLines[find[0]]!= []:
                        for n in multipleLines[find[0]]:
                            newModule.write('%s %s\n' %(find[0],n))
                    else:
                        newModule.write('%s\n' %find[0])
                    old.append(find[0])
            else:
                newModule.write(line)
        else:
            newModule.write(line)
        
    
    loadModule.close()
    newModule.close()


def load (GUI,filePath):
    def setNumber(fieldGUI,fieldDictionary):
        try:
            fieldGUI.setValue(int(fieldDictionary))
            return fieldGUI
        except ValueError:
            pass
    def loadLists (groupGUI,groupDictionary,number,fieldNumber):
        for n in range(number):
            for m in range(len(groupGUI)):
                groupGUI[m].append('')
                if n+1 <= len(groupDictionary[m]):
                    groupGUI[m][n] = groupDictionary[m][n]
            if fieldNumber != 'No':    
                fieldNumber.setValue(n+1)  
    
    informations = {}
    informations = read_txt(informations,filePath)
    
    #Analysis to perform
    if informations[0]['A'] : GUI._0A.setChecked(True)
    if informations[0]['B'] : GUI._0B.setChecked(True)
    if informations[0]['C'] : GUI._0C.setChecked(True)
    if informations[0]['D'] : GUI._0D.setChecked(True)
    if informations[0]['E'] : GUI._0E.setChecked(True)
    if informations[0]['F'] : GUI._0F.setChecked(True)
    if informations[0]['G'] : GUI._0G.setChecked(True)
    if informations[0]['H'] : GUI._0H.setChecked(True)
    #General Information
    GUI._1A.setText(informations[1]['A'])
    GUI._1B.setText(informations[1]['B'])
    #Read
    GUI._2B.setCurrentIndex(0 if informations[2]['B'] else 1)
    GUI._2A.setValue(0)
    loadLists([GUI._2C,GUI._2D,GUI._2E],[informations[2]['C'],informations[2]['D'],informations[2]['E']],
              int(informations[2]['A']),GUI._2A)
    GUI._2F.setText(informations[2]['F'])
    GUI._2G.setText(informations[2]['G'])
    GUI._2H = setNumber(GUI._2H,informations[2]['H'])
    GUI._2J = setNumber(GUI._2J,informations[2]['J'])
    if informations[2]['K'] : GUI._2K.setChecked(True)
    #Phix
    GUI._3A.setText(informations[3]['A'])
    if informations[3]['B'] : GUI._3B.setChecked(True)
    GUI._3D.setCurrentIndex(0 if informations[3]['D'] else 1)
    GUI._3C.setValue(0)
    loadLists([GUI._3E,GUI._3F,GUI._3G],[informations[3]['E'],informations[3]['F'],informations[3]['G']],
                        int(informations[3]['B']),GUI._3C)
    #Alignment
    if informations[4]['A'] == 'Bowtie2':
        GUI._4A.setCurrentIndex(0)
    elif informations[4]['A'] == 'nvBowtie':
        GUI._4A.setCurrentIndex(1)
    elif informations[4]['A'] == 'ngm':  
        GUI._4A.setCurrentIndex(2)    
    GUI._4B.setText(informations[4]['B'])
    if informations[4]['C'] : GUI._4C.setChecked(True)
    GUI._4E.setCurrentIndex(0 if informations[4]['E'] else 1)
    GUI._4D.setValue(0)
    loadLists([GUI._4F,GUI._4G,GUI._4H],[informations[4]['F'],informations[4]['G'],informations[4]['H']],
                        int(informations[4]['D']),GUI._4D)
    #IIdefinition
    setNumber(GUI._5A,informations[5]['A'])
    setNumber(GUI._5B,informations[5]['B'])
    if informations[5]['C'] : GUI._5C.setChecked(True)
    setNumber(GUI._5D,informations[5]['D'])
    GUI._5F.setCurrentIndex(0 if informations[5]['F'] else 1)
    GUI._5E.setValue(0)
    loadLists([GUI._5G,GUI._5H],[informations[5]['G'],informations[5]['H']],
                        int(informations[5]['E']),GUI._5E)
    #IIingenes
    GUI._6A.setText(informations[6]['A'])
    if informations[6]['B'] : GUI._6B.setChecked(True)
    if informations[6]['C'] : GUI._6C.setChecked(True)
    if informations[6]['D'] : GUI._6D.setChecked(True)
    if informations[6]['E'] : GUI._6E.setChecked(True)
    GUI._6G.setCurrentIndex(0 if informations[6]['G'] else 1)
    GUI._6F.setValue(0)
    loadLists([GUI._6H,GUI._6I],[informations[6]['H'],informations[6]['I']],
                               int(informations[6]['F']),GUI._6F)
    #Analysis
    GUI._7A.setValue(0)
    GUI._7B.setText(informations[7]['B'])
    GUI._7C.setText(informations[7]['C'])
    loadLists([GUI._7D],[informations[7]['D']],int(informations[7]['A']),'No')
    loadLists([GUI._7E],[informations[7]['E']],int(informations[7]['A']),GUI._7A)
#    GUI._7A = setNumber(GUI._7A,informations[7]['A'])
    if informations[7]['F'] : GUI._7F.setChecked(True)
    if informations[7]['G'] : GUI._7G.setChecked(True)
    if informations[7]['H'] : GUI._7H.setChecked(True)
    if informations[7]['I'] : GUI._7I.setChecked(True)
    GUI._7J.setCurrentIndex(0 if informations[7]['J'] else 1)
    if informations[7]['K'] : GUI._7K.setChecked(True)
    if informations[7]['L'] : GUI._7L.setChecked(True)
    if informations[7]['M'] : GUI._7M.setChecked(True)
    if informations[7]['N'] : GUI._7N.setChecked(True)
    if informations[7]['O'] : GUI._7O.setChecked(True)
    if informations[7]['P'] : GUI._7P.setChecked(True)
    GUI._7Q = setNumber(GUI._7Q,informations[7]['Q']) 
    GUI._7R.setValue(0)
    loadLists([GUI._7S,GUI._7T],[informations[7]['S'],informations[7]['T']],
              int(informations[7]['R']),GUI._7R)
    #Tables
    GUI._8A.setValue(0)
    loadLists([GUI._8B,GUI._8C,GUI._8D],[informations[8]['B'],informations[8]['C'],informations[8]['D']],
              int(informations[8]['A']),GUI._8A)
    GUI._8E.setText(informations[8]['E'])
    #Graphs
    if informations[9]['A'] : GUI._9A.setChecked(True)
    if informations[9]['B'] : GUI._9B.setChecked(True)
    GUI._9C.setText(informations[9]['C'])
    GUI._9D.setText(informations[9]['D'])
    GUI._9E.setCurrentIndex(0 if informations[9]['E'] else 1)
    setNumber(GUI._9F,informations[9]['F'])
    GUI._9G.setCurrentIndex(0 if informations[9]['G'] else 1)
    GUI._9H.setText(informations[9]['H'])
    GUI._9I.setText(informations[9]['I'])

    
    
    
    
    
    
    