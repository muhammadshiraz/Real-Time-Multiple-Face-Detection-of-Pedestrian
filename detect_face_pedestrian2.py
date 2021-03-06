import cv2

# Load the cascade
face_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('images/pedestrian2.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_classifier.detectMultiScale(gray, 1.133, 6)

# Declare color variable
dark_blue = (0,0,255)

# Draw rectangle around the faces
if len(faces) > 1:
    i = 0
    for f in faces:
        face = faces[i]
        (x, y, w, h) = face
        cv2.rectangle(img, (x, y), (x + w, y + h), dark_blue, 2)
        cv2.putText(img, "Face {}".format(i), (x - 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, dark_blue, 2)
        i = i + 1

# Display the output
cv2.imshow('img', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
