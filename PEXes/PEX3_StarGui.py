# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/C18Jaren.Lynch/PycharmProjects/usafa_cs210_2015/PEXes/PEX3_StarGui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PEX3_StarGui(object):
    def setupUi(self, PEX3_StarGui):
        PEX3_StarGui.setObjectName(_fromUtf8("PEX3_StarGui"))
        PEX3_StarGui.resize(681, 573)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        PEX3_StarGui.setPalette(palette)
        self.centralwidget = QtGui.QWidget(PEX3_StarGui)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.window_layout = QtGui.QHBoxLayout(self.centralwidget)
        self.window_layout.setObjectName(_fromUtf8("window_layout"))
        self.main_layout = QtGui.QHBoxLayout()
        self.main_layout.setObjectName(_fromUtf8("main_layout"))
        self.drawing_widget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.drawing_widget.sizePolicy().hasHeightForWidth())
        self.drawing_widget.setSizePolicy(sizePolicy)
        self.drawing_widget.setMinimumSize(QtCore.QSize(512, 512))
        self.drawing_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.drawing_widget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(12)
        self.drawing_widget.setFont(font)
        self.drawing_widget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.drawing_widget.setAutoFillBackground(True)
        self.drawing_widget.setObjectName(_fromUtf8("drawing_widget"))
        self.main_layout.addWidget(self.drawing_widget)
        self.vertical_line = QtGui.QFrame(self.centralwidget)
        self.vertical_line.setFrameShape(QtGui.QFrame.VLine)
        self.vertical_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.vertical_line.setObjectName(_fromUtf8("vertical_line"))
        self.main_layout.addWidget(self.vertical_line)
        self.controls_layout = QtGui.QVBoxLayout()
        self.controls_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.controls_layout.setMargin(8)
        self.controls_layout.setObjectName(_fromUtf8("controls_layout"))
        spacerItem = QtGui.QSpacerItem(128, 16777215, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.controls_layout.addItem(spacerItem)
        self.TopLine = QtGui.QFrame(self.centralwidget)
        self.TopLine.setFrameShape(QtGui.QFrame.HLine)
        self.TopLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.TopLine.setObjectName(_fromUtf8("TopLine"))
        self.controls_layout.addWidget(self.TopLine)
        self.Constellation_layout = QtGui.QVBoxLayout()
        self.Constellation_layout.setObjectName(_fromUtf8("Constellation_layout"))
        self.Constellation = QtGui.QLabel(self.centralwidget)
        self.Constellation.setMaximumSize(QtCore.QSize(128, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Constellation.setFont(font)
        self.Constellation.setObjectName(_fromUtf8("Constellation"))
        self.Constellation_layout.addWidget(self.Constellation)
        self.none_button = QtGui.QRadioButton(self.centralwidget)
        self.none_button.setMaximumSize(QtCore.QSize(128, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.none_button.setFont(font)
        self.none_button.setChecked(False)
        self.none_button.setObjectName(_fromUtf8("none_button"))
        self.ConstellationGroup = QtGui.QButtonGroup(PEX3_StarGui)
        self.ConstellationGroup.setObjectName(_fromUtf8("ConstellationGroup"))
        self.ConstellationGroup.addButton(self.none_button)
        self.Constellation_layout.addWidget(self.none_button)
        self.BigDipper = QtGui.QRadioButton(self.centralwidget)
        self.BigDipper.setMaximumSize(QtCore.QSize(128, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BigDipper.setFont(font)
        self.BigDipper.setObjectName(_fromUtf8("BigDipper"))
        self.ConstellationGroup.addButton(self.BigDipper)
        self.Constellation_layout.addWidget(self.BigDipper)
        self.Bootes = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Bootes.setFont(font)
        self.Bootes.setChecked(True)
        self.Bootes.setObjectName(_fromUtf8("Bootes"))
        self.ConstellationGroup.addButton(self.Bootes)
        self.Constellation_layout.addWidget(self.Bootes)
        self.Cassiopeia = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cassiopeia.setFont(font)
        self.Cassiopeia.setObjectName(_fromUtf8("Cassiopeia"))
        self.ConstellationGroup.addButton(self.Cassiopeia)
        self.Constellation_layout.addWidget(self.Cassiopeia)
        self.Cygnet = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cygnet.setFont(font)
        self.Cygnet.setObjectName(_fromUtf8("Cygnet"))
        self.ConstellationGroup.addButton(self.Cygnet)
        self.Constellation_layout.addWidget(self.Cygnet)
        self.Gemini = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Gemini.setFont(font)
        self.Gemini.setObjectName(_fromUtf8("Gemini"))
        self.ConstellationGroup.addButton(self.Gemini)
        self.Constellation_layout.addWidget(self.Gemini)
        self.Hydra = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Hydra.setFont(font)
        self.Hydra.setObjectName(_fromUtf8("Hydra"))
        self.ConstellationGroup.addButton(self.Hydra)
        self.Constellation_layout.addWidget(self.Hydra)
        self.UrsaMajor = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.UrsaMajor.setFont(font)
        self.UrsaMajor.setObjectName(_fromUtf8("UrsaMajor"))
        self.ConstellationGroup.addButton(self.UrsaMajor)
        self.Constellation_layout.addWidget(self.UrsaMajor)
        self.UrsaMinor = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.UrsaMinor.setFont(font)
        self.UrsaMinor.setObjectName(_fromUtf8("UrsaMinor"))
        self.ConstellationGroup.addButton(self.UrsaMinor)
        self.Constellation_layout.addWidget(self.UrsaMinor)
        self.controls_layout.addLayout(self.Constellation_layout)
        self.BottomLine = QtGui.QFrame(self.centralwidget)
        self.BottomLine.setFrameShape(QtGui.QFrame.HLine)
        self.BottomLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.BottomLine.setObjectName(_fromUtf8("BottomLine"))
        self.controls_layout.addWidget(self.BottomLine)
        spacerItem1 = QtGui.QSpacerItem(128, 16777215, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.controls_layout.addItem(spacerItem1)
        self.main_layout.addLayout(self.controls_layout)
        self.window_layout.addLayout(self.main_layout)
        PEX3_StarGui.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PEX3_StarGui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        self.menu_Star = QtGui.QMenu(self.menubar)
        self.menu_Star.setObjectName(_fromUtf8("menu_Star"))
        self.menu_Map = QtGui.QMenu(self.menubar)
        self.menu_Map.setObjectName(_fromUtf8("menu_Map"))
        PEX3_StarGui.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PEX3_StarGui)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PEX3_StarGui.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(PEX3_StarGui)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(PEX3_StarGui)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(PEX3_StarGui)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.action_save = QtGui.QAction(PEX3_StarGui)
        self.action_save.setObjectName(_fromUtf8("action_save"))
        self.action_exit = QtGui.QAction(PEX3_StarGui)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.action_insert_vertex = QtGui.QAction(PEX3_StarGui)
        self.action_insert_vertex.setObjectName(_fromUtf8("action_insert_vertex"))
        self.action_insert_edge = QtGui.QAction(PEX3_StarGui)
        self.action_insert_edge.setObjectName(_fromUtf8("action_insert_edge"))
        self.action_about = QtGui.QAction(PEX3_StarGui)
        self.action_about.setObjectName(_fromUtf8("action_about"))
        self.action_new = QtGui.QAction(PEX3_StarGui)
        self.action_new.setObjectName(_fromUtf8("action_new"))
        self.action_node = QtGui.QAction(PEX3_StarGui)
        self.action_node.setObjectName(_fromUtf8("action_node"))
        self.action_edge = QtGui.QAction(PEX3_StarGui)
        self.action_edge.setObjectName(_fromUtf8("action_edge"))
        self.action_open = QtGui.QAction(PEX3_StarGui)
        self.action_open.setObjectName(_fromUtf8("action_open"))
        self.action_save_image = QtGui.QAction(PEX3_StarGui)
        self.action_save_image.setObjectName(_fromUtf8("action_save_image"))
        self.action_find_by_name = QtGui.QAction(PEX3_StarGui)
        self.action_find_by_name.setObjectName(_fromUtf8("action_find_by_name"))
        self.action_name = QtGui.QAction(PEX3_StarGui)
        self.action_name.setObjectName(_fromUtf8("action_name"))
        self.action_draper = QtGui.QAction(PEX3_StarGui)
        self.action_draper.setObjectName(_fromUtf8("action_draper"))
        self.actionOpen_2 = QtGui.QAction(PEX3_StarGui)
        self.actionOpen_2.setObjectName(_fromUtf8("actionOpen_2"))
        self.action_Harvard_Revised_Number = QtGui.QAction(PEX3_StarGui)
        self.action_Harvard_Revised_Number.setObjectName(_fromUtf8("action_Harvard_Revised_Number"))
        self.menu_Help.addAction(self.action_about)
        self.menu_Star.addAction(self.action_name)
        self.menu_Star.addAction(self.action_draper)
        self.menu_Star.addAction(self.action_Harvard_Revised_Number)
        self.menu_Map.addAction(self.action_exit)
        self.menu_Map.addAction(self.actionOpen_2)
        self.menubar.addAction(self.menu_Map.menuAction())
        self.menubar.addAction(self.menu_Star.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(PEX3_StarGui)
        QtCore.QMetaObject.connectSlotsByName(PEX3_StarGui)

    def retranslateUi(self, PEX3_StarGui):
        PEX3_StarGui.setWindowTitle(_translate("PEX3_StarGui", "Stars", None))
        self.Constellation.setText(_translate("PEX3_StarGui", "Constellations", None))
        self.none_button.setText(_translate("PEX3_StarGui", "None", None))
        self.BigDipper.setText(_translate("PEX3_StarGui", "Big Dipper", None))
        self.Bootes.setText(_translate("PEX3_StarGui", "Bootes", None))
        self.Cassiopeia.setText(_translate("PEX3_StarGui", "Cassiopeia", None))
        self.Cygnet.setText(_translate("PEX3_StarGui", "Cygnet", None))
        self.Gemini.setText(_translate("PEX3_StarGui", "Gemini", None))
        self.Hydra.setText(_translate("PEX3_StarGui", "Hydra", None))
        self.UrsaMajor.setText(_translate("PEX3_StarGui", "Ursa Major", None))
        self.UrsaMinor.setText(_translate("PEX3_StarGui", "Ursa Minor", None))
        self.menu_Help.setTitle(_translate("PEX3_StarGui", "Help", None))
        self.menu_Star.setTitle(_translate("PEX3_StarGui", "Star", None))
        self.menu_Map.setTitle(_translate("PEX3_StarGui", "Map", None))
        self.actionOpen.setText(_translate("PEX3_StarGui", "Open...", None))
        self.actionSave.setText(_translate("PEX3_StarGui", "Save", None))
        self.actionSave_As.setText(_translate("PEX3_StarGui", "Save As...", None))
        self.action_save.setText(_translate("PEX3_StarGui", "Save...", None))
        self.action_exit.setText(_translate("PEX3_StarGui", "Exit", None))
        self.action_insert_vertex.setText(_translate("PEX3_StarGui", "Vertex...", None))
        self.action_insert_edge.setText(_translate("PEX3_StarGui", "Edge...", None))
        self.action_about.setText(_translate("PEX3_StarGui", "About", None))
        self.action_new.setText(_translate("PEX3_StarGui", "New", None))
        self.action_node.setText(_translate("PEX3_StarGui", "Node...", None))
        self.action_edge.setText(_translate("PEX3_StarGui", "Edge...", None))
        self.action_open.setText(_translate("PEX3_StarGui", "Open...", None))
        self.action_save_image.setText(_translate("PEX3_StarGui", "Save Image...", None))
        self.action_find_by_name.setText(_translate("PEX3_StarGui", "Find by Name...", None))
        self.action_name.setText(_translate("PEX3_StarGui", "Name", None))
        self.action_draper.setText(_translate("PEX3_StarGui", "Henry Draper Number", None))
        self.actionOpen_2.setText(_translate("PEX3_StarGui", "Open", None))
        self.action_Harvard_Revised_Number.setText(_translate("PEX3_StarGui", "Harvard Revised Number", None))

