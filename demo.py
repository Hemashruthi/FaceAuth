import cv2
import pickle
import face_recognition
import numpy as np

#  Load the encoding file
print("Loading Encode File___")
file = open(r"Encodings\SaveFile.p",'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print("Encode File Loaded___")
matchIndex = []
img = cv2.imread(r"D:\Higher studies\Projects\fr_demo\Images\tv.jpeg")
# img = cv2.imread(r"D:\downloads\12.png")
# imgS = cv2.resize(img,(0,0),None,0.25, 0.25)
imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

faceCurFrame = face_recognition.face_locations(imgS)
encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)
print(encodeCurFrame)

for encodeFace , faceLoc in zip(encodeCurFrame,faceCurFrame):
    matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
    faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
    # print("matches",matches)
    # print("faceDis",faceDis)
    matchIndex = np.argmin(faceDis)
    print("Match Index", matchIndex)

    if matches[matchIndex]:
        print("Known Face Detected")
        print("Match Index", matchIndex)
        print(studentIds[matchIndex])
    else:
        print("Unknown face detected")

cv2.waitKey(0)