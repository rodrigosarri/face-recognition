import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np

def getEncodedFaces():
    """
    Na pasta faces são coloca as imagens com os respectivos nomes ao qual aquele rosto pertence
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded


def classifyFace(im):
    faces = getEncodedFaces()
    facesEncoded = list(faces.values())
    knownFaceNames = list(faces.keys())
    testFolder = "tests/"

    img = cv2.imread(testFolder + im, 1)
    #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    #img = img[:,:,::-1]

    face_locations = face_recognition.face_locations(img)
    unknownFaceEncodings = face_recognition.face_encodings(img, face_locations)

    faceNames = []
    for face_encoding in unknownFaceEncodings:
        # Se não encontrar o rosto retorna como ?????
        matches = face_recognition.compare_faces(facesEncoded, face_encoding)
        name = "?????"

        # Se encontrar, é atribuido o nome no rosto
        faceDistances = face_recognition.face_distance(facesEncoded, face_encoding)
        bestMatchIndex = np.argmin(faceDistances)
        if matches[bestMatchIndex]:
            name = knownFaceNames[bestMatchIndex]

        faceNames.append(name)

        for (top, right, bottom, left), name in zip(face_locations, faceNames):
            # Desenhando o retângulo
            cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

            # Desenhando o rótulo
            cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)

    cv2.imwrite("results/" + im.split(".")[0] + '.jpg', img)

def generateTests():
    for dirpath, dnames, fnames in os.walk("./tests"):
        for f in fnames:
            classifyFace(f)

generateTests()
