from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
import sys
import os
import const
from mainWindow import Ui_MainWindow
from editMetadata_form import Ui_EditMetaDataDialog
from bs4 import UnicodeDammit
from LocalStorage.AccessLocalStorageModule import AccessLocalStorage
from LocalStorage.ManageLocalStorageModule import ManageLocalStorage


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # self.app = QtWidgets.QApplication(sys.argv)
        self.mainWindow = QtWidgets.QMainWindow()
        # print(dir(self.mainWindow))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainWindow)
        # bind my self.closeEvent to mainWindow.closeEvent
        self.mainWindow.closeEvent = self.closeEvent
        self.extraSetup()
        # EditMetaDataDialog setup
        self.metadataDialog = MetadataDialog()
        # print(mainWindow.centralWidget)
        # self.mainWindow.show()
        # self.app.exec_()

    def extraSetup(self):
        # main window
        self.window = self.ui
        # Lists
        self.playlistView = self.window.Playlist
        self.recommendLocalList = self.window.RecommendLocal
        self.recommendOnlineList = self.window.RecommendOnline
        # Song Info section
        self.posterView = self.window.PosterView
        self.songTitle = self.window.SongTitle
        self.songArtist = self.window.SongArtist
        self.songAlbum = self.window.SongAlbum
        # player Controls
        self.prevBtn = self.window.Prev
        self.nextBtn = self.window.Next
        self.stopBtn = self.window.Stop
        self.playPauseBtn = self.window.PlayPause
        # Volume Controls
        self.volumeDecr = self.window.VolumeDecr
        self.volumeIncr = self.window.VolumeIncr
        self.mute = self.window.Mute
        self.volumeText = self.window.VolumeLabel
        # player timeline controls
        self.progressBar = self.window.ProgressBar
        self.currentTime = self.window.CurrentTime
        self.totalTime = self.window.TotalTime
        # Menu bar items
        self.openFolder = self.window.actionOpen_Folder
        self.editMetadata = self.window.actionEdit_MetaData
        self.fetchRecommendation = self.window.actionFetch_Recommendation
        self.aboutProject = self.window.actionAbout_Project
        self.seeSourceCode = self.window.actionSee_Source_on_Github
        self.reportBug = self.window.actionReport_Bug
        # set shortcuts on menu items
        self.openFolder.setShortcut('Ctrl+O')
        self.editMetadata.setShortcut('Ctrl+E')
        self.fetchRecommendation.setShortcut('Ctrl+R')
        # add actions on menu items

        """
        all events are triggered from here
        """
        self.openFolder.triggered.connect(self.browseHandler)
        self.editMetadata.triggered.connect(self.editMetadataHandler)
        # media control handlers
        self.playPauseBtn.clicked.connect(self.playPauseHandler)
        self.stopBtn.clicked.connect(self.stopHandler)
        self.prevBtn.clicked.connect(self.prevHandler)
        self.nextBtn.clicked.connect(self.nextHandler)
        # volume control handlers
        self.volumeIncr.clicked.connect(self.volumeIncrHandler)
        self.volumeDecr.clicked.connect(self.VolumeDecrHandler)
        self.mute.clicked.connect(self.muteHandler)

        # open webpages
        self.aboutProject.triggered.connect(self.openAboutUrl)
        self.seeSourceCode.triggered.connect(self.openGitHubUrl)
        self.reportBug.triggered.connect(self.openIssuesUrl)

        # create music player items
        self.mediaPlayer = QtMultimedia.QMediaPlayer()
        self.mediaPlaylist = QtMultimedia.QMediaPlaylist()
        self.mediaPlayer.setPlaylist(self.mediaPlaylist)
        # settings , in Ini format
        self.settings = QtCore.QSettings(QtCore.QSettings.IniFormat, QtCore.QSettings.UserScope, const.orgName, const.projName)
        self.settings.setFallbacksEnabled(False)
        # print(dir(self.settings))
        # read from settings and set volume
        # set songsFolder None so if we don't find it in settings we don't crawlFolder
        self.songsFolder = None
        self.loadSettings()
        # The playback volume is linear in effect and the value
        # can range from 0 - 100, values outside this range will be clamped.
        self.mediaPlayer.setVolume(int(self.volume))
        self.mediaPlayer.positionChanged.connect(self.mediaPlayerPositionChangedHandler)
        self.mediaPlayer.durationChanged.connect(self.durationChangedHandler)
        self.mediaPlayer.volumeChanged.connect(self.volumeChangedHandler)
        self.mediaPlayer.currentMediaChanged.connect(self.currentMediaChangedHandler)
        # print(dir(self.mediaPlayer))
        self.progressBar.sliderMoved.connect(self.seekPosition)
        self.progressBar.setTracking(True)
        self.sliderEventSender = QtWidgets.QSlider.sender(self.progressBar)
        # load music from songsFolder
        self.crawlFolder()
        # populate UI


    """
    Event handlers
    """
    def closeEvent(self, event):
        # print("close event")
        self.saveSettings()

    def browseHandler(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(None, "Open a folder", os.getenv('HOME'), QtWidgets.QFileDialog.ShowDirsOnly)
        if folder:
            self.songsFolder = folder
            self.crawlFolder()
        # print(self.songsFolder)

    def openAboutUrl(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://projectrecommend.github.io/"))

    def openGitHubUrl(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/ProjectRecommend/Recommend"))

    def openIssuesUrl(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/ProjectRecommend/Recommend/issues"))

    def crawlFolder(self):
        # print(self.songsFolder)
        if self.songsFolder is not None:
            self.filePathList = []
            if self.songsFolder is not None:
                iterator = QtCore.QDirIterator(self.songsFolder, QtCore.QDirIterator.Subdirectories)
                # print(dir(iterator))
                # print(dir(iterator.IteratorFlags))
                # print(iterator)
                while iterator.hasNext():
                    iterator.next()
                    fInfo = iterator.fileInfo()
                    if fInfo.isDir() is False and iterator.filePath() is not '.' and iterator.filePath() is not '..':
                        # print(iterator.fileInfo())
                        if fInfo.suffix() in ('mp3'):
                            # print(fInfo.absoluteFilePath())
                            self.filePathList.append(fInfo.absoluteFilePath())
            # print(len(self.filePathList))
            # add stuff into LocalStorage
            self.manageLocalStorage = ManageLocalStorage(const.LS_connectionName)
            lsStatus = self.manageLocalStorage.build()
            print(lsStatus)
            if lsStatus:
                print("built LS/Already there")
            else:
                print("Failed to Build LS, Exit")
                self.buildMessageBox("Building LocalStorage Storage Failed")
            self.localStorage = AccessLocalStorage(const.LS_connectionName)
            for path in self.filePathList:
                self.localStorage.write(path)

            # build playlist with all the songs
            model = self.manageLocalStorage.query()
            # set header title
            model.setHeaderData(2, QtCore.Qt.Horizontal, 'Track Title')
            model.setHeaderData(3, QtCore.Qt.Horizontal, 'Artist')
            self.playlistView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
            # self.playlistView.setColumnWidth(1000, 2000)
            # Query db and hide all the not required fields
            self.playlistView.setModel(model)
            # hide column 0 (SID) and 1 (SPath), which we will use to other purposes
            self.playlistView.setColumnHidden(0, True)
            self.playlistView.setColumnHidden(1, True)
            self.playlistView.setColumnWidth(2, 200)
            self.playlistView.setColumnWidth(3, 100)
            self.playlistView.setTabKeyNavigation(False)
            self.playlistView.setCornerButtonEnabled(False)
            self.playlistView.selectRow(0)
            self.playlistView.doubleClicked.connect(self.playlistViewDoubleClickHandler)
            self.buildMediaPlaylistPathList()

            self.buildPlayList()
        else:
            # throw an error saying to add music folder
            print("load a folder for music, from settings it is None")
            self.buildMessageBox("No Music Folder Found, Select a Music Folder")

    def buildMediaPlaylistPathList(self):
        self.mediaPlaylistPathList = []
        model = self.playlistView.model()
        for row in range(model.rowCount()):
            index = model.index(row, 1)
                # We suppose data are strings
            self.mediaPlaylistPathList.append(str(model.data(index)))
        print(len(self.mediaPlaylistPathList))
        # print(mediaPlaylistPathList)

    def playlistViewDoubleClickHandler(self, index):
        print("playList View item double clicked")
        row = index.row()
        print(row)
        self.mediaPlaylist.setCurrentIndex(row)

    def saveSettings(self):
        # print("save settings in")
        # save settings to Ini Format in User scope
        # check and update music folder location and volume
        self.settings.setValue(const.musicFolderLocationKey, self.songsFolder)
        self.settings.setValue(const.volumeKey, self.volume)
        # print(self.songsFolder)
        # print(self.volume)
        # print("save settings out")

    def loadSettings(self):
        # print("load settings in")
        if self.settings.value(const.volumeKey)is not None:
            self.volume = self.settings.value(const.volumeKey)
        else:
            self.volume = 60
        if self.settings.value(const.musicFolderLocationKey):
            self.songsFolder = self.settings.value(const.musicFolderLocationKey)
        else:
            print("can't load music folder from settings")
            # self.buildMessageBox("Failed to Load location from Settings, select a Music Folder")
            # print(self.settings.value(const.musicFolderLocationKey))
        # print(self.settings)
        # print(self.volume)
        # print(self.songsFolder)
        # print("load settings out")

    def buildPlayList(self):
        self.mediaPlaylist.clear()
        # self.mediaPlayer = QMediaPlayer()
        for filepath in self.mediaPlaylistPathList:
            print(filepath)
            self.mediaPlaylist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(filepath)))
            # print(self.mediaPlaylist.mediaCount())
        self.mediaPlayer.setPlaylist(self.mediaPlaylist)

    def playPauseHandler(self):
        # if play list is not empty then proceed
        if self.mediaPlaylist:
            self.userAction = 1
            if self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.StoppedState:
                if self.mediaPlayer.mediaStatus() == QtMultimedia.QMediaPlayer.NoMedia:
                    print("no media in playlist")
                    self.buildMessageBox("Playlist is empty, select a folder that have music(.mp3 files) in it")
                    # print(self.mediaPlaylist.mediaCount())
                elif self.mediaPlayer.mediaStatus() == QtMultimedia.QMediaPlayer.LoadedMedia:
                    self.mediaPlayer.play()
                elif self.mediaPlayer.mediaStatus() == QtMultimedia.QMediaPlayer.BufferedMedia:
                    self.mediaPlayer.play()
            elif self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState:
                self.mediaPlayer.pause()
                self.userAction = 2
            elif self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PausedState:
                self.mediaPlayer.play()

    def stopHandler(self):
        if self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState:
            self.mediaPlayer.stop()
            self.userAction = 0
        elif self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PausedState:
            self.mediaPlayer.stop()
            self.userAction = 0
        elif self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.StoppedState:
            pass

    def prevHandler(self):
        self.mediaPlayer.playlist().previous()

    def nextHandler(self):
        self.mediaPlayer.playlist().next()

    # The playback volume is linear in effect and the value
    # can range from 0 - 100, values outside this range will be clamped.
    def volumeIncrHandler(self):
        self.volume = min(int(self.volume) + 5, 100)
        self.mediaPlayer.setVolume(int(self.volume))
        # print(self.volume)

    def VolumeDecrHandler(self):
        self.volume = max(int(self.volume) - 5, 0)
        self.mediaPlayer.setVolume(int(self.volume))
        # print(self.volume)

    def muteHandler(self):
        # don't set  volume to 0 because we want to continue from
        # same volume on volumeDecr or volumeIncr button click
        self.mediaPlayer.setVolume(0)
        self.volumeText.setText("Mute")

    def mediaPlayerPositionChangedHandler(self, position, senderType=False):
        # print("mediaPlayer position changed")
        if senderType is False:
            self.progressBar.setValue(position)
            self.currentTime.setText('%d:%02d' % (int(position / 60000), int((position / 1000) % 60)))

    def durationChangedHandler(self):
        # print("media Duration changed triggered")
        # update seek bar duration and range
        self.durationTotal_ms = self.mediaPlayer.duration()
        # print(self.durationTotal_ms)
        if self.durationTotal_ms is 0:
            pass
            # this event gets triggered twice when song goes out of plyer and
            # song comes in player it have 0 durationTotal_ms
            # when song goes out gets triggered
        else:
            self.progressBar.setRange(0, self.durationTotal_ms)
            self.totalTime.setText('%d:%02d' % (int(self.durationTotal_ms / 60000), int((self.durationTotal_ms / 1000) % 60)))

            # update song info in ui
            if self.mediaPlayer.metaData('ThumbnailImage') is not None:
                pixmap = QtGui.QPixmap.fromImage(self.mediaPlayer.metaData('ThumbnailImage'))
                self.posterView.setPixmap(pixmap)
            else:
                img = QtGui.QImage("icons\ina.png")
                pixmap = QtGui.QPixmap.fromImage(img)
                self.posterView.setPixmap(pixmap)
                # self.posterView.setText("Image Not Available")

            self.songArtist.setText(self.mediaPlayer.metaData('AlbumArtist'))
            self.songAlbum.setText(self.mediaPlayer.metaData('AlbumTitle'))
            self.songTitle.setText(self.mediaPlayer.metaData('Title'))
            self.volumeText.setText(str(self.volume))

    def currentMediaChangedHandler(self):
        # print("current Media changed Handler triggered")
        # print(self.mediaPlayer.currentMedia())
        # print(dir(self.mediaPlayer.currentMedia()))
        if self.mediaPlayer.currentMedia():
            self.currentPlayingMediaUrl = self.mediaPlayer.currentMedia().canonicalUrl().toString()
            # print(currentPlayingMediaUrl)
            # convert file:///C:/Users/Electron/Music/filename.mp3
            # to C:/Users/Electron/Music/filename.mp3
            self.currentPlayingMediaUrl = self.currentPlayingMediaUrl[8:]
            # convert it to Unicode
            # print(currentPlayingMediaUrl)
            dammit = UnicodeDammit(self.currentPlayingMediaUrl)
            self.currentPlayingMediaUrl = dammit.unicode_markup
            # print(self.currentPlayingMediaUrl)
        # pass

    def seekPosition(self, position):
        # print("seek position called")
        # print(self.mediaPlayer.isSeekable())
        # print(self.sliderEventSender)
        # print(dir(self.sliderEventSender))
        # if isinstance(QtWidgets.QSlider.sender, QtWidgets.QSlider):
        #     print(self.mediaPlayer.isSeekable())
        if self.mediaPlayer.isSeekable():
            # print(position)
            self.mediaPlayer.setPosition(position)
            # print("seek")

    def volumeChangedHandler(self):
        self.volumeText.setText(str(self.volume))

    def increaseVolume(self):
        vol = self.player.volume()
        vol = min(vol + 5, 100)
        self.player.setVolume(vol)

    def decreaseVolume(self):
        vol = self.player.volume()
        vol = max(vol - 5, 0)
        self.player.setVolume(vol)

    def editMetadataHandler(self):
        print("open edit metadata dialog")
        self.metadataDialog.editMetadataDialog.exec_()

    def buildMessageBox(self, message):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setText(message)
        messageBox.setIcon(messageBox.Warning)
        messageBox.setWindowTitle("Message")
        messageBox.exec()


class MetadataDialog(Ui_EditMetaDataDialog):
    def __init__(self):
        super().__init__()
        # setup editMetadataDialog
        self.editMetadataDialog = QtWidgets.QDialog()
        self.ui = Ui_EditMetaDataDialog()
        self.ui.setupUi(self.editMetadataDialog)
        self.buttonSave = self.ui.saveButton
        self.buttonCancel = self.ui.cancelButton
        # self.editMetadataDialog.accept = self.accept
        # self.editMetadataDialog.reject = self.reject
        self.wireButtons()

    def wireButtons(self):
        # self.buttonBox.accepted.connect(self.editMetadataDialog.accept)
        # self.buttonBox.rejected.connect(self.editMetadataDialog.reject)
        self.buttonSave.clicked.connect(self.saveButtonHandler)
        self.buttonCancel.clicked.connect(self.cancelButtonHandler)

    def saveButtonHandler(self):
        print("save stuff")
        self.editMetadataDialog.accept()

    def cancelButtonHandler(self):
        print("cancel stuff")
        self.editMetadataDialog.reject()


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
