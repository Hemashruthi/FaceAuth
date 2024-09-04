import cv2
import face_recognition

import pickle
import os
# Importing student image

folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentIds.append(os.path.splitext(path)[0])
    print(path)
    print(os.path.splitext(path)[0])
print(len(imgList))

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
print("Encoding Started")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown , studentIds]
print(encodeListKnown)
print("Encoding complete")

file = open(r"D:\Higher studies\Projects\fr_demo\Encodings\SaveFile.p",'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File Saved")
