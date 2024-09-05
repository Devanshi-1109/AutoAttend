import face_recognition
import cv2
import numpy as np
import os
import xlwt
from xlwt import Workbook
from datetime import date
import xlrd
from xlutils.copy import copy as xl_copy
import time

# Initialize variables
CurrentFolder = os.getcwd()  # Read current folder path
image = CurrentFolder + '/devanshi2.png'
image2 = CurrentFolder + '/Rishu.png'

video_capture = cv2.VideoCapture(0)

# Load sample pictures and learn how to recognize them.
person1_name = "Devanshi"
person1_image = face_recognition.load_image_file(image)
person1_face_encoding = face_recognition.face_encodings(person1_image)[0]

person2_name = "Rishu"
person2_image = face_recognition.load_image_file(image2)
person2_face_encoding = face_recognition.face_encodings(person2_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    person1_face_encoding,
    person2_face_encoding
]
known_face_names = [
    person1_name,
    person2_name
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# Load the workbook and check if the sheet exists
try:
    rb = xlrd.open_workbook('attendence_excel.xls', formatting_info=True)
    sheet_exists = False
    sheet_index = None

    for index, sheet_name in enumerate(rb.sheet_names()):
        if sheet_name == str(date.today()):
            sheet_exists = True
            sheet_index = index
            break

    wb = xl_copy(rb)

    if sheet_exists:
        sheet1 = wb.get_sheet(sheet_index)
        # Find the last row in the sheet
        last_row = rb.sheet_by_index(sheet_index).nrows
        row = last_row
        # Track existing names to prevent duplicates
        existing_names = set(rb.sheet_by_index(sheet_index).col_values(0)[1:])
    else:
        sheet1 = wb.add_sheet(str(date.today()))
        sheet1.write(0, 0, 'Name/Date')
        sheet1.write(0, 1, str(date.today()))
        row = 1
        existing_names = set()

except FileNotFoundError:
    # If the file does not exist, create a new workbook
    wb = Workbook()
    sheet1 = wb.add_sheet(str(date.today()))
    sheet1.write(0, 0, 'Name/Date')
    sheet1.write(0, 1, str(date.today()))
    row = 1
    existing_names = set()

col = 0

while True:
    # Close the current OpenCV window before making a new choice
    cv2.destroyAllWindows()

    # Grab a single frame of video or load an image
    choice = int(input("1. Use Camera\n2. Use Image\n3. Exit\nEnter Choice: "))
    
    if choice == 1:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture image from camera.")
            continue
    elif choice == 2:
        pname = input("Enter person name: ")
        frame = cv2.imread(pname + ".jpeg")
        if frame is None:
            print(f"Error: Could not load image {pname}.jpeg")
            continue
    elif choice == 3:
        video_capture.release()
        cv2.destroyAllWindows()
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue

    # Process the frame (whether from camera or image)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

        # Check for duplicate entry
        if name in existing_names:
            print(f"Duplicate entry with {name}")
        elif name != "Unknown":
            sheet1.write(row, col, name)
            col = col + 1
            sheet1.write(row, col, "Present")
            row = row + 1
            col = 0
            existing_names.add(name)
            print(f"Attendance taken for {name}")
            wb.save('attendence_excel.xls')

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image or video frame
    cv2.imshow('Video', frame)

    # Automatically close the window if 'q' is pressed or attendance is recorded
    if cv2.waitKey(1) == ord('q'):
        print("Exiting...")
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
