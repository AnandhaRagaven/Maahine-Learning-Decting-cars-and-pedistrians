import cv2

# our image
#img_file = 'caar.jpg'


# viedo files
#video = cv2.VideoCapture('cardector.mp4')
video = cv2.VideoCapture('pedstrian.mp4')

# pretrained car and pedestrian images
car_tracker = 'car_detector.xml'
predestrian_tracker = 'haarcascade_fullbody.xml'


# create car classifier
car_tracker = cv2.CascadeClassifier(car_tracker)

# create  pedstrian classifier
predestrian_tracker = cv2.CascadeClassifier(predestrian_tracker)


# Run forever until car stops or something
while True:

    # read the currnt frame
    (read_successful, frame) = video.read()

    # Safe coding
    if read_successful:
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # detect cars and pedestrian

    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrian = predestrian_tracker.detectMultiScale(grayscaled_frame)

    # draw rectanges around car

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x+1, y+2), (x+w, y+h), (255, 0, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

     # draw rectanges around pedestrians

    for (x, y, w, h) in pedestrian:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    cv2.imshow('Automatic car', frame)

    cv2.waitKey(1)
""""

# create open cv image
img = cv2.imread(img_file)


# convet to greyscale
black_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# create car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)


# detect cars

cars = car_tracker.detectMultiScale(black_white)


# draw rectanges around car


for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)


# display the images with the faces spotted
cv2.imshow('Automatic car', img)

# Don't autoclose
cv2.waitKey()

"""
