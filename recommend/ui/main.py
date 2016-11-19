from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import const
from mainWindow import Ui_MainWindow


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
    prev = window.Prev
    next = window.Next
    stop = window.Stop
    playPause = window.PlayPause
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

    # Create Qt items
    # mediaPlaylist = QMediaPlaylist()
    # mediaPlayer = QMediaPlayer()
"""
Event handler for browse open folder action.
"""

def Browse(self):
    folder = QtWidgets.QFileDialog.getExistingDirectory(None, "Open a folder", os.getenv('HOME'), QtWidgets.QFileDialog.ShowDirsOnly)
    print(folder)
    crawlFolder(folder)
    return folder


def crawlFolder(folderPath):
    fileList = []
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
                    fileList.append(fInfo.absoluteFilePath())
    print(len(fileList))
    saveSettings()
    return fileList


def saveSettings():
    print("settings")

    # save settings to Ini Format in User scope
    settings = QtCore.QSettings(QtCore.QSettings.IniFormat, QtCore.QSettings.UserScope , const.orgName, const.projName)
    settings.setFallbacksEnabled(False)

    # check and update music folder location and volume
    musicFolderLocation = "C:\\Users\\Electron\\Music\\test_music_mp3"
    volume = "30"
    settings.setValue("musicFolderLocation", musicFolderLocation)
    settings.setValue("volume", volume)
    print("done")

# def buildPlayList():
#     pass


if __name__ == '__main__':
    main()
