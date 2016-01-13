# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yohann/Projets/CeGui-Debian/ceed-0.8.0/ceed/ui/editors/animation_list/AnimationListDockWidget.ui'
#
# Created: Wed Jan 13 23:35:01 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AnimationListDockWidget(object):
    def setupUi(self, AnimationListDockWidget):
        AnimationListDockWidget.setObjectName("AnimationListDockWidget")
        AnimationListDockWidget.setEnabled(True)
        AnimationListDockWidget.resize(290, 300)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.list = QtGui.QListWidget(self.dockWidgetContents)
        self.list.setObjectName("list")
        self.verticalLayout.addWidget(self.list)
        AnimationListDockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(AnimationListDockWidget)
        QtCore.QMetaObject.connectSlotsByName(AnimationListDockWidget)

    def retranslateUi(self, AnimationListDockWidget):
        AnimationListDockWidget.setWindowTitle(QtGui.QApplication.translate("AnimationListDockWidget", "List of animations", None, QtGui.QApplication.UnicodeUTF8))

