import cv2

# Load the cascade
face_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

# Declare color variable
dark_red = (0,0,255)

# Read the input image
img = cv2.imread('images/pedestrian5.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_classifier.detectMultiScale(gray, 1.133, 6)

# Draw rectangle around the faces
if len(faces) > 1:
    i = 0
    for f in faces:
        face = faces[i]
        (x, y, w, h) = face
        cv2.rectangle(img, (x, y), (x + w, y + h), dark_red, 2)
        cv2.putText(img, "Face #{}".format(i), (x - 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, dark_red, 2)
        i = i + 1

# Display the output
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
