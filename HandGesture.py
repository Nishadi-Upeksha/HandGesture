import cv2
import time
import os
import HandTrackingModule as htm
from pygame import mixer

# camera
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Music Player
mixer.init()

# Song Tracks
musicFolderPath = "Songs"
myMusicList = os.listdir(musicFolderPath)
print(myMusicList)
overlayMusicList = []
for musicPath in myMusicList:
    Music = cv2.imread(f'{musicFolderPath}/{musicPath}')
    overlayMusicList.append((Music))

print(len(overlayMusicList))

# Finger Photos
folderPath = "FingerPhotos"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append((image))

print(len(overlayList))

pTime = 0
prev_volume = mixer.music.get_volume()

detector = htm.handDetector(detectionCon=0.75)
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []

        # For Right Hand


        if ((lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]) and (
                lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2]) and (
                      lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2]) and (
                      lmList[tipIds[3]][2] < lmList[tipIds[3] - 2][2]) and (
                      lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2])):
            # Song No 4
            print(4)
            mixer.music.load(myMusicList[3])
            mixer.music.play()



        elif ((lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]) and (
                lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2]) and (
                      lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2]) and (
                      lmList[tipIds[3]][2] < lmList[tipIds[3] - 2][2]) and (
                      lmList[tipIds[4]][2] > lmList[tipIds[4] - 2][2])):
            # Song No 3
            print(3)
            mixer.music.load(myMusicList[2])
            mixer.music.play()


        elif ((lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]) and (
                lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2]) and (
                      lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2]) and (
                      lmList[tipIds[3]][2] > lmList[tipIds[3] - 2][2]) and (
                      lmList[tipIds[4]][2] > lmList[tipIds[4] - 2][2])):
            # Song No 2
            print(2)
            mixer.music.load(myMusicList[1])
            mixer.music.play()



        elif ((lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]) and (
                lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2]) and (
                      lmList[tipIds[2]][2] > lmList[tipIds[2] - 2][2]) and (
                      lmList[tipIds[3]][2] > lmList[tipIds[3] - 2][2]) and (
                      lmList[tipIds[4]][2] > lmList[tipIds[4] - 2][2])):
            # Song No 1
            print(1)
            mixer.music.load(myMusicList[0])
            mixer.music.play()


        elif ((lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]) and (
                lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2]) and (
                lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2]) and (
                lmList[tipIds[3]][2] < lmList[tipIds[3] - 2][2]) and (lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2])):
            # Stop
            print("Stop")
            cv2.putText(img, 'Stop', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
            mixer.music.stop()


        elif ((lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]) and (
                lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2]) and (
                      lmList[tipIds[2]][2] > lmList[tipIds[2] - 2][2]) and (
                      lmList[tipIds[3]][2] > lmList[tipIds[3] - 2][2]) and (
                      lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2])):
            # Pause
            print("Pause")
            cv2.putText(img, 'Pause', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
            mixer.music.pause()

        elif ((lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]) and (
                lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2]) and (
                      lmList[tipIds[2]][2] > lmList[tipIds[2] - 2][2]) and (
                      lmList[tipIds[3]][2] > lmList[tipIds[3] - 2][2]) and (
                      lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2])):
            # Resume
            print("Resume")
            cv2.putText(img, 'Resume', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
            mixer.music.unpause()


        elif ((lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]) and (
                lmList[tipIds[1]][2] > lmList[tipIds[1] - 2][2]) and (
                      lmList[tipIds[2]][2] > lmList[tipIds[2] - 2][2]) and (
                      lmList[tipIds[3]][2] > lmList[tipIds[3] - 2][2]) and (
                      lmList[tipIds[4]][2] > lmList[tipIds[4] - 2][2])):
            # Mute
            print("Mute")
            cv2.putText(img, 'Mute', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
            mixer.music.set_volume(0)

        elif ((lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]) and (
                lmList[tipIds[1]][2] > lmList[tipIds[1] - 2][2]) and (
                      lmList[tipIds[2]][2] > lmList[tipIds[2] - 2][2]) and (
                      lmList[tipIds[3]][2] > lmList[tipIds[3] - 2][2]) and (
                      lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2])):
            # Unmute
            print("Unmute")
            cv2.putText(img, 'Unmute', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
            mixer.music.set_volume(prev_volume)

        elif ((lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]) and (
                lmList[tipIds[1]][2] > lmList[tipIds[1] - 2][2]) and (
                      lmList[tipIds[2]][2] > lmList[tipIds[2] - 2][2]) and (
                      lmList[tipIds[3]][2] > lmList[tipIds[3] - 2][2]) and (
                      lmList[tipIds[4]][2] > lmList[tipIds[4] - 2][2])):
            # Previous
            print("Previous")




        elif ((lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]) and (
                lmList[tipIds[1]][2] > lmList[tipIds[1] - 2][2]) and (
                      lmList[tipIds[2]][2] > lmList[tipIds[2] - 2][2]) and (
                      lmList[tipIds[3]][2] > lmList[tipIds[3] - 2][2]) and (
                      lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2])):
            # Next
            print("Next")




    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTiime = cTime

    cv2.imshow("Image", img)
    cv2.waitKey(1)
