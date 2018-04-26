#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 14:07:44 2018

@author: gdiminin
"""
from PyQt4 import QtCore, QtGui

import re
from selectLibraries import Ui_Libraries
from headerSelection import Ui_Header
from filterSelection import Ui_Filter


def selectLibraries(main,output_):
    def emit(dialog,output_):
        libraries = ','.join([str(main.ui.selected.item(i).text()) for i in range(main.ui.selected.count())])
        output_.setText(libraries)        
    def add(dialog):
        row = dialog.available.currentRow()
        item = dialog.available.item(row).text()
        dialog.selected.addItem(item)        
    def remove(dialog):
        row = dialog.selected.currentRow()
        item = dialog.selected.takeItem(row)
        del item
    def up(dialog):
        row = dialog.selected.currentRow()
        if row >= 1:
            item = dialog.selected.takeItem(row)
            dialog.selected.insertItem(row - 1, item)
            dialog.selected.setCurrentItem(item)
    def down(dialog):
        row = dialog.selected.currentRow()
        if row < dialog.selected.count() - 1:
            item = dialog.selected.takeItem(row)
            dialog.selected.insertItem(row + 1, item)
            dialog.selected.setCurrentItem(item)
    
    main.window = QtGui.QDialog()
    main.ui = Ui_Libraries()
    main.ui.setupUi(main.window)
    for library in main.startingTask:
        main.ui.available.addItem(library)
    for library in [x.rstrip().lstrip() for x in str(output_.text()).split(',')]:
        main.ui.selected.addItem(library)
    main.ui.add.clicked.connect(lambda: add(main.ui))
    main.ui.remove.clicked.connect(lambda: remove(main.ui))
    main.ui.up.clicked.connect(lambda: up(main.ui))
    main.ui.down.clicked.connect(lambda: down(main.ui))
    
    main.ui.buttonBox.accepted.connect(lambda : emit(main.ui,output_))
    
    main.window.show()
    
###############################    
        
def headerSelection(main,output_):
    def emit(dialog,output_):
        libraries = ','.join([str(main.ui.selected.item(i).text()) for i in range(main.ui.selected.count())])
        output_.setText(libraries)        
    def add(dialog):
        sample = str(dialog.sample.currentText())
        parameter = str(dialog.parameter.currentText())
        function = str(dialog.function.currentText())
        header = '(%s,%s,%s)' %(sample,parameter,function)
        dialog.selected.addItem(header)       
    def remove(dialog):
        row = dialog.selected.currentRow()
        item = dialog.selected.takeItem(row)
        del item
    def up(dialog):
        row = dialog.selected.currentRow()
        if row >= 1:
            item = dialog.selected.takeItem(row)
            dialog.selected.insertItem(row - 1, item)
            dialog.selected.setCurrentItem(item)
    def down(dialog):
        row = dialog.selected.currentRow()
        if row < dialog.selected.count() - 1:
            item = dialog.selected.takeItem(row)
            dialog.selected.insertItem(row + 1, item)
            dialog.selected.setCurrentItem(item)
    def fillComboBox(main,dialog):
        def changeFunction(main,dialog,rawExperiments):
            dialog.function.clear()
            to_exclude = list(rawExperiments.union(str(main._7B.text())))
            if dialog.parameter.currentText()=='Score':
                if dialog.sample.currentText()not in to_exclude:
                    dialog.function.addItem('all')
                    dialog.function.addItem('fisher')
                    if main._7K.isChecked():
                        dialog.function.addItem('fold')
                    if main._7L.isChecked():
                        dialog.function.addItem('rank')
            else:
                for function in ['all','raw','rank']:
                    dialog.function.addItem(function)
                if dialog.sample.currentText()not in to_exclude:
                    dialog.function.addItem('fold')    
                multipleExperiments = False
                for group in main._7E:
                    if len(','.join(group)) > 1:
                        multipleExperiments = True
                if len(','.join(str(main._7C.text()))) > 1:
                    multipleExperiments = True
                if multipleExperiments:
                    if dialog.sample.currentText()not in to_exclude[:-1]:
                        for function in ['mean', 'stdev']:
                            dialog.function.addItem(function) 
                        if dialog.sample.currentText() != to_exclude[-1]:
                            dialog.function.addItem('ttest')
        #Sample
        dialog.sample.addItem('All')
        dialog.sample.addItem('Raw')
        dialog.sample.addItem(str(main._7B.text()))
        for group in main._7D:
            if group != '':
                dialog.sample.addItem(group)
        
        rawExperiments = set()
        rawExperiments = rawExperiments.union(str(main._7C.text()).split(','))
        for group in main._7E:
            rawExperiments = rawExperiments.union(group.split(','))
        
        for library in rawExperiments:
            if library != '':
                dialog.sample.addItem(library)
                
        #Parameter
        dialog.parameter.addItem('All')
        if main._7F.isChecked():
            dialog.parameter.addItem('II')
        if main._7G.isChecked():
            dialog.parameter.addItem('KI')
        if main._7H.isChecked():
            dialog.parameter.addItem('Bias')
        if main._7I.isChecked():
            dialog.parameter.addItem('Reads')
        if main._7J.currentText()=='Yes':
            dialog.parameter.addItem('Score')
        #Function
        changeFunction(main,dialog,rawExperiments)
        dialog.parameter.currentIndexChanged.connect(lambda: changeFunction(main,dialog,rawExperiments))
        dialog.sample.currentIndexChanged.connect(lambda: changeFunction(main,dialog,rawExperiments))
        
    main.window = QtGui.QDialog()
    main.ui = Ui_Header()
    main.ui.setupUi(main.window)
    
    fillComboBox(main,main.ui)
    for header in re.findall('(\(.*?\))',str(output_.text())):
        main.ui.selected.addItem(header)
    main.ui.add.clicked.connect(lambda: add(main.ui))
    main.ui.remove.clicked.connect(lambda: remove(main.ui))
    main.ui.up.clicked.connect(lambda: up(main.ui))
    main.ui.down.clicked.connect(lambda: down(main.ui))
    
    main.ui.buttonBox.accepted.connect(lambda : emit(main.ui,output_))
    
    main.window.show()
    
###############################    
        
def filterSelection(main,output_):
    def emit(dialog,output_):
        libraries = ','.join([str(main.ui.selected.item(i).text()) for i in range(main.ui.selected.count())])
        output_.setText(libraries)        
    def add(dialog):
        sample = str(dialog.sample.currentText())
        parameter = str(dialog.parameter.currentText())
        function = str(dialog.function.currentText())
        header = '(%s,%s,%s)' %(sample,parameter,function)
        
        operation = str(dialog.operation.currentText())
        if operation not in ['Ascending','Descending']:
            value = str(dialog.value.value())
            filter_ = '[%s,%s,%s]' %(header,operation,value)
        else:
            filter_ = '[%s,%s]' %(header,operation)
        
        dialog.selected.addItem(filter_)       
    def remove(dialog):
        row = dialog.selected.currentRow()
        item = dialog.selected.takeItem(row)
        del item
    def up(dialog):
        row = dialog.selected.currentRow()
        if row >= 1:
            item = dialog.selected.takeItem(row)
            dialog.selected.insertItem(row - 1, item)
            dialog.selected.setCurrentItem(item)
    def down(dialog):
        row = dialog.selected.currentRow()
        if row < dialog.selected.count() - 1:
            item = dialog.selected.takeItem(row)
            dialog.selected.insertItem(row + 1, item)
            dialog.selected.setCurrentItem(item)
            
    def fillComboBox(main,dialog):
        def changeFunction(main,dialog,rawExperiments):
            dialog.function.clear()
            to_exclude = list(rawExperiments.union(str(main._7B.text())))
            if dialog.parameter.currentText()=='Score':
                if dialog.sample.currentText()not in to_exclude:
                    dialog.function.addItem('fisher')
                    if main._7K.isChecked():
                        dialog.function.addItem('fold')
                    if main._7L.isChecked():
                        dialog.function.addItem('rank')
            else:
                for function in ['raw','rank']:
                    dialog.function.addItem(function)
                if dialog.sample.currentText()not in to_exclude:
                    dialog.function.addItem('fold')    
                multipleExperiments = False
                for group in main._7E:
                    if len(','.join(group)) > 1:
                        multipleExperiments = True
                if len(','.join(str(main._7C.text()))) > 1:
                    multipleExperiments = True
                if multipleExperiments:
                    if dialog.sample.currentText()not in to_exclude[:-1]:
                        for function in ['mean', 'stdev']:
                            dialog.function.addItem(function) 
                        if dialog.sample.currentText() != to_exclude[-1]:
                            dialog.function.addItem('ttest')
        #Sample
        dialog.sample.addItem(str(main._7B.text()))
        for group in main._7D:
            if group != '':
                dialog.sample.addItem(group)
        rawExperiments = set()
        rawExperiments = rawExperiments.union(str(main._7C.text()).split(','))
        for group in main._7E:
            rawExperiments = rawExperiments.union(group.split(','))
        for library in rawExperiments:
            if library != '':
                dialog.sample.addItem(library)
                
        #Parameter
        if main._7F.isChecked():
            dialog.parameter.addItem('II')
        if main._7G.isChecked():
            dialog.parameter.addItem('KI')
        if main._7H.isChecked():
            dialog.parameter.addItem('Bias')
        if main._7I.isChecked():
            dialog.parameter.addItem('Reads')
        if main._7J.currentText()=='Yes':
            dialog.parameter.addItem('Score')
        #Function
        changeFunction(main,dialog,rawExperiments)
        dialog.parameter.currentIndexChanged.connect(lambda: changeFunction(main,dialog,rawExperiments))
        dialog.sample.currentIndexChanged.connect(lambda: changeFunction(main,dialog,rawExperiments))
      
    main.window = QtGui.QDialog()
    main.ui = Ui_Filter()
    main.ui.setupUi(main.window)
    
    fillComboBox(main,main.ui)
    for filter_ in re.findall('(\[.*?\])',str(output_.text())):
        main.ui.selected.addItem(filter_)
    main.ui.add.clicked.connect(lambda: add(main.ui))
    main.ui.remove.clicked.connect(lambda: remove(main.ui))
    main.ui.up.clicked.connect(lambda: up(main.ui))
    main.ui.down.clicked.connect(lambda: down(main.ui))
    
    main.ui.buttonBox.accepted.connect(lambda : emit(main.ui,output_))
    
    main.window.show()