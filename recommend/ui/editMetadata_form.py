# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editMetadata_form.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditMetaDataDialog(object):
    def setupUi(self, EditMetaDataDialog):
        EditMetaDataDialog.setObjectName("EditMetaDataDialog")
        EditMetaDataDialog.setWindowModality(QtCore.Qt.NonModal)
        EditMetaDataDialog.resize(384, 408)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EditMetaDataDialog.sizePolicy().hasHeightForWidth())
        EditMetaDataDialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        EditMetaDataDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/ic_main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditMetaDataDialog.setWindowIcon(icon)
        EditMetaDataDialog.setToolTip("")
        EditMetaDataDialog.setStatusTip("")
        EditMetaDataDialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(EditMetaDataDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.saveButton = QtWidgets.QPushButton(EditMetaDataDialog)
        self.saveButton.setSizeIncrement(QtCore.QSize(0, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/ic_save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon1)
        self.saveButton.setIconSize(QtCore.QSize(25, 25))
        self.saveButton.setAutoDefault(False)
        self.saveButton.setDefault(False)
        self.saveButton.setFlat(True)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 2, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.titleLabel = QtWidgets.QLabel(EditMetaDataDialog)
        self.titleLabel.setIndent(5)
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titleLabel)
        self.titleLineEdit = QtWidgets.QLineEdit(EditMetaDataDialog)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titleLineEdit)
        self.artistLabel = QtWidgets.QLabel(EditMetaDataDialog)
        self.artistLabel.setIndent(5)
        self.artistLabel.setObjectName("artistLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.artistLabel)
        self.artistLineEdit = QtWidgets.QLineEdit(EditMetaDataDialog)
        self.artistLineEdit.setObjectName("artistLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.artistLineEdit)
        self.albumLabel = QtWidgets.QLabel(EditMetaDataDialog)
        self.albumLabel.setIndent(5)
        self.albumLabel.setObjectName("albumLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.albumLabel)
        self.albumLineEdit = QtWidgets.QLineEdit(EditMetaDataDialog)
        self.albumLineEdit.setObjectName("albumLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.albumLineEdit)
        self.albumArtistLabel = QtWidgets.QLabel(EditMetaDataDialog)
        self.albumArtistLabel.setIndent(5)
        self.albumArtistLabel.setObjectName("albumArtistLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.albumArtistLabel)
        self.albumArtistLineEdit = QtWidgets.QLineEdit(EditMetaDataDialog)
        self.albumArtistLineEdit.setObjectName("albumArtistLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.albumArtistLineEdit)
        self.genreLabel = QtWidgets.QLabel(EditMetaDataDialog)
        self.genreLabel.setIndent(5)
        self.genreLabel.setObjectName("genreLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.genreLabel)
        self.genreLineEdit = QtWidgets.QLineEdit(EditMetaDataDialog)
        self.genreLineEdit.setObjectName("genreLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.genreLineEdit)
        self.yearLabel = QtWidgets.QLabel(EditMetaDataDialog)
        self.yearLabel.setIndent(5)
        self.yearLabel.setObjectName("yearLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.yearLabel)
        self.yearLineEdit = QtWidgets.QLineEdit(EditMetaDataDialog)
        self.yearLineEdit.setObjectName("yearLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.yearLineEdit)
        self.publisherLabel = QtWidgets.QLabel(EditMetaDataDialog)
        self.publisherLabel.setIndent(5)
        self.publisherLabel.setObjectName("publisherLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.publisherLabel)
        self.publisherLineEdit = QtWidgets.QLineEdit(EditMetaDataDialog)
        self.publisherLineEdit.setObjectName("publisherLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.publisherLineEdit)
        self.lyricsLabel = QtWidgets.QLabel(EditMetaDataDialog)
        self.lyricsLabel.setIndent(5)
        self.lyricsLabel.setObjectName("lyricsLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lyricsLabel)
        self.lyricsLineEdit = QtWidgets.QLineEdit(EditMetaDataDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.lyricsLineEdit.sizePolicy().hasHeightForWidth())
        self.lyricsLineEdit.setSizePolicy(sizePolicy)
        self.lyricsLineEdit.setObjectName("lyricsLineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lyricsLineEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 5, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(EditMetaDataDialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/ic_cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon2)
        self.cancelButton.setIconSize(QtCore.QSize(25, 25))
        self.cancelButton.setAutoDefault(False)
        self.cancelButton.setDefault(False)
        self.cancelButton.setFlat(True)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 1, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)

        self.retranslateUi(EditMetaDataDialog)
        QtCore.QMetaObject.connectSlotsByName(EditMetaDataDialog)
        EditMetaDataDialog.setTabOrder(self.titleLineEdit, self.artistLineEdit)
        EditMetaDataDialog.setTabOrder(self.artistLineEdit, self.albumLineEdit)
        EditMetaDataDialog.setTabOrder(self.albumLineEdit, self.albumArtistLineEdit)
        EditMetaDataDialog.setTabOrder(self.albumArtistLineEdit, self.genreLineEdit)
        EditMetaDataDialog.setTabOrder(self.genreLineEdit, self.yearLineEdit)
        EditMetaDataDialog.setTabOrder(self.yearLineEdit, self.publisherLineEdit)
        EditMetaDataDialog.setTabOrder(self.publisherLineEdit, self.lyricsLineEdit)
        EditMetaDataDialog.setTabOrder(self.lyricsLineEdit, self.saveButton)
        EditMetaDataDialog.setTabOrder(self.saveButton, self.cancelButton)

    def retranslateUi(self, EditMetaDataDialog):
        _translate = QtCore.QCoreApplication.translate
        EditMetaDataDialog.setWindowTitle(_translate("EditMetaDataDialog", "Edit Song MetaData"))
        EditMetaDataDialog.setWhatsThis(_translate("EditMetaDataDialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Edit MetaData(ID3 Tags) of song, we use MetaData to recommend new songs.</span></p><p><span style=\" font-size:10pt;\">Wrong MetaData may result in incorrect or no recommendation of this song</span></p></body></html>"))
        self.saveButton.setText(_translate("EditMetaDataDialog", "Save"))
        self.titleLabel.setText(_translate("EditMetaDataDialog", "Track Title"))
        self.artistLabel.setText(_translate("EditMetaDataDialog", "Artist"))
        self.albumLabel.setText(_translate("EditMetaDataDialog", "Album"))
        self.albumArtistLabel.setText(_translate("EditMetaDataDialog", "Album Artist"))
        self.genreLabel.setText(_translate("EditMetaDataDialog", "Genre"))
        self.yearLabel.setText(_translate("EditMetaDataDialog", "Year"))
        self.publisherLabel.setText(_translate("EditMetaDataDialog", "Publisher"))
        self.lyricsLabel.setText(_translate("EditMetaDataDialog", "Lyrics"))
        self.cancelButton.setText(_translate("EditMetaDataDialog", "Cancel"))

