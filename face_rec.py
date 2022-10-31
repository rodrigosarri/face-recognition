import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np

def get_encoded_faces():
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


def classify_face(im):
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(im, 1)
    #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    #img = img[:,:,::-1]

    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # Se não encontrar o rosto retorna como ?????
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "?????"

        # Se encontrar, é atribuido o nome no rosto
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Desenhando o retângulo
            cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

            # Desenhando o rótulo
            cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)


    """
    while True:
        cv2.imshow('Resultado', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return face_names
    """

    cv2.imwrite("resultado.jpg", img)

classify_face("test.jpg")
