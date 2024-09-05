# AutoAttend

## Overview
AutoAttend is an automated facial recognition attendance system designed to streamline attendance tracking in educational and workplace environments. By leveraging the power of OpenCV and face recognition algorithms, AutoAttend achieves high accuracy in identifying individuals and automatically recording their attendance. The system is ideal for environments where reliable and efficient management of attendance is crucial. 

The project was developed using a Raspberry Pi and OpenCV, achieving an impressive 99.38% accuracy on the Labeled Faces in the Wild (LFW) benchmark. AutoAttend significantly reduces the need for manual intervention, ensuring a seamless and efficient attendance process. 

## Features
+ High Accuracy: Achieves 99.38% accuracy on the LFW benchmark.
Automated Attendance Recording: Automatically records attendance by recognizing individuals' faces.
+ Efficient Management: Streamlines the attendance process, reducing manual intervention and enhancing overall efficiency.
+ Ideal for Various Environments: Suitable for educational institutions, workplaces, and other environments where reliable attendance management is essential.
  
# Setup and Installation
**Prerequisites**  
Before running the AutoAttend system, ensure you have the following installed on your system:

+ Python 3.x
+ OpenCV (cv2)
+ face_recognition library
+ numpy
+ xlwt, xlrd, and xlutils for handling Excel files 
You can install the necessary Python packages using pip:

```bash
pip install opencv-python face_recognition numpy xlwt xlrd xlutils
```

**Directory Structure**  
Ensure your project directory is structured as follows:
```bash
AutoAttend/
│
├── person1.png           # Image file for the first person
├── person2.png           # Image file for the second person
├── attendance_excel.xls  # Excel file for recording attendance (auto-created if not present)
└── auto_attend.py        # Main script file
```

**Setting Up Images**  
+ Place the images of individuals to be recognized in the project directory.
+ Ensure that the image filenames correspond to the individuals' names (e.g., `person1.png`, `person2.png`).
+ The system will use these images to create face encodings and match them during attendance recording. 

**Running the Script**  
To start the AutoAttend system, navigate to the project directory and run the script:

```bash
python auto_attend.py
```

**Usage Instructions**
1. **Use Camera**: Select option `1` to capture a frame from the webcam and recognize faces in real-time.
2. **Use Image**: Select option `2` to load and process a specific image from the directory.
3. **Exit**: Select option `3` to exit the program.
     
The system will automatically record attendance for recognized individuals and save it in the `attendance_excel.xls` file. If a duplicate entry is detected, it will be ignored, and a message will be displayed in the console.

## Notes
+ The `attendance_excel.xls` file will be created automatically if it doesn't exist. The system will append attendance records to this file daily.
+ Ensure the webcam is properly connected and accessible if you choose to use the camera option.

## Project Description
AutoAttend was devised as a solution to automate and enhance the attendance tracking process. Utilizing Raspberry Pi and OpenCV, the system has been fine-tuned to achieve exceptional accuracy in facial recognition, making it reliable for daily use in environments where managing attendance is crucial.

The project has been designed with scalability in mind, allowing it to be adapted for various settings, from classrooms to corporate offices. By reducing manual intervention, AutoAttend not only saves time but also minimizes the risk of errors, making it a robust tool for managing attendance efficiently.
