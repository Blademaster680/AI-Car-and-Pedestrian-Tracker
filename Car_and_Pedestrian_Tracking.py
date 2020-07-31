import cv2

# Our Image
img_file = 'car images/Screenshot_4.png'
video = cv2.VideoCapture('The Ultimate Pedestrian Compilation.mp4')

# Create car classifier
car_tracker = cv2.CascadeClassifier('car_detector.xml')
pedestrian_tracker = cv2.CascadeClassifier('pedestrian_detector.xml')

# Run forever until car stops
while True:

    # Read the current frame
    (read_successful, frame) = video.read()

    # Safe code
    if read_successful:
        # Must convert to grayscale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # Detect cars and pedestrians
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    peds = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    # Draw rectangles around the cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Draw rectangles around the pedestrians
    for (x, y, w, h) in peds:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    # Display the image with the cars spotted
    cv2.imshow('Blademasters Pedestrian and Car Tracker', frame)

    # Dont autoclose (Wait here in the code and listen for a key press)
    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key==81 or key==113:
        break

# Relase the VideoCapture object
video.release()

"""

# Create opencv image
img = cv2.imread(img_file)

# Create car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

# Convert the image to black and white (Needed for the haar cascade)
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect cars
cars = car_tracker.detectMultiScale(black_n_white)

# Draw rectangles around the cars
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

print(cars)

# Display the image with the faces spotted
cv2.imshow("Blademaster's Car Detector", img)

"""

print("Code Completed")
