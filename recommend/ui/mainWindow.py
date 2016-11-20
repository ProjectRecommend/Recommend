# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 600))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle("Offline Music Recommender")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/ic_main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(705, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Lists = QtWidgets.QGridLayout()
        self.Lists.setObjectName("Lists")
        self.RecommendLocal = QtWidgets.QTableView(self.centralwidget)
        self.RecommendLocal.setObjectName("RecommendLocal")
        self.Lists.addWidget(self.RecommendLocal, 0, 1, 1, 1)
        self.Playlist = QtWidgets.QTableView(self.centralwidget)
        self.Playlist.setObjectName("Playlist")
        self.Lists.addWidget(self.Playlist, 0, 0, 2, 1)
        self.RecommendOnline = QtWidgets.QTableView(self.centralwidget)
        self.RecommendOnline.setObjectName("RecommendOnline")
        self.Lists.addWidget(self.RecommendOnline, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.Lists, 0, 0, 1, 1)
        self.Player = QtWidgets.QGridLayout()
        self.Player.setObjectName("Player")
        self.Timeline = QtWidgets.QHBoxLayout()
        self.Timeline.setObjectName("Timeline")
        self.CurrentTime = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.CurrentTime.setFont(font)
        self.CurrentTime.setIndent(2)
        self.CurrentTime.setObjectName("CurrentTime")
        self.Timeline.addWidget(self.CurrentTime)
        self.ProgressBar = QtWidgets.QSlider(self.centralwidget)
        self.ProgressBar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ProgressBar.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.ProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.ProgressBar.setTickInterval(0)
        self.ProgressBar.setObjectName("ProgressBar")
        self.Timeline.addWidget(self.ProgressBar)
        self.TotalTime = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.TotalTime.setFont(font)
        self.TotalTime.setIndent(2)
        self.TotalTime.setObjectName("TotalTime")
        self.Timeline.addWidget(self.TotalTime)
        self.Player.addLayout(self.Timeline, 1, 0, 1, 1)
        self.SongInfoAndControls = QtWidgets.QGridLayout()
        self.SongInfoAndControls.setObjectName("SongInfoAndControls")
        self.SongArtist = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.SongArtist.setFont(font)
        self.SongArtist.setIndent(5)
        self.SongArtist.setObjectName("SongArtist")
        self.SongInfoAndControls.addWidget(self.SongArtist, 1, 1, 1, 1)
        self.PlayerControls = QtWidgets.QHBoxLayout()
        self.PlayerControls.setObjectName("PlayerControls")
        self.Prev = QtWidgets.QPushButton(self.centralwidget)
        self.Prev.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/ic_skip_previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Prev.setIcon(icon1)
        self.Prev.setIconSize(QtCore.QSize(25, 25))
        self.Prev.setDefault(False)
        self.Prev.setFlat(True)
        self.Prev.setObjectName("Prev")
        self.PlayerControls.addWidget(self.Prev)
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/ic_stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Stop.setIcon(icon2)
        self.Stop.setIconSize(QtCore.QSize(25, 25))
        self.Stop.setFlat(True)
        self.Stop.setObjectName("Stop")
        self.PlayerControls.addWidget(self.Stop)
        self.PlayPause = QtWidgets.QPushButton(self.centralwidget)
        self.PlayPause.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/ic_play_pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPause.setIcon(icon3)
        self.PlayPause.setIconSize(QtCore.QSize(25, 25))
        self.PlayPause.setFlat(True)
        self.PlayPause.setObjectName("PlayPause")
        self.PlayerControls.addWidget(self.PlayPause)
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/ic_skip_next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Next.setIcon(icon4)
        self.Next.setIconSize(QtCore.QSize(25, 25))
        self.Next.setDefault(False)
        self.Next.setFlat(True)
        self.Next.setObjectName("Next")
        self.PlayerControls.addWidget(self.Next)
        self.SongInfoAndControls.addLayout(self.PlayerControls, 0, 3, 2, 1)
        self.SongAlbum = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.SongAlbum.setFont(font)
        self.SongAlbum.setIndent(5)
        self.SongAlbum.setObjectName("SongAlbum")
        self.SongInfoAndControls.addWidget(self.SongAlbum, 2, 1, 1, 1)
        self.Volume = QtWidgets.QHBoxLayout()
        self.Volume.setObjectName("Volume")
        self.VolumeLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel.setFont(font)
        self.VolumeLabel.setIndent(5)
        self.VolumeLabel.setObjectName("VolumeLabel")
        self.Volume.addWidget(self.VolumeLabel)
        self.VolumeDecr = QtWidgets.QPushButton(self.centralwidget)
        self.VolumeDecr.setEnabled(True)
        self.VolumeDecr.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/ic_volume_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VolumeDecr.setIcon(icon5)
        self.VolumeDecr.setIconSize(QtCore.QSize(25, 25))
        self.VolumeDecr.setFlat(True)
        self.VolumeDecr.setObjectName("VolumeDecr")
        self.Volume.addWidget(self.VolumeDecr)
        self.VolumeIncr = QtWidgets.QPushButton(self.centralwidget)
        self.VolumeIncr.setEnabled(True)
        self.VolumeIncr.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/ic_volume_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VolumeIncr.setIcon(icon6)
        self.VolumeIncr.setIconSize(QtCore.QSize(25, 25))
        self.VolumeIncr.setFlat(True)
        self.VolumeIncr.setObjectName("VolumeIncr")
        self.Volume.addWidget(self.VolumeIncr)
        self.Mute = QtWidgets.QPushButton(self.centralwidget)
        self.Mute.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/ic_volume_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Mute.setIcon(icon7)
        self.Mute.setIconSize(QtCore.QSize(20, 20))
        self.Mute.setFlat(True)
        self.Mute.setObjectName("Mute")
        self.Volume.addWidget(self.Mute)
        self.SongInfoAndControls.addLayout(self.Volume, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.SongInfoAndControls.addItem(spacerItem, 2, 2, 1, 1)
        self.SongTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SongTitle.setFont(font)
        self.SongTitle.setIndent(5)
        self.SongTitle.setObjectName("SongTitle")
        self.SongInfoAndControls.addWidget(self.SongTitle, 0, 1, 1, 1)
        self.PosterView = QtWidgets.QLabel(self.centralwidget)
        self.PosterView.setMaximumSize(QtCore.QSize(85, 85))
        self.PosterView.setText("")
        self.PosterView.setPixmap(QtGui.QPixmap("icons/ina.png"))
        self.PosterView.setScaledContents(True)
        self.PosterView.setObjectName("PosterView")
        self.SongInfoAndControls.addWidget(self.PosterView, 0, 0, 3, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.SongInfoAndControls.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.SongInfoAndControls.addItem(spacerItem2, 1, 2, 1, 1)
        self.Player.addLayout(self.SongInfoAndControls, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.Player, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 705, 21))
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen_Folder = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/ic_folder_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Folder.setIcon(icon8)
        font = QtGui.QFont()
        font.setKerning(False)
        self.actionOpen_Folder.setFont(font)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.actionAbout_Project = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/ic_info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_Project.setIcon(icon9)
        self.actionAbout_Project.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionAbout_Project.setObjectName("actionAbout_Project")
        self.actionFetch_Recommendation = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/ic_music_note.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFetch_Recommendation.setIcon(icon10)
        self.actionFetch_Recommendation.setObjectName("actionFetch_Recommendation")
        self.actionEdit_MetaData = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/ic_border_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_MetaData.setIcon(icon11)
        self.actionEdit_MetaData.setObjectName("actionEdit_MetaData")
        self.actionSee_Source_on_Github = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/GitHub-Mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSee_Source_on_Github.setIcon(icon12)
        self.actionSee_Source_on_Github.setObjectName("actionSee_Source_on_Github")
        self.actionReport_Bug = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/ic_bug_report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReport_Bug.setIcon(icon13)
        self.actionReport_Bug.setObjectName("actionReport_Bug")
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuEdit.addAction(self.actionFetch_Recommendation)
        self.menuEdit.addAction(self.actionEdit_MetaData)
        self.menuAbout.addAction(self.actionAbout_Project)
        self.menuAbout.addAction(self.actionSee_Source_on_Github)
        self.menuAbout.addAction(self.actionReport_Bug)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionOpen_Folder)
        self.toolBar.addAction(self.actionEdit_MetaData)
        self.toolBar.addAction(self.actionFetch_Recommendation)
        self.toolBar.addAction(self.actionAbout_Project)
        self.toolBar.addAction(self.actionSee_Source_on_Github)
        self.toolBar.addAction(self.actionReport_Bug)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.CurrentTime.setText(_translate("MainWindow", "Time"))
        self.TotalTime.setText(_translate("MainWindow", "Time"))
        self.SongArtist.setText(_translate("MainWindow", "Singer"))
        self.Prev.setToolTip(_translate("MainWindow", "<html><head/><body><p>Previous</p></body></html>"))
        self.Stop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Stop</p></body></html>"))
        self.PlayPause.setToolTip(_translate("MainWindow", "<html><head/><body><p>Play/Pause</p></body></html>"))
        self.Next.setToolTip(_translate("MainWindow", "<html><head/><body><p>Next</p></body></html>"))
        self.SongAlbum.setText(_translate("MainWindow", "Album"))
        self.VolumeLabel.setText(_translate("MainWindow", "Vol"))
        self.VolumeDecr.setToolTip(_translate("MainWindow", "<html><head/><body><p>Decrease Volume</p></body></html>"))
        self.VolumeIncr.setToolTip(_translate("MainWindow", "<html><head/><body><p>Increase Volume</p></body></html>"))
        self.Mute.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mute</p></body></html>"))
        self.SongTitle.setText(_translate("MainWindow", "SongName"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen_Folder.setText(_translate("MainWindow", "Add Music Folder"))
        self.actionAbout_Project.setText(_translate("MainWindow", "About Project"))
        self.actionFetch_Recommendation.setText(_translate("MainWindow", "Fetch Recommendation"))
        self.actionEdit_MetaData.setText(_translate("MainWindow", "Edit MetaData"))
        self.actionSee_Source_on_Github.setText(_translate("MainWindow", "See Source Code"))
        self.actionReport_Bug.setText(_translate("MainWindow", "Report Bug"))

