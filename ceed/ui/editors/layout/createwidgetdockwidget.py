# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yohann/Projets/CeGui-Debian/ceed-0.8.0/ceed/ui/editors/layout/CreateWidgetDockWidget.ui'
#
# Created: Wed Jan 13 23:35:01 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CreateWidgetDockWidget(object):
    def setupUi(self, CreateWidgetDockWidget):
        CreateWidgetDockWidget.setObjectName("CreateWidgetDockWidget")
        CreateWidgetDockWidget.setEnabled(False)
        CreateWidgetDockWidget.resize(290, 300)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tree = WidgetTypeTreeWidget(self.dockWidgetContents)
        self.tree.setObjectName("tree")
        self.verticalLayout.addWidget(self.tree)
        CreateWidgetDockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(CreateWidgetDockWidget)
        QtCore.QMetaObject.connectSlotsByName(CreateWidgetDockWidget)

    def retranslateUi(self, CreateWidgetDockWidget):
        CreateWidgetDockWidget.setWindowTitle(QtGui.QApplication.translate("CreateWidgetDockWidget", "Create new Widget", None, QtGui.QApplication.UnicodeUTF8))
        self.tree.setToolTip(QtGui.QApplication.translate("CreateWidgetDockWidget", "Drag to the layout to create", None, QtGui.QApplication.UnicodeUTF8))
        self.tree.headerItem().setText(0, QtGui.QApplication.translate("CreateWidgetDockWidget", "Name", None, QtGui.QApplication.UnicodeUTF8))

from ceed.editors.layout.visual import WidgetTypeTreeWidget
