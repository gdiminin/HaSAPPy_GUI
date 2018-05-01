
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 08:15:05 2018

@author: gdiminin
"""

import sys
from PyQt4 import QtCore, QtGui
import dialogs
import SaveLoad


class QHLine(QtGui.QFrame):
    def __init__(self):
        super(QHLine,self).__init__()
        self.setFrameShape(QtGui.QFrame.HLine)
        self.setFrameShadow(QtGui.QFrame.Sunken)
        

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(939, 626)
        self.experimentCount = {}
        self.pairEndWidgets = {}

        self.splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.splitter.setSizes([100,200])
        self.generate_generalFrame()  #generates the General object on the left
        self.generate_taskFrame()     #generates the Task object on the right      
        
        self.splitter.addWidget(self.general)
        self.splitter.addWidget(self.task) #default task profile
        
        self.setCentralWidget(self.splitter)
        
        #BarMenu actions
        openFile = QtGui.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        saveFile = QtGui.QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        self.statusBar()

        mainMenu = self.menuBar()
        
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        ####
        
        layout = QtGui.QGridLayout()
        layout.addWidget(self.general)
        layout.addWidget(self.task)
        
        
#        self.setLayout(layout)
        
        
################### GENERAL FUNCTIONS #########################################      
    def add_widget_to_layout(self,widgets,layout):
        for element in widgets:
            if element == 'stretch':
                layout.addStretch(1)
            else:
                layout.addWidget(element)
        return layout
    
    def add_widget_to_gridlayout(self,widgets,layout):
        horizontalSpacer =QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        for element,x,y,l,h in widgets:
            if element == 'space_h':
                layout.addItem(horizontalSpacer,x,y,l,h)
                
            else:    
                layout.addWidget(element,x,y,l,h)
        return layout
    def add_layout_to_layout(self,layouts,layout_main):
        for layout in layouts:
            if layout == 'stretch':
                layout_main.addStretch(1)
            else:
                layout_main.addLayout(layout)
    
    
    def getfile(self,QLineEdit):
        file_name = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        QLineEdit.setText(file_name)
    
    def getFolder(self,QLineEdit):
        file_name = QtGui.QFileDialog.getExistingDirectory(self, 'Open file')
        QLineEdit.setText(file_name)
        
    def deactivate(self,to_deactivate,if_modified):
        try:
            if if_modified.isChecked():
                for widget in to_deactivate:
                    widget.setEnabled(True)
            else:
                for widget in to_deactivate:
                    widget.setEnabled(False)
        except AttributeError:
            if if_modified.currentText() == 'Yes':
                for widget in to_deactivate:
                    widget.setEnabled(True)
            else:
                for widget in to_deactivate:
                    widget.setEnabled(False)
                    
    def defineStartingTask(self):
        if self._0A.isChecked():
            self.startingTask = self._2C
        elif self._0B.isChecked():
            self.startingTask = self._3E
        elif self._0C.isChecked():
            self.startingTask = self._4F
        elif self._0D.isChecked():
            self.startingTask = self._5G
        elif self._0E.isChecked():
            self.startingTask = self._6H
        elif self._0F.isChecked():
            self.startingTask = self._7Q
        else:
            self.startingTask = 'n.d'  
                    
    def enableTab (self,box,index):
        if box.isChecked():
            self.task.setTabEnabled(index,True)
        else:
            self.task.setTabEnabled(index,False)            
        self.defineStartingTask()
        
            
                
    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        SaveLoad.load(self,name)

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        SaveLoad.save (self,name,'LoadModule.txt')

    def addExperiment(self,group,l_group,task,newNumberLine,pairEnd,name,input_1,input_2):#newNumberLine=self.xx.value() - pairEnd = self.xx.currentText()      
        ####
        def storeValue(group,index,value):
            group[index] = value
        ####
        while self.experimentCount[task] != newNumberLine:
            n = self.experimentCount[task] +1

            if self.experimentCount[task] < newNumberLine:  
                if len(name) <= n:
                    name.append('')
                    input_1.append('')
                    if input_2 != 'No':
                        input_2.append('')
                label = QtGui.QLabel('%i)'%n,group)
                libraryName = QtGui.QLineEdit(name[n-1],group)
                inputFirst = QtGui.QLineEdit(group)
                inputFirst.setText(input_1[n-1])
                tool_inputFirst = QtGui.QToolButton(group)
                tool_inputFirst.setIcon(QtGui.QIcon(QtGui.QPixmap("icons/open.png")))
                tool_inputFirst.clicked.connect(lambda: self.getfile(inputFirst)) 
                inputSecond = QtGui.QLineEdit(group)
                if input_2 != 'No':
                    inputSecond.setText(input_2[n-1])
                tool_inputSecond = QtGui.QToolButton(group)
                tool_inputSecond.setIcon(QtGui.QIcon(QtGui.QPixmap("icons/open.png")))
                tool_inputSecond.clicked.connect(lambda: self.getfile(inputSecond))
            
                self.add_widget_to_gridlayout([(label,int((n*2)+1),2,1,1),
                                           (libraryName,int((n*2)+1),3,1,2),(inputFirst,int((n*2)+1),5,1,1),(tool_inputFirst,int((n*2)+1),6,1,1)
                                           ,(inputSecond,int((n*2)+1),7,1,1),(tool_inputSecond,int((n*2)+1),8,1,1)
                                           ],l_group)
                self.pairEndWidgets[task] +=[l_group.count()-2,l_group.count()-1]
                
                    
                libraryName.editingFinished.connect(lambda: storeValue(name,n-1,str(libraryName.text())))
                inputFirst.textChanged.connect(lambda: storeValue(input_1,n-1,str(inputFirst.text())))
                
                if input_2 != 'No':
                    inputSecond.textChanged.connect(lambda: storeValue(input_2,n-1,str(inputSecond.text())))
                
                self.experimentCount[task] +=1
                
                
            else:
                for x in range(6):
                    item = l_group.takeAt(l_group.count()-1)
                    widget = item.widget()
                    widget.deleteLater()
                self.pairEndWidgets[task] = self.pairEndWidgets[task][:-2]
                self.experimentCount[task] -=1
                del name[n-2]
                del input_1[n-2]
                if input_2 != 'No':
                    del input_2[n-2]
                
             
        if pairEnd == 'No':
            for x in self.pairEndWidgets[task][::-1]:
                item = l_group.itemAt(x)
                widget = item.widget()
                widget.setHidden(True)
        else:
            for x in self.pairEndWidgets[task][::-1]:
                item = l_group.itemAt(x)
                widget = item.widget()
                widget.setHidden(False)
  
        return group,l_group
        
###############################################################################   
     
    def generate_generalFrame(self):
        """Generates the Left dialog box where user defines general informations
        and sets up the type of analysis to perform. At the end the "Updte" button
        generates the right Dialog() and the "Start" button run the analysis"""
        
        self.general =  QtGui.QScrollArea()
        layout = QtGui.QVBoxLayout()
        
        #Definition of the widgets of the first block        
        label_1 = QtGui.QLabel("  User name:",self.general)
        label_2 = QtGui.QLabel("  Saving directory:",self.general)
        self._1A = QtGui.QLineEdit(self.general)
        self._1B = QtGui.QLineEdit(self.general)
        self.tool_1B = QtGui.QToolButton(self.general)
        self.tool_1B.setIcon(QtGui.QIcon(QtGui.QPixmap("icons/open.png")))
        self.tool_1B.clicked.connect(lambda: self.getFolder(self._1B)) #connect the tool_1B to QFileDialog and saving PATH in self._1B
        layout_1B = QtGui.QHBoxLayout()
        layout_1B = self.add_widget_to_layout([self._1B,self.tool_1B],layout_1B)
        
        #Adding widgets to layout 
        layout = self.add_widget_to_layout([label_1,self._1A,label_2],layout)
        layout.addLayout(layout_1B)
        layout.addStretch(1)
        
        #Definition of the widgets of the second block 
        label_3 = QtGui.QLabel("  Analysis to perform:",self.general)
        self._0A = QtGui.QCheckBox(' Read trimming',self.general)
        self._0B = QtGui.QCheckBox(' Phix genome removal',self.general)
        self._0C = QtGui.QCheckBox(' Alignment to genome',self.general)
        self._0D = QtGui.QCheckBox(' I.I. identification',self.general)
        self._0E = QtGui.QCheckBox(' Classification of I.I.\n in genes',self.general)
        self._0F = QtGui.QCheckBox(' Analysis of experiments',self.general)
        self._0G = QtGui.QCheckBox(' Defining tables',self.general)
        self._0H = QtGui.QCheckBox(' Graphs',self.general)
        
        #Adding widgets to layout
        layout = self.add_widget_to_layout([label_3,self._0A,self._0B,
                                            self._0C,self._0D,self._0E,self._0F,
                                            self._0G,self._0H],
                                            layout)
        layout.addStretch(1)
        
         
        
        #Definition of the widgets of the third block 
        self.general.updateButton =  QtGui.QPushButton("Update")
        self.general.startButton =  QtGui.QPushButton("Start")
        l_commands = QtGui.QHBoxLayout()
        l_commands = self.add_widget_to_layout([self.general.updateButton,
                                                     self.general.startButton],
                                                    l_commands)

        layout.addLayout(l_commands)
        
        #Adding widgets to layout
        self.general.setLayout(layout)
        
    def generate_taskFrame(self):                
        
        self.task =  QtGui.QTabWidget() #Tab widget according the analysis to perform
        self.task.setGeometry(QtCore.QRect(290, 10, 491, 521))
        
        self.generate_tabReads()
        self.generate_tabPhix()
        self.generate_tabAlignment()
        self.generate_tabIIdefinition()
        self.generate_tabIIingenes()
        self.generate_tabAnalysis()
        self.generate_tabTables()
        self.generate_tabDesign()
        
        #Deactivate all the generated tabs
        for n in range (8):
            self.task.setTabEnabled(n,False)
        
        #Activate the frame selected in the general Task
        self._0A.stateChanged.connect(lambda: self.enableTab(self._0A,0))
        self._0B.stateChanged.connect(lambda: self.enableTab(self._0B,1))
        self._0C.stateChanged.connect(lambda: self.enableTab(self._0C,2))
        self._0D.stateChanged.connect(lambda: self.enableTab(self._0D,3))
        self._0E.stateChanged.connect(lambda: self.enableTab(self._0E,4))
        self._0F.stateChanged.connect(lambda: self.enableTab(self._0F,5))
        self._0G.stateChanged.connect(lambda: self.enableTab(self._0G,6))
        self._0H.stateChanged.connect(lambda: self.enableTab(self._0H,7))
       
    def generate_tabReads(self):
        
        self.Read = QtGui.QFrame()#2nd 
        l_Read = QtGui.QGridLayout() #layout 2nd
        
        scrollArea = QtGui.QScrollArea(self.Read) #3rd
        scrollArea.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidgetResizable(True)
        l_scroll = QtGui.QGridLayout(scrollArea) #layout 3rd 
        container = QtGui.QWidget(scrollArea) #4th
        container.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidget(container) #link 4th to 3rd =>provides to container to scroll
        ####Add here container attributes####
        l_container = QtGui.QVBoxLayout()
        label_1 = QtGui.QLabel('Read trimming',container)
        label_1.setFont(QtGui.QFont("",20,QtGui.QFont.Bold))
        label_2 = QtGui.QLabel('Numbers of libraries to analyse:\t\t',container)
        label_3 = QtGui.QLabel('Are libreries sequenced pair-end?\t\t',container)
        self._2A = QtGui.QSpinBox(container)
        self._2A.setRange(0,100)
        self._2A.setValue(1)
        self._2B = QtGui.QComboBox(container)
        self._2B.addItems(['Yes','No'])
        
        #Creates a QGridLayout where to store position of libraries location created in addExperiment function
        line_4 = QtGui.QGridLayout()
        
        self._2C = []
        self._2D = []
        self._2E = []
        
        self.experimentCount['Read'] = 0
        self.pairEndWidgets['Read'] = []
        label_4 = QtGui.QLabel('Name of the libraries',container)
        label_5 = QtGui.QLabel('Location of file',container)
        label_6 = QtGui.QLabel('Location of file P7',container)
        
        self.add_widget_to_gridlayout([(label_4,0,3,1,2),(label_5,0,5,1,1),(label_6,0,7,1,1)],
                                       line_4)
        self.pairEndWidgets['Read'].append(line_4.count()-1)
        container,line_4 = self.addExperiment(container,line_4,'Read',self._2A.value(),self._2B.currentText(),
                                              self._2C,self._2D,self._2E)
        
        self._2A.valueChanged.connect(lambda : self.addExperiment(container,line_4,'Read',self._2A.value(),self._2B.currentText(),
                                            self._2C,self._2D,self._2E))
        self._2B.currentIndexChanged.connect(lambda : self.addExperiment(container,line_4,'Read',self._2A.value(),self._2B.currentText(),
                                            self._2C,self._2D,self._2E))
        ###
        
        label_8 = QtGui.QLabel('Adaptor p7 sequence\t\t\t\t\n(for trimming 3 ends of sequence in file 1)',container)
        self._2F = QtGui.QLineEdit(container)
        label_9 = QtGui.QLabel('Adaptor p5 sequence\t\t\t\t\n(for trimming 3 ends of sequence in file 2)',container)
        self._2G = QtGui.QLineEdit(container)
        label_10 = QtGui.QLabel('Quality selection parameters',container)
        label_11 = QtGui.QLabel('    Initial bad quality QA value detected:\t\t',container)
        self._2H = QtGui.QSpinBox(container)
        self._2H.setRange(1,45)
        self._2H.setValue(20)
        self.slider_2H = QtGui.QSlider(QtCore.Qt.Horizontal,container)
        self.slider_2H.setRange(1,45)
        self.slider_2H.setValue(20)
        self._2H.valueChanged.connect(self.slider_2H.setValue)
        self.slider_2H.valueChanged.connect(self._2H.setValue)
        
        label_12 = QtGui.QLabel('    Quality average limit of 3 end sequence\t\t\n'
                                '    after the call of a bad quality base:',container)
        self._2J = QtGui.QSpinBox(container)
        self._2J.setRange(1,45)
        self._2J.setValue(30)
        self.slider_2J = QtGui.QSlider(QtCore.Qt.Horizontal,container)
        self.slider_2J.setRange(1,45)
        self.slider_2J.setValue(30)
        self._2J.valueChanged.connect(self.slider_2J.setValue)
        self.slider_2J.valueChanged.connect(self._2J.setValue)
        
        
        
        label_13 = QtGui.QLabel('Permanently store Libraries\t\t\t\nafter "Read Trimming" (FASTQ file) ',container)
        self._2K = QtGui.QCheckBox(container)
        
        ###### Place conatainer attribuates #######
        spacer = QtGui.QHBoxLayout()
        self.add_widget_to_layout(['stretch'],spacer)
        line_1 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_1,'stretch'],line_1)
        line_2 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_2,self._2A,'stretch'],line_2)
        line_3 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_3,self._2B,'stretch'],line_3)    
        line_7 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_8,self._2F],line_7)
        line_8 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_9,self._2G],line_8)
        line_9 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_10,'stretch'],line_9)
        line_10 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_11,self._2H,self.slider_2H,'stretch'],line_10)
        line_11 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_12,self._2J,self.slider_2J,'stretch'],line_11)
        line_12 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_13,self._2K,'stretch'],line_12)
        
        self.add_layout_to_layout([line_1,'stretch',line_2,line_3,'stretch',line_4,
                              'stretch',line_7,line_8,'stretch',line_9,line_10,line_11,'stretch',line_12],l_container)
        
        container.setLayout(l_container)
        #####################################
    
        l_scroll.addWidget(container)  #link 4th to 3rd
        scrollArea.setLayout(l_scroll) # and layout
        
        l_Read.addWidget(scrollArea) #link 3rd to 2nd
        self.Read.setLayout(l_Read)  # and layout
        
        self.task.addTab(self.Read, "Read") #link 2nd to 1st creating a new tab
        
    def generate_tabPhix(self):
        self.Phix = QtGui.QFrame()#2nd 
        l_Phix = QtGui.QGridLayout() #layout 2nd
        
        scrollArea = QtGui.QScrollArea(self.Phix) #3rd
        scrollArea.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidgetResizable(True)
        l_scroll = QtGui.QGridLayout(scrollArea) #layout 3rd 
        
        container = QtGui.QWidget(scrollArea) #4th
        container.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidget(container) #link 4th to 3rd =>provides to container to scroll
        ####Add here container attributes####
        l_container = QtGui.QVBoxLayout()
        label_1 = QtGui.QLabel('Phix genome removal',container)
        label_1.setFont(QtGui.QFont("",20,QtGui.QFont.Bold))
        label_2 = QtGui.QLabel('Location of Phix genome reference:\t\t',container)
        self._3A = QtGui.QLineEdit(container)
        self.tool_3A = QtGui.QToolButton(container)
        self.tool_3A.setIcon(QtGui.QIcon(QtGui.QPixmap("icons/open.png")))
        self.tool_3A.clicked.connect(lambda: self.getfile(self._3A))
        label_3 = QtGui.QLabel('Permanently store Libraries\t\t\nafter "Phix removal" (FASTQ file) ',container)
        self._3B = QtGui.QCheckBox(container)
        label_4 = QtGui.QLabel('Numbers of libraries to analyse:\t\t',container)
        label_5 = QtGui.QLabel('Are libreries sequenced pair-end?\t\t',container)
        self._3C = QtGui.QSpinBox(container)
        self._3C.setRange(1,100)
        self._3C.setValue(1)
        self._3D = QtGui.QComboBox(container)
        self._3D.addItems(['Yes','No'])
        
        #Creates a QGridLayout where to store position of libraries location created in addExperiment function
        line_7 = QtGui.QGridLayout()
        
        self._3E = []
        self._3F = []
        self._3G = []
        
        self.experimentCount['Phix'] = 0
        self.pairEndWidgets['Phix'] = []
        label_6 = QtGui.QLabel('Name of the libraries',container)
        label_7 = QtGui.QLabel('Location of file',container)
        label_8 = QtGui.QLabel('Location of file P7',container)
        self.add_widget_to_gridlayout([(label_6,0,3,1,2),(label_7,0,5,1,1),(label_8,0,7,1,1)],
                                       line_7)
        self.pairEndWidgets['Phix'].append(line_7.count()-1)
        container,line_7 = self.addExperiment(container,line_7,'Phix',self._3C.value(),self._3D.currentText(),
                                              self._3E,self._3F,self._3G)
        self._3C.valueChanged.connect(lambda : self.addExperiment(container,line_7,'Phix',self._3C.value(),self._3D.currentText(),
                                            self._3E,self._3F,self._3G))
        self._3D.currentIndexChanged.connect(lambda : self.addExperiment(container,line_7,'Phix',self._3C.value(),self._3D.currentText(),
                                            self._3E,self._3F,self._3G))
        ###### Place conatainer attribuates #######
        l_container = QtGui.QVBoxLayout()
        spacer = QtGui.QHBoxLayout()
        self.add_widget_to_layout(['stretch'],spacer)
        line_1 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_1,'stretch'],line_1)
        line_2 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_2,self._3A,self.tool_3A],line_2)
        line_3 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_3,self._3B,'stretch'],line_3)
        line_4 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([QHLine()],line_4)
        line_5 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_4,self._3C,'stretch'],line_5)
        line_6 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_5,self._3D,'stretch'],line_6)
        self.add_layout_to_layout([line_1,line_2,line_3,'stretch',line_4,line_5,line_6,line_7],l_container)
        container.setLayout(l_container)
        #####################################
        l_scroll.addWidget(container)  #link 4th to 3rd
        scrollArea.setLayout(l_scroll) # and layout
        l_Phix.addWidget(scrollArea) #link 3rd to 2nd
        self.Phix.setLayout(l_Phix)  # and layout
        self.task.addTab(self.Phix, "Phix") #link 2nd to 1st creating a new tab
        
        
    def generate_tabAlignment(self):
        self.Alignment = QtGui.QFrame()#2nd 
        l_Alignment = QtGui.QGridLayout() #layout 2nd
        
        scrollArea = QtGui.QScrollArea(self.Alignment) #3rd
        scrollArea.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidgetResizable(True)
        l_scroll = QtGui.QGridLayout(scrollArea) #layout 3rd 
        
        container = QtGui.QWidget(scrollArea) #4th
        container.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidget(container) #link 4th to 3rd =>provides to container to scroll
        ####Add here container attributes####
        l_container = QtGui.QVBoxLayout()
        label_1 = QtGui.QLabel('Alignment to the reference genome',container)
        label_1.setFont(QtGui.QFont("",20,QtGui.QFont.Bold))
        label_2 = QtGui.QLabel('Alignment program:\t\t\t',container)
        self._4A = QtGui.QComboBox(container)
        self._4A.addItems(['Bowtie2','nvBowtie','ngm'])
        label_3 = QtGui.QLabel('Location of refernce genome:\t\t',container)
        self._4B = QtGui.QLineEdit(container)
        self.tool_4B = QtGui.QToolButton(container)
        self.tool_4B.setIcon(QtGui.QIcon(QtGui.QPixmap("icons/open.png")))
        self.tool_4B.clicked.connect(lambda: self.getfile(self._4B))
        label_4 = QtGui.QLabel('Permanently store aligned libraries\t\t\n(SAM file) ',container)
        self._4C = QtGui.QCheckBox(container)
        
        label_5 = QtGui.QLabel('Numbers of libraries to analyse:\t\t',container)
        label_6 = QtGui.QLabel('Are libreries sequenced pair-end?\t\t',container)
        self._4D = QtGui.QSpinBox(container)
        self._4D.setRange(1,100)
        self._4D.setValue(1)
        self._4E = QtGui.QComboBox(container)
        self._4E.addItems(['Yes','No'])
        
        #Creates a QGridLayout where to store position of libraries location created in addExperiment function
        line_8 = QtGui.QGridLayout()
        
        self._4F = []
        self._4G = []
        self._4H = []

        self.experimentCount['Alignment'] = 0
        self.pairEndWidgets['Alignment'] = []
        label_7 = QtGui.QLabel('Name of the libraries',container)
        label_8 = QtGui.QLabel('Location of file',container)
        label_9 = QtGui.QLabel('Location of file P7',container)
        self.add_widget_to_gridlayout([(label_7,0,3,1,2),(label_8,0,5,1,1),(label_9,0,7,1,1)],
                                       line_8)
        self.pairEndWidgets['Alignment'].append(line_8.count()-1)
        container,line_8 = self.addExperiment(
                container,line_8,'Alignment',self._4D.value(),self._4E.currentText(),
                self._4F,self._4G,self._4H)
        self._4D.valueChanged.connect(lambda : self.addExperiment(
                container,line_8,'Alignment',self._4D.value(),self._4E.currentText(),
                self._4F,self._4G,self._4H))
        self._4E.currentIndexChanged.connect(lambda : self.addExperiment(
                container,line_8,'Alignment',self._4D.value(),self._4E.currentText(),
                self._4F,self._4G,self._4H))
        ###### Place conatainer attribuates #######
        l_container = QtGui.QVBoxLayout()
        spacer = QtGui.QHBoxLayout()
        self.add_widget_to_layout(['stretch'],spacer)
        line_1 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_1,'stretch'],line_1)
        line_2 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_2,self._4A,'stretch'],line_2)
        line_3 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_3,self._4B,self.tool_4B],line_3)
        line_4 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_4,self._4C,'stretch'],line_4)
        line_5 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([QHLine()],line_5)
        line_6 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_5,self._4D,'stretch'],line_6)
        line_7 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_6,self._4E,'stretch'],line_7)
        
        
        self.add_layout_to_layout([line_1,line_2,line_3,line_4,'stretch',line_5,line_6,line_7,line_8],l_container)
        container.setLayout(l_container)
        #####################################
        l_scroll.addWidget(container)  #link 4th to 3rd
        scrollArea.setLayout(l_scroll) # and layout
        l_Alignment.addWidget(scrollArea) #link 3rd to 2nd
        self.Alignment.setLayout(l_Alignment)  # and layout
        self.task.addTab(self.Alignment, "Alignment") #link 2nd to 1st creating a new tab
        
    def generate_tabIIdefinition(self):
        self.IIdefinition = QtGui.QFrame()#2nd 
        l_IIdefinition = QtGui.QGridLayout() #layout 2nd
        
        scrollArea = QtGui.QScrollArea(self.IIdefinition) #3rd
        scrollArea.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidgetResizable(True)
        l_scroll = QtGui.QGridLayout(scrollArea) #layout 3rd 
        
        container = QtGui.QWidget(scrollArea) #4th
        container.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidget(container) #link 4th to 3rd =>provides to container to scroll
        ####Add here container attributes####
        l_container = QtGui.QVBoxLayout()
        label_1 = QtGui.QLabel('Identification of I.I.',container)
        label_1.setFont(QtGui.QFont("",20,QtGui.QFont.Bold))
        label_2 = QtGui.QLabel('Number of reads to define I.I. :\t',container)
        self._5A = QtGui.QSpinBox(container)
        self._5A.setRange(1,100)
        self._5A.setValue(1)
        self.slider_5A = QtGui.QSlider(QtCore.Qt.Horizontal,container)
        self.slider_5A.setRange(1,100)
        self.slider_5A.setValue(1)
        self._5A.valueChanged.connect(self.slider_5A.setValue)
        self.slider_5A.valueChanged.connect(self._5A.setValue)
        label_3 = QtGui.QLabel('Window size to define I.I. :\t\t',container)
        self._5B = QtGui.QSpinBox(container)
        self._5B.setRange(1,100)
        self._5B.setValue(1)
        self.slider_5B = QtGui.QSlider(QtCore.Qt.Horizontal,container)
        self.slider_5B.setRange(1,100)
        self.slider_5B.setValue(1)
        self._5B.valueChanged.connect(self.slider_5B.setValue)
        self.slider_5B.valueChanged.connect(self._5B.setValue)
        label_4 = QtGui.QLabel('Alignment Q value :\t\t',container)
        self._5C = QtGui.QCheckBox(container)
        self._5C.setChecked(True)
        self._5D = QtGui.QSpinBox(container)
        self._5D.setRange(0,100)
        self._5D.setValue(0)
        self.slider_5D = QtGui.QSlider(QtCore.Qt.Horizontal,container)
        self.slider_5D.setRange(0,100)
        self.slider_5D.setValue(0)
        
        self._5C.clicked.connect(lambda: self.deactivate([self._5D,self.slider_5D],self._5C))
        self._5D.valueChanged.connect(self.slider_5D.setValue)
        self.slider_5D.valueChanged.connect(self._5D.setValue)
        
        label_5 = QtGui.QLabel('Numbers of libraries to analyse:\t\t',container)
        label_6 = QtGui.QLabel('Are libreries sequenced pair-end?\t\t',container)
        self._5E = QtGui.QSpinBox(container)
        self._5E.setRange(1,100)
        self._5E.setValue(1)
        self._5F = QtGui.QComboBox(container)
        self._5F.addItems(['Yes','No'])
        
        #Creates a QGridLayout where to store position of libraries location created in addExperiment function
        line_8 = QtGui.QGridLayout()
        
        self._5G = []
        self._5H = []
        
        self.experimentCount['IIdefinition'] = 0
        self.pairEndWidgets['IIdefinition'] = []
        label_7 = QtGui.QLabel('Name of the libraries',container)
        label_8 = QtGui.QLabel('Location of file',container)
        label_9 = QtGui.QLabel('Location of file P7',container)
        self.add_widget_to_gridlayout([(label_7,0,3,1,2),(label_8,0,5,1,1),(label_9,0,7,1,1)],
                                       line_8)
        self.pairEndWidgets['IIdefinition'].append(line_8.count()-1)
        container,line_8 = self.addExperiment(
                container,line_8,'IIdefinition',self._5E.value(),'No',self._5G,self._5H,'No')
        self._5E.valueChanged.connect(lambda : self.addExperiment(
                container,line_8,'IIdefinition',self._5E.value(),'No',self._5G,self._5H,'No'))
        
        ###### Place conatainer attribuates #######
        l_container = QtGui.QVBoxLayout()
        spacer = QtGui.QHBoxLayout()
        self.add_widget_to_layout(['stretch'],spacer)
        line_1 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_1,'stretch'],line_1)
        line_2 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_2,self._5A,self.slider_5A,'stretch'],line_2)
        line_3 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_3,self._5B,self.slider_5B,'stretch'],line_3)
        line_4 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_4,self._5C,self._5D,self.slider_5D,'stretch'],line_4)
        line_5 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([QHLine()],line_5)
        line_6 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_5,self._5E,'stretch'],line_6)
        line_7 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_6,self._5F,'stretch'],line_7)
        
        
        self.add_layout_to_layout([line_1,line_2,line_3,line_4,'stretch',line_5,line_6,line_7,line_8],l_container)
        container.setLayout(l_container)
        #####################################
        l_scroll.addWidget(container)  #link 4th to 3rd
        scrollArea.setLayout(l_scroll) # and layout
        l_IIdefinition.addWidget(scrollArea) #link 3rd to 2nd
        self.IIdefinition.setLayout(l_IIdefinition)  # and layout
        self.task.addTab(self.IIdefinition, "IIdefinition") #link 2nd to 1st creating a new tab
        
    def generate_tabIIingenes(self):
        self.IIingenes = QtGui.QFrame()#2nd 
        l_IIingenes = QtGui.QGridLayout() #layout 2nd
        
        scrollArea = QtGui.QScrollArea(self.IIingenes) #3rd
        scrollArea.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidgetResizable(True)
        l_scroll = QtGui.QGridLayout(scrollArea) #layout 3rd 
        
        container = QtGui.QWidget(scrollArea) #4th
        container.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidget(container) #link 4th to 3rd =>provides to container to scroll
        ####Add here container attributes####
        l_container = QtGui.QVBoxLayout()
        label_1 = QtGui.QLabel('Classification of I.I. in genes',container)
        label_1.setFont(QtGui.QFont("",20,QtGui.QFont.Bold))
        label_2 = QtGui.QLabel('Location of gene reference:\t',container)
        self._6A = QtGui.QLineEdit(container)
        self.tool_6A = QtGui.QToolButton(container)
        self.tool_6A.setIcon(QtGui.QIcon(QtGui.QPixmap("icons/open.png")))
        self.tool_6A.clicked.connect(lambda: self.getfile(self._6A))
        label_3 = QtGui.QLabel('Type of parameters analysed',container)
        label_4 = QtGui.QLabel(' 1) Independent insertions (I.I.):\t',container)
        self._6B = QtGui.QCheckBox(container)
        label_5 = QtGui.QLabel(' 2) Killing insertions (K.I.):\t\t',container)
        self._6C = QtGui.QCheckBox(container)
        label_6 = QtGui.QLabel(' 3) Bias insertions:\t\t',container)
        self._6D = QtGui.QCheckBox(container)
        label_7 = QtGui.QLabel(' 4) Reads:\t\t\t',container)
        self._6E = QtGui.QCheckBox(container)
        
        label_8 = QtGui.QLabel('Numbers of libraries to analyse:\t\t',container)
        label_9 = QtGui.QLabel('Are libreries sequenced pair-end?\t\t',container)
        self._6F = QtGui.QSpinBox(container)
        self._6F.setRange(0,100)
        self._6F.setValue(1)
        self._6G = QtGui.QComboBox(container)
        self._6G.addItems(['Yes','No'])
        
        #Creates a QGridLayout where to store position of libraries location created in addExperiment function
        line_11 = QtGui.QGridLayout()
        
        self._6H = []
        self._6I = []
        
        self.experimentCount['IIingenes'] = 0
        self.pairEndWidgets['IIingenes'] = []
        label_10 = QtGui.QLabel('Name of the libraries',container)
        label_11= QtGui.QLabel('Location of file',container)
        label_12= QtGui.QLabel('Location of file P7',container)
        self.add_widget_to_gridlayout([(label_10,0,3,1,2),(label_11,0,5,1,1),(label_12,0,7,1,1)],
                                       line_11)
        self.pairEndWidgets['IIingenes'].append(line_11.count()-1)
        container,line_11 = self.addExperiment(
                container,line_11,'IIingenes',self._6F.value(),'No',self._6H,self._6I,'No')
        self._6F.valueChanged.connect(lambda : self.addExperiment(
                container,line_11,'IIingenes',self._6F.value(),'No',self._6H,self._6I,'No'))
        
        ###### Place conatainer attribuates #######
        l_container = QtGui.QVBoxLayout()
        spacer = QtGui.QHBoxLayout()
        self.add_widget_to_layout(['stretch'],spacer)
        line_1 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_1,'stretch'],line_1)
        line_2 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_2,self._6A,self.tool_6A],line_2)
        line_3 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_3,'stretch'],line_3)
        line_4 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_4,self._6B,'stretch'],line_4)
        line_5 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_5,self._6C,'stretch'],line_5)
        line_6 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_6,self._6D,'stretch'],line_6)
        line_7 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_7,self._6E,'stretch'],line_7)
        
        line_8 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([QHLine()],line_8)
        line_9 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_8,self._6F,'stretch'],line_9)
        line_10 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_9,self._6G,'stretch'],line_10)
        
        
        self.add_layout_to_layout([line_1,line_2,line_3,line_4,line_5,line_6,line_7,'stretch',line_8,line_9,line_10,line_11],l_container)
        container.setLayout(l_container)
        #####################################
        l_scroll.addWidget(container)  #link 4th to 3rd
        scrollArea.setLayout(l_scroll) # and layout
        l_IIingenes.addWidget(scrollArea) #link 3rd to 2nd
        self.IIingenes.setLayout(l_IIingenes)  # and layout
        self.task.addTab(self.IIingenes, "IIingenes")
        
    def generate_tabAnalysis(self):
        ####
        def addLibraries(self,group,l_group,task,newNumberLine,labelsList,librariesList):
            ####
            def storeValue(group,index,value):
                group[index]= value
            ####
            while self.experimentCount[task] != newNumberLine:
                n = self.experimentCount[task] +1
                if self.experimentCount[task] < newNumberLine:
                    if len(labelsList)<= n:
                        labelsList.append('')
                        librariesList.append('')
                    label = QtGui.QLabel('%i)'%n,group)
                    libraryName = QtGui.QLineEdit(labelsList[n-1],group)
                    inputFirst = QtGui.QLineEdit(librariesList[n-1],group)
                    tool_inputFirst = QtGui.QToolButton(group)
                    tool_inputFirst.setIcon(QtGui.QIcon(QtGui.QPixmap("icons/select.png")))
                    tool_inputFirst.clicked.connect(lambda: dialogs.selectLibraries(self,inputFirst)) 
            
                    self.add_widget_to_gridlayout([(label,int((n*2)+1),4,1,1),
                                           (libraryName,int((n*2)+1),5,1,1),(inputFirst,int((n*2)+1),7,1,1),(tool_inputFirst,int((n*2)+1),8,1,1)
                                           ],l_group)
                    libraryName.editingFinished.connect(lambda: storeValue(labelsList,n-1,str(libraryName.text())))
                    inputFirst.textChanged.connect(lambda: storeValue(librariesList,n-1,str(inputFirst.text())))
                    self.experimentCount[task] +=1
                else:
                    for x in range(4):
                        item = l_group.takeAt(l_group.count()-1)
                        widget = item.widget()
                        widget.deleteLater()
                    del labelsList[n-2]
                    del librariesList[n-2]
                    self.experimentCount[task] -=1
        ####
            
        
        self.Analysis = QtGui.QFrame()#2nd 
        l_Analysis = QtGui.QGridLayout() #layout 2nd
        
        scrollArea = QtGui.QScrollArea(self.Analysis) #3rd
        scrollArea.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidgetResizable(True)
        l_scroll = QtGui.QGridLayout(scrollArea) #layout 3rd 
        
        container =  QtGui.QWidget(scrollArea) #4th
        container.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidget(container) #link 4th to 3rd =>provides to container to scroll
        ####Add here container attributes####
        l_container = QtGui.QVBoxLayout()
        label_1 = QtGui.QLabel('Analysis of experiment',container)
        label_1.setFont(QtGui.QFont("",20,QtGui.QFont.Bold))
        label_2 = QtGui.QLabel('Number of group to analyse:\t',container)
        self._7A = QtGui.QSpinBox(container)
        self._7A.setRange(0,100)
        self._7A.setValue(0)
        
        ##
        line_3 = QtGui.QGridLayout()
        self.experimentCount['AnalysisGroup'] = 0
        label_3 = QtGui.QLabel('Name',container)
        label_4= QtGui.QLabel('Libraries in group',container)
        label_5= QtGui.QLabel('Reference group:',container)
        self._7B = QtGui.QLineEdit(container)
        self._7C = QtGui.QLineEdit(container)
        self.push_7B = QtGui.QToolButton(container)
        self.push_7B.setIcon(QtGui.QIcon(QtGui.QPixmap("icons/select.png")))
        self.push_7B.clicked.connect(lambda: dialogs.selectLibraries(self,self._7C)) 
        
        label_6 = QtGui.QLabel('Analysed groups :',container)
        self.add_widget_to_gridlayout([(label_3,0,5,1,1),(label_4,0,7,1,1),
                                       (label_5,1,3,1,2),(self._7B,1,5,1,1),(self._7C,1,7,1,1),(self.push_7B,1,8,1,1),
                                       (label_6,2,3,1,2)],
                                       line_3)
        
        self._7D = []
        self._7E = []
        self._7A.valueChanged.connect(lambda : addLibraries(self,
                container,line_3,'AnalysisGroup',self._7A.value(),self._7D,self._7E))
        
        ##
        label_space = QtGui.QLabel('\t\t\t',container)
        label_7 =  QtGui.QLabel('Parameters analysed :\t',container)
        self._7F = QtGui.QCheckBox('I.I.',container)
        self._7G = QtGui.QCheckBox('K.I.',container)
        self._7H = QtGui.QCheckBox('Bias.',container)
        self._7I = QtGui.QCheckBox('Reads',container)
        
        label_8 =  QtGui.QLabel('Perform Outlier analysis :\t\t',container)
        self._7J = QtGui.QComboBox(container)
        self._7J.addItems(['Yes','No'])
        label_9 = QtGui.QLabel('- Approach for analysis :\t',container)
        self._7K = QtGui.QCheckBox('Fold',container)
        self._7L = QtGui.QCheckBox('Rank',container)
        label_10 = QtGui.QLabel('- Parameters analysed :\t', container)
        self._7M = QtGui.QCheckBox('I.I.',container)
        self._7N = QtGui.QCheckBox('K.I.',container)
        self._7O = QtGui.QCheckBox('Bias.',container)
        self._7P = QtGui.QCheckBox('Reads',container)
        label_11 = QtGui.QLabel('- Confidence value of I.I. :\t\t\n     per gene', container)
        self._7Q = QtGui.QSpinBox(container)
        self._7Q.setRange(1,100)
        self._7Q.setValue(1)
        self.slider_7Q = QtGui.QSlider(QtCore.Qt.Horizontal,container)
        self.slider_7Q.setRange(1,100)
        self.slider_7Q.setValue(1)
        self._7Q.valueChanged.connect(self.slider_7Q.setValue)
        self.slider_7Q.valueChanged.connect(self._7Q.setValue)
        
        ###
        label_12 = QtGui.QLabel('Numbers of libraries to analyse:\t',container)
        self._7R = QtGui.QSpinBox(container)
        self._7R.setRange(1,100)
        self._7R.setValue(1)
        
        line_18 = QtGui.QGridLayout()
        
        self._7S = []
        self._7T = []
        
        self.experimentCount['Analysis'] = 0
        self.pairEndWidgets['Analysis'] = []
        label_13 = QtGui.QLabel('Name of the libraries',container)
        label_14= QtGui.QLabel('Location of file',container)
        label_15= QtGui.QLabel('Location of file P7',container)
        self.add_widget_to_gridlayout([(label_13,0,3,1,2),(label_14,0,5,1,1),(label_15,0,7,1,1)],
                                       line_18)
        self.pairEndWidgets['Analysis'].append(line_18.count()-1)
        container,line_11 = self.addExperiment(
                container,line_18,'Analysis',self._7R.value(),'No',self._7S,self._7T,'No')
        self._7R.valueChanged.connect(lambda : self.addExperiment(
                container,line_18,'IIingenes',self._7R.value(),'No',self._7S,self._7T,'No'))
        ######Deactivation commands ###############
        self._7J.currentIndexChanged.connect(lambda: self.deactivate([self._7K,self._7L,self._7M,
                                                                      self._7N,self._7O,self._7P,
                                                                      self._7Q,self.slider_7Q],self._7J))
            
        
        ###### Place conatainer attribuates #######
        l_container = QtGui.QVBoxLayout()
        spacer = QtGui.QHBoxLayout()
        self.add_widget_to_layout(['stretch'],spacer)
        line_1 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_1,'stretch'],line_1)
        line_2 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_2,self._7A,'stretch'],line_2)

        line_4 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_7,self._7F,'stretch'],line_4)
        line_5 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_space,self._7G,'stretch'],line_5)
        line_6 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_space,self._7H,'stretch'],line_6)
        line_7 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_space,self._7I,'stretch'],line_7)
        
        line_8 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_8,self._7J,'stretch'],line_8)
        line_9 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_9,self._7K,'stretch'],line_9)
        line_10 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_space,self._7L,'stretch'],line_10)
        line_11 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_10,self._7M,'stretch'],line_11)
        line_12 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_space,self._7N,'stretch'],line_12)
        line_13 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_space,self._7O,'stretch'],line_13)
        line_14 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_space,self._7P,'stretch'],line_14)
        line_15 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_11,self._7Q,self.slider_7Q,'stretch'],line_15)
        line_16 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([QHLine()],line_16)
        line_17 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_12,self._7R,'stretch'],line_17)              
        self.add_layout_to_layout([line_1,line_2,line_3,line_4,line_5,line_6,line_7,
                                   line_8,line_9,line_10,line_11,
                                   line_12,line_13,line_14,line_15,line_16,line_17,line_18],l_container)
        container.setLayout(l_container)
        
        #####################################
        l_scroll.addWidget(container)  #link 4th to 3rd
        scrollArea.setLayout(l_scroll) # and layout
        l_Analysis.addWidget(scrollArea) #link 3rd to 2nd
        self.Analysis.setLayout(l_Analysis)  # and layout
        self.task.addTab(self.Analysis, "Analysis")
        
        
    def generate_tabTables(self):
        ####
        def addTables(self,group,l_group,task,newNumberLine,namesList,headersList,filtersList):
            ####
            def storeValue(group,index,value):
                group[index] = value
            ####    
            while self.experimentCount[task] != newNumberLine:
                n = self.experimentCount[task] +1
                if self.experimentCount[task] < newNumberLine:
                    if len (namesList) <= n:
                        namesList.append('')
                        headersList.append('')
                        filtersList.append('')
                    
                    label = QtGui.QLabel('%i)'%n,group)
                    tableName = QtGui.QLineEdit(namesList[n-1],group)
                    headers = QtGui.QLineEdit(headersList[n-1],group)
                    tool_headers = QtGui.QToolButton(group)
                    tool_headers.setIcon(QtGui.QIcon(QtGui.QPixmap("icons/table.png")))
                    tool_headers.clicked.connect(lambda: dialogs.headerSelection(self,headers)) 
                    filters = QtGui.QLineEdit(filtersList[n-1],group)
                    tool_filters = QtGui.QToolButton(group)
                    tool_filters.setIcon(QtGui.QIcon(QtGui.QPixmap("icons/filter.png")))
                    tool_filters.clicked.connect(lambda: dialogs.filterSelection(self,filters)) 
            
                    self.add_widget_to_gridlayout([(label,int((n*2)+1),1,1,1),
                                           (tableName,int((n*2)+1),2,1,2),(headers,int((n*2)+1),4,1,1),(tool_headers,int((n*2)+1),5,1,1),
                                           (filters,int((n*2)+1),6,1,1),(tool_filters,int((n*2)+1),7,1,1)
                                           ],l_group)
                    
                    tableName.editingFinished.connect(lambda: storeValue(namesList,n-1,str(tableName.text())))
                    headers.textChanged.connect(lambda: storeValue(headersList,n-1,str(headers.text())))
                    filters.textChanged.connect(lambda: storeValue(filtersList,n-1,str(filters.text())))
                    
                    self.experimentCount[task] +=1
                    
                else:
                    for x in range(6):
                        item = l_group.takeAt(l_group.count()-1)
                        widget = item.widget()
                        widget.deleteLater()
                    del namesList[n-2]
                    del headersList[n-2]
                    del filtersList[n-2]
                    
                    self.experimentCount[task] -=1
            return group, l_group
        ####
        
        self.Tables = QtGui.QFrame()#2nd 
        l_Tables = QtGui.QGridLayout() #layout 2nd
        
        scrollArea = QtGui.QScrollArea(self.Tables) #3rd
        scrollArea.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidgetResizable(True)
        l_scroll = QtGui.QGridLayout(scrollArea) #layout 3rd 
        container = QtGui.QWidget(scrollArea) #4th
        container.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidget(container) #link 4th to 3rd =>provides to container to scroll
        ####Add here container attributes####
        l_container = QtGui.QVBoxLayout()
        label_1 = QtGui.QLabel('Defyining Tables',container)
        label_1.setFont(QtGui.QFont("",20,QtGui.QFont.Bold))
        label_2 = QtGui.QLabel('Number of Tables to generate:\t',container)
        self._8A = QtGui.QSpinBox(container)
        self._8A.setRange(0,100)
        self._8A.setValue(1)
        
        line_3 = QtGui.QGridLayout()
        self._8B = []
        self._8C = []
        self._8D = []
        
        self.experimentCount['TablesGroup'] = 0
        label_3 = QtGui.QLabel('Name of the tables',container)
        label_4= QtGui.QLabel('Headers',container)
        label_5= QtGui.QLabel('Filters',container)
        self.add_widget_to_gridlayout([(label_3,0,2,1,2),(label_4,0,4,1,1),(label_5,0,6,1,1)],line_3)
        container,line_3 = addTables(self,container,line_3,'TablesGroup',self._8A.value(),
                                     self._8B,self._8C,self._8D)
        self._8A.valueChanged.connect(lambda : addTables(self,
                container,line_3,'TablesGroup',self._8A.value(),self._8B,self._8C,self._8D))
        
        label_6 = QtGui.QLabel('Location of GroupAnalysis file :\t',container)
        self._8E = QtGui.QLineEdit(container)
        self.tool_8E = QtGui.QToolButton(container)
        self.tool_8E.setIcon(QtGui.QIcon(QtGui.QPixmap("icons/open.png")))
        self.tool_8E.clicked.connect(lambda: self.getfile(self._8E))
        
        
        ###### Place conatainer attribuates #######
        l_container = QtGui.QVBoxLayout()
        spacer = QtGui.QHBoxLayout()
        self.add_widget_to_layout(['stretch'],spacer)
        line_1 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_1,'stretch'],line_1)
        line_2 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_2,self._8A,'stretch'],line_2)
        line_4 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([QHLine()],line_4)
        line_5 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_6,self._8E,self.tool_8E],line_5)
        
        self.add_layout_to_layout([line_1,line_2,line_3,'stretch',line_4,line_5],l_container)
        container.setLayout(l_container)
        #####################################
        l_scroll.addWidget(container)  #link 4th to 3rd
        scrollArea.setLayout(l_scroll) # and layout
        l_Tables.addWidget(scrollArea) #link 3rd to 2nd
        self.Tables.setLayout(l_Tables)  # and layout
        self.task.addTab(self.Tables, "Tables") #link 2nd to 1st creating a new tab
    
    
    def generate_tabDesign(self):
        self.Design = QtGui.QFrame()#2nd 
        l_Design = QtGui.QGridLayout() #layout 2nd
        
        scrollArea = QtGui.QScrollArea(self.Phix) #3rd
        scrollArea.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidgetResizable(True)
        l_scroll = QtGui.QGridLayout(scrollArea) #layout 3rd 
        
        container = QtGui.QWidget(scrollArea) #4th
        container.setGeometry(QtCore.QRect(24, 12, 231, 81))
        scrollArea.setWidget(container) #link 4th to 3rd =>provides to container to scroll
        
        ####Add here container attributes####
        l_container = QtGui.QVBoxLayout()
        label_space = QtGui.QLabel('\t\t\t\t',container)
        
        label_1 = QtGui.QLabel('Graphs',container)
        label_1.setFont(QtGui.QFont("",20,QtGui.QFont.Bold))
        label_2 = QtGui.QLabel('Type of graph to generate :\t',container)
        self._9A = QtGui.QCheckBox('I.I. in gene models',container)
        self._9A.setChecked(True)
        self._9B = QtGui.QCheckBox('Genes distribution',container)
        self._9B.setChecked(True)
        label_3 = QtGui.QLabel('I.I. in gene models',container)
        label_3.setFont(QtGui.QFont("",12,QtGui.QFont.Bold))
        label_4 = QtGui.QLabel('Location  of reference genome :\t',container)
        self._9C = QtGui.QLineEdit(container)
        self.tool_9C = QtGui.QToolButton(container)
        self.tool_9C.setIcon(QtGui.QIcon(QtGui.QPixmap("icons/open.png")))
        self.tool_9C.clicked.connect(lambda: self.getfile(self._9C))
        label_5 = QtGui.QLabel('Genes (or intervals) to analyse :\t',container)
        self._9D = QtGui.QLineEdit(container)
        label_6 = QtGui.QLabel('Genes distribution with LOF analysis',container)
        label_6.setFont(QtGui.QFont("",12,QtGui.QFont.Bold))
        label_7 = QtGui.QLabel('Highlight outliers :\t\t\t',container)
        self._9E = QtGui.QComboBox(container)
        self._9E.addItems(['Yes','No'])
        label_8 = QtGui.QLabel('Starting Outlier value :\t\t',container)
        self._9F = QtGui.QSpinBox(container)
        self._9F.setRange(1,100)
        self._9F.setValue(1)
        self.slider_9F = QtGui.QSlider(QtCore.Qt.Horizontal,container)
        self.slider_9F.setRange(1,100)
        self.slider_9F.setValue(1)
        self._9F.valueChanged.connect(self.slider_9F.setValue)
        self.slider_9F.valueChanged.connect(self._9F.setValue)
        label_9 = QtGui.QLabel('Annotate gene names :\t\t',container)
        self._9G = QtGui.QComboBox(container)
        self._9G.addItems(['Yes','No'])
        label_10 = QtGui.QLabel('Genes listo to annotate :\t\t\n(or Outlier value)  ',container)
        self._9H = QtGui.QLineEdit(container)
        label_11 = QtGui.QLabel('Location of GroupAnalysis file :\t',container)
        self._9I = QtGui.QLineEdit(container)
        self.tool_9I = QtGui.QToolButton(container)
        self.tool_9I.setIcon(QtGui.QIcon(QtGui.QPixmap("icons/open.png")))
        self.tool_9I.clicked.connect(lambda: self.getfile(self._9J))
        
        ######Deactivation commands ###############
        self._9A.clicked.connect(lambda: self.deactivate([label_3,label_4,self._9C,self.tool_9C,
                                                          label_5,self._9D],self._9A))
        self._9B.clicked.connect(lambda: self.deactivate([label_6,label_7,self._9E,label_8,self._9F,self.slider_9F,
                                                          label_9,self._9G,label_10,self._9H],self._9B))
        self._9E.currentIndexChanged.connect(lambda: self.deactivate([self._9F,self.slider_9F],self._9E))
        self._9G.currentIndexChanged.connect(lambda: self.deactivate([self._9H],self._9G))
        
        ###### Place conatainer attribuates #######
        l_container = QtGui.QVBoxLayout()
        spacer = QtGui.QHBoxLayout()
        self.add_widget_to_layout(['stretch'],spacer)
        line_1 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_1,'stretch'],line_1)
        line_2 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_2,self._9A,'stretch'],line_2)
        line_3 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_space,self._9B,'stretch'],line_3)
        line_4 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_3],line_4)
        line_5 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_4,self._9C,self.tool_9C],line_5)
        line_6 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_5,self._9D],line_6)
        line_7 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_6,'stretch'],line_7)
        line_8 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_7,self._9E,'stretch'],line_8)
        line_9 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_8,self._9F,self.slider_9F,'stretch'],line_9)
        line_10 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_9,self._9G,'stretch'],line_10)
        line_11 = QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_10,self._9H],line_11)
        line_12= QtGui.QHBoxLayout()
        self.add_widget_to_layout([QHLine()],line_12)
        line_13= QtGui.QHBoxLayout()
        self.add_widget_to_layout([label_11,self._9I,self.tool_9I],line_13)
        self.add_layout_to_layout([line_1,line_2,line_3,line_4,line_5,line_6,
                                   line_7,line_8,line_9,line_10,line_11,
                                   'stretch',line_12,line_13],l_container)
        
        container.setLayout(l_container)
        #####################################
        l_scroll.addWidget(container)  #link 4th to 3rd
        scrollArea.setLayout(l_scroll) # and layout
        l_Design.addWidget(scrollArea) #link 3rd to 2nd
        self.Design.setLayout(l_Design)  # and layout
        self.task.addTab(self.Design, "Graphs") #link 2nd to 1st creating a new tab
        
        

        
        
        
        
        
        
        



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()  
     
