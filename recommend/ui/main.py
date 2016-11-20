from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
import sys
import os
import const
from mainWindow import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # self.app = QtWidgets.QApplication(sys.argv)
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainWindow)
        self.extraSetup()
        # print(mainWindow.centralWidget)
        self.mainWindow.show()
        # self.app.exec_()

    def extraSetup(self):
        # main window
        self.window = self.ui
        # Lists
        self.playlistView = self.window.Playlist
        self.recommendLocalList = self.window.RecommendLocal
        self.recommendOnlineList = self.window.RecommendOnline
        # Song Info section
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
        # self.mediaPlayer.stateChanged.connect(self.mediaPlayerMediaStatusChangeHandler)
        # read from settings and set volume
        # The playback volume is linear in effect and the value
        # can range from 0 - 100, values outside this range will be clamped.
        self.volume = 50
        self.mediaPlayer.setVolume(self.volume)
        self.mediaPlayer.positionChanged.connect(self.mediaPlayerPositionChangedHandler)
        self.mediaPlayer.durationChanged.connect(self.durationChangedHandler)
        # print(dir(self.mediaPlayer))
        self.progressBar.sliderMoved.connect(self.seekPosition)
        self.progressBar.setTracking(True)
        self.sliderEventSender = QtWidgets.QSlider.sender(self.progressBar)

    """
    Event handlers
    """
    def browseHandler(self):
        self.songsFolder = QtWidgets.QFileDialog.getExistingDirectory(None, "Open a folder", os.getenv('HOME'),
                                                                 QtWidgets.QFileDialog.ShowDirsOnly)
        print(self.songsFolder)
        # save folder to settings
        self.crawlFolder()
        return True

    def openAboutUrl(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://projectrecommend.github.io/"))
        return True

    def openGitHubUrl(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/ProjectRecommend/Recommend"))
        return True

    def openIssuesUrl(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/ProjectRecommend/Recommend/issues"))
        return True

    def crawlFolder(self):
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
        self.saveSettings()
        self.buildPlayList()
        return self.filePathList

    def saveSettings(self):
        print("settings")

        # save settings to Ini Format in User scope
        self.settings = QtCore.QSettings(QtCore.QSettings.IniFormat, QtCore.QSettings.UserScope, const.orgName, const.projName)
        self.settings.setFallbacksEnabled(False)

        # check and update music folder location and volume
        self.volume = "30"
        self.settings.setValue("musicFolderLocation", self.songsFolder)
        self.settings.setValue("volume", self.volume)
        print("done")

    def buildPlayList(self):
        self.mediaPlaylist.clear()
        # self.mediaPlayer = QMediaPlayer()
        for filepath in self.filePathList:
            # print(filepath)
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
        print(self.volume)

    def VolumeDecrHandler(self):
        self.volume = max(int(self.volume) - 5, 0)
        self.mediaPlayer.setVolume(int(self.volume))
        print(self.volume)

    def muteHandler(self):
        # don't set  volume to 0 because we want to continue from
        # same volume on volumeDecr or volumeIncr button click
        self.mediaPlayer.setVolume(0)

    def mediaPlayerPositionChangedHandler(self, position, senderType=False):
        # print("mediaplayer position changed")
        if senderType is False:
            self.progressBar.setValue(position)
            self.currentTime.setText('%d:%02d' % (int(position / 60000), int((position / 1000) % 60)))

    def durationChangedHandler(self):
        # print("media Duration changed triggered")
        # update seek bar duration and range
        self.durationTotal_ms = self.mediaPlayer.duration()
        # print(self.durationTotal_ms)
        self.progressBar.setRange(0, self.durationTotal_ms)
        self.totalTime.setText('%d:%02d' % (int(self.durationTotal_ms / 60000), int((self.durationTotal_ms / 1000) % 60)))
        # update song info in ui
        metadataList = self.mediaPlayer.availableMetaData()
        for key in metadataList:
            print(self.mediaPlayer.metaData(key))

        self.songArtist.setText("test Artist")
        self.songAlbum.setText("test album")
        self.songTitle.setText("test song")


    def seekPosition(self, position):
        # print("seek position called")
        # # print(self.mediaPlayer.isSeekable())
        # print(self.sliderEventSender)
        # print(dir(self.sliderEventSender))
        # if isinstance(QtWidgets.QSlider.sender, QtWidgets.QSlider):
        #     print(self.mediaPlayer.isSeekable())
        if self.mediaPlayer.isSeekable():
            # print(position)
            self.mediaPlayer.setPosition(position)
            # print("seek")

    def qmp_volumeChanged(self):
        msg = self.statusBar().currentMessage()
        msg = msg[:-2] + str(self.player.volume())
        self.statusBar().showMessage(msg)

    def increaseVolume(self):
        vol = self.player.volume()
        vol = min(vol + 5, 100)
        self.player.setVolume(vol)

    def decreaseVolume(self):
        vol = self.player.volume()
        vol = max(vol - 5, 0)
        self.player.setVolume(vol)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

