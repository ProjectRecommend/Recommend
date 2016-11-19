from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
import sys
import os
import const
from mainWindow import Ui_MainWindow

filePathList = []
songsFolder = ""
# these will be QMediaPlaylist and QMediaPlayer objects, here they are assigned
# just to silence errors
mediaPlaylist = []
mediaPlayer = []
# user action for play/pause, stop, next, prev
# -1 is undetermined
# 0-stopped, 1-playing, 2-paused
userAction = -1


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    extraSetup(ui)
    # print(mainWindow.centralWidget)
    mainWindow.show()
    app.exec_()


def extraSetup(Ui_MainWindow):
    # main window
    window = Ui_MainWindow
    # Lists
    playlistView = window.Playlist
    recommendLocalList = window.RecommendLocal
    recommendOnlineList = window.RecommendOnline
    # Song Info section
    songTitle = window.SongTitle
    songArtist = window.SongArtist
    songAlbum = window.SongAlbum
    # player Controls
    prevBtn = window.Prev
    nextBtn = window.Next
    stopBtn = window.Stop
    playPauseBtn = window.PlayPause
    # Volume Controls
    volumeDecr = window.VolumeDecr
    volumeIncr = window.VolumeIncr
    mute = window.Mute
    # player timeline controls
    progressBar = window.ProgressBar
    currentTime = window.CurrentTime
    totalTime = window.TotalTime
    # Menu bar items
    openFolder = window.actionOpen_Folder
    editMetadata = window.actionEdit_MetaData
    fetchRecommendation = window.actionFetch_Recommendation
    aboutProject = window.actionAbout_Project
    seeSourceCode = window.actionSee_Source_on_Github
    reportBug = window.actionReport_Bug
    # set shortcuts on menu items
    openFolder.setShortcut('Ctrl+O')
    editMetadata.setShortcut('Ctrl+E')
    fetchRecommendation.setShortcut('Ctrl+R')
    # add actions on menu items

    """
    all events are triggered from here
    """
    openFolder.triggered.connect(Browse)
    # media control handlers
    playPauseBtn.clicked.connect(playPauseHandler)
    stopBtn.clicked.connect(stopHandler)
    prevBtn.clicked.connect(prevHandler)
    nextBtn.clicked.connect(nextHandler)

    # open webpages
    aboutProject.triggered.connect(openAboutUrl)
    seeSourceCode.triggered.connect(openGitHubUrl)
    reportBug.triggered.connect(openIssuesUrl)


"""
Event handler for browse open folder action.
"""


def Browse(self):
    global songsFolder
    songsFolder = QtWidgets.QFileDialog.getExistingDirectory(None, "Open a folder", os.getenv('HOME'), QtWidgets.QFileDialog.ShowDirsOnly)
    print(songsFolder)
    crawlFolder(songsFolder)
    return True


def openAboutUrl():
    QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://projectrecommend.github.io/"))
    return True


def openGitHubUrl():
    QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/ProjectRecommend/Recommend"))
    return True


def openIssuesUrl():
    QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/ProjectRecommend/Recommend/issues"))
    return True


def crawlFolder(folderPath):
    global filePathList
    filePathList = []
    if folderPath is not None:
        iterator = QtCore.QDirIterator(folderPath, QtCore.QDirIterator.Subdirectories)
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
                    filePathList.append(fInfo.absoluteFilePath())
    print(len(filePathList))
    saveSettings()
    buildPlayList()
    buildPlayer()
    # play()
    return filePathList


def saveSettings():
    print("settings")

    # save settings to Ini Format in User scope
    settings = QtCore.QSettings(QtCore.QSettings.IniFormat, QtCore.QSettings.UserScope , const.orgName, const.projName)
    settings.setFallbacksEnabled(False)

    # check and update music folder location and volume
    global songsFolder
    volume = "30"
    settings.setValue("musicFolderLocation", songsFolder)
    settings.setValue("volume", volume)
    print("done")


def buildPlayList():
    # Create Qt items
    global filePathList
    global mediaPlaylist
    mediaPlaylist = QtMultimedia.QMediaPlaylist()
    mediaPlaylist.clear()
    # self.mediaPlayer = QMediaPlayer()
    for filepath in filePathList:
        # print(filepath)
        mediaPlaylist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(filepath)))
    # print(mediaPlaylist.mediaCount())


def buildPlayer():
    global mediaPlaylist
    global mediaPlayer
    mediaPlayer = QtMultimedia.QMediaPlayer()
    mediaPlayer.setPlaylist(mediaPlaylist)


# def play():
#     global mediaPlayer
#     mediaPlayer.play()


def playPauseHandler():
    global userAction
    global mediaPlayer
    global mediaPlaylist

    if not mediaPlaylist:
        print("playlist is empty add few items")

    # if play list is not empty then proceed
    if mediaPlaylist:
        userAction = 1
        if mediaPlayer.state() == QtMultimedia.QMediaPlayer.StoppedState:
            if mediaPlayer.mediaStatus() == QtMultimedia.QMediaPlayer.NoMedia:
                print("no media in playlist")
                print(mediaPlaylist.mediaCount())
            elif mediaPlayer.mediaStatus() == QtMultimedia.QMediaPlayer.LoadedMedia:
                mediaPlayer.play()
            elif mediaPlayer.mediaStatus() == QtMultimedia.QMediaPlayer.BufferedMedia:
                mediaPlayer.play()
        elif mediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState:
            mediaPlayer.pause()
            userAction = 2
        elif mediaPlayer.state() == QtMultimedia.QMediaPlayer.PausedState:
            mediaPlayer.play()


def stopHandler():
    global mediaPlayer
    global userAction
    if mediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState:
        mediaPlayer.stop()
        userAction = 0
    elif mediaPlayer.state() == QtMultimedia.QMediaPlayer.PausedState:
        mediaPlayer.stop()
        userAction = 0
    elif mediaPlayer.state() == QtMultimedia.QMediaPlayer.StoppedState:
        pass


def prevHandler():
    global mediaPlayer
    mediaPlayer.playlist().previous()


def nextHandler():
    global mediaPlayer
    mediaPlayer.playlist().next()


def increaseVolume(self):
    vol = self.player.volume()
    vol = min(vol+5,100)
    self.player.setVolume(vol)


def decreaseVolume(self):
    vol = self.player.volume()
    vol = max(vol-5,0)
    self.player.setVolume(vol)


def qmp_mediaStatusChanged(self):
    if self.player.mediaStatus() == QMediaPlayer.LoadedMedia and self.userAction == 1:
        durationT = self.player.duration()
        self.centralWidget().layout().itemAt(0).layout().itemAt(1).widget().setRange(0,durationT)
        self.centralWidget().layout().itemAt(0).layout().itemAt(2).widget().setText('%d:%02d'%(int(durationT/60000),int((durationT/1000)%60)))
        self.player.play()


def qmp_stateChanged(self):
    if self.player.state() == QMediaPlayer.StoppedState:
        self.player.stop()


def qmp_positionChanged(self, position,senderType=False):
    sliderLayout = self.centralWidget().layout().itemAt(0).layout()
    if senderType == False:
        sliderLayout.itemAt(1).widget().setValue(position)
    # update the text label
    sliderLayout.itemAt(0).widget().setText('%d:%02d'%(int(position/60000), int((position/1000)%60)))


def seekPosition(self, position):
    sender = self.sender()
    if isinstance(sender,QSlider):
        if self.player.isSeekable():
            self.player.setPosition(position)


def qmp_volumeChanged(self):
    msg = self.statusBar().currentMessage()
    msg = msg[:-2] + str(self.player.volume())
    self.statusBar().showMessage(msg)


def increaseVolume(self):
    vol = self.player.volume()
    vol = min(vol+5,100)
    self.player.setVolume(vol)


def decreaseVolume(self):
    vol = self.player.volume()
    vol = max(vol-5,0)
    self.player.setVolume(vol)


if __name__ == '__main__':
    main()
