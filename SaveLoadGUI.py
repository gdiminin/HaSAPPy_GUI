#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#===================================================================
# Module with functions to save & restore qt widget values
# Written by: Alan Lilly 
# Website: http://panofish.net
#===================================================================

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import inspect
from distutils.util import strtobool

#===================================================================
# save "ui" controls and values to registry "setting"
# currently only handles comboboxes editlines & checkboxes
# ui = qmainwindow object
# settings = qsettings object
#===================================================================



def guisave(self):

  # Save geometry
    self.settings.setValue('size', self.size())
    self.settings.setValue('pos', self.pos())

    for name, obj in inspect.getmembers(self):
      # if type(obj) is QComboBox:  # this works similar to isinstance, but missed some field... not sure why?
      if isinstance(obj, QComboBox):
          name = obj.objectName()  # get combobox name
          index = obj.currentIndex()  # get current index from combobox
          text = obj.itemText(index)  # get the text for current index
          self.settings.setValue(name, text)  # save combobox selection to registry
          print index,text

      if isinstance(obj, QLineEdit):
          name = obj.objectName()
          value = obj.text()
          self.settings.setValue(name, value)# save ui values, so they can be restored next time
          print name,value

      if isinstance(obj, QCheckBox):
          name = obj.objectName()
          state = obj.isChecked()
          self.settings.setValue(name, state)

      if isinstance(obj, QRadioButton):
          name = obj.objectName()
          value = obj.isChecked()  # get stored value from registry
          self.settings.setValue(name, value)
      if isinstance(obj, QSpinBox):
          name  = obj.objectName()
          value = obj.value()             # get stored value from registry
          self.settings.setValue(name, value)

      if isinstance(obj, QSlider):
          name  = obj.objectName()
          value = obj.value()             # get stored value from registry
          self.settings.setValue(name, value)
          
      if isinstance(obj, QListWidget):
          name = obj.objectName()
          self.settings.beginWriteArray(name)
          for i in range(obj.count()):
              self.settings.setArrayIndex(i)
              self.settings.setValue(name, obj.item(i).text())
          self.settings.endArray()
          
      
         



def guirestore(self):

  # Restore geometry  
#  self.resize(self.settings.value('size', QSize(500, 500)))
#  self.move(self.settings.value('pos', QPoint(60, 60)))

  for name, obj in inspect.getmembers(self):
      if isinstance(obj, QComboBox):
          index = obj.currentIndex()  # get current region from combobox
          # text   = obj.itemText(index)   # get the text for new selected index
          name = obj.objectName()

          value = unicode(self.settings.value(name).toString())

          if value == "":
              continue

          index = obj.findText(value)  # get the corresponding index for specified string in combobox

          if index == -1:  # add to list if not found
              obj.insertItems(0, [value])
              index = obj.findText(value)
              obj.setCurrentIndex(index)
          else:
              obj.setCurrentIndex(index)  # preselect a combobox value by index

      if isinstance(obj, QLineEdit):
          name = obj.objectName()
          value = unicode(self.settings.value(name).toString())  # get stored value from registry
          obj.setText(value)  # restore lineEditFile

      if isinstance(obj, QCheckBox):
          name = obj.objectName()
          value = unicode(self.settings.value(name).toString())  # get stored value from registry
          if value != None:
              obj.setChecked(strtobool(value))  # restore checkbox

      if isinstance(obj, QRadioButton):
         name = obj.objectName()
         value = unicode(self.settings.value(name).toString())  # get stored value from registry
         if value != None:
             obj.setChecked(value)

      if isinstance(obj, QSlider):
          name = obj.objectName()
          value = unicode(self.settings.value(name).toString())    # get stored value from registry
          if value != None:           
              obj. setValue(int(value))   # restore value from registry

      if isinstance(obj, QSpinBox):
          name = obj.objectName()
          value = unicode(self.settings.value(name).toString())    # get stored value from registry
          if value != None:
              obj. setValue(int(value))   # restore value from registry
      
      if isinstance(obj, QListWidget):
          name = obj.objectName()
          size = self.settings.beginReadArray(name)
          for i in range(size):
              self.settings.setArrayIndex(i)
              value = unicode(self.settings.value(name).toString())  # get stored value from registry
              if value != None:
                  obj.addItem(value)
          self.settings.endArray()
          