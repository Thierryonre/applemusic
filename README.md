# applemusic
 Apple music in python made easy - Play music with ease!
 Please feel free to create pull requests, whether to fix a bug or implement a new feature.

## Features
_Please keep in mind that this module is still in extreme-alpha._

### Current Features
* Login to the apple music platform
* Play songs
* Resume and pause songs
* Restart playing song
* Play the previous song in the album
* Play the next song in the album
* Shuffle songs

### Features to do
* Determine the country code via IP address
* Only shuffle if not shuffled and vice versa
* Allow user to change volume
* Play playlists
* Initiate all commands in one function
* Allow sleep statements to be more easily changed for people with different internet speeds
* Allow firefox and PhantomJS to be used
* Allow for the song to be rewinded or forwarded by a specific amount of time

### Other things to do
* Remove sleep statements to make it faster
* Add documentation for variables dictionary
* Add documentation to install module from source

## **Requirements**
* Python 3.*
* Selenium
* The correct webdriver for your system - Please find all required selenium webdrivers [here](https://github.com/Thierryonre/Selenium-Drivers)

## **Installation**
### **From PyPi**
```
pip install applemusic
```

## **Usuage**
To use the module, run the following commands:
```python
from applemusic import AppleMusic
AM = AppleMusic()
AM.setupMethod()
AM.setupVariables()
AM.initiateWindow()
AM.login("Johnny_applebottom@outlook.com", "password123")
# E.G. AM.playSong("Hello by Adele")
```

Replace the last line with some of the commands from below.
The commands to be replaced are below and the above code is only to initiate the player so it only has to be used once,
 unless multiple songs are to be played synchronously.

## **Commands**
| Command       | Parameters                      | What does it do?                                                                                                                                        |
|---------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| login         | Username/Email address Password | Logs into the apple music website. If 2FA is enabled, it will ask for the code sent to a validated iCloud device.                                       |
| playSong      | Song                            | Plays the song. The input is directly passed into the apple music website.                                                                              |
| resumeOrPause | NO PARAMETERS                   | Resumes or pauses the song regardless of its current state.                                                                                             |
| restartSong   | NO PARAMETERS                   | Restarts the currently playing song. Executing within a few seconds of previously being executed will result in the previous song in the album playing. |
| previousSong  | NO PARAMETERS                   | Plays the previous song in the album.                                                                                                                   |
| nextSong      | NO PARAMETERS                   | Plays the next song in the album. Nothing will occur if there is not a next song.                                                                       |
| shuffle       | NO PARAMETERS                   | Shuffles the order of the songs regardless of whether it was already shuffled or not.                                                                   |

## **Notes**
* Until the sleep statements are removed, the time for the script to execute will be longer than it should be.
* However, selenium can just be slow. Speeds may vary due to your internet speed.
* PhantomJS should make the script faster when I have implemented it.
