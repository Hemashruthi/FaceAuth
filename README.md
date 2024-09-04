# Face Recognition System with Student ID Encoding

This project demonstrates a face recognition system that encodes student images and compares them with a test image to identify known faces. The system is built using Python, OpenCV, and the `face_recognition` library.

## Features

- **Student Image Encoding:** The system reads student images from a specified folder, encodes their facial features, and associates these encodings with student IDs.
- **Face Recognition:** It loads a test image, detects faces in the image, and compares these faces with the encoded student faces to identify known individuals.
- **Pickle Serialization:** The encoded data (student face encodings and IDs) is serialized and saved using Python's `pickle` module for later use.

## Technology Stack

- **Python:** The core language used for development.
- **OpenCV:** Used for image processing tasks.
- **face_recognition:** A Python library for face recognition tasks.

## Folder Structure

- `Images/`: Contains the images of students. Each image file should be named according to the student's ID (e.g., `12345.jpg`).

## How It Works

### Encoding Student Faces

1. **Load Student Images:** Images of students are loaded from the `Images/` directory.
2. **Encode Faces:** The faces in these images are encoded using the `face_recognition` library.
3. **Save Encodings:** The encodings and student IDs are saved to a file (`SaveFile.p`) using `pickle`.

### Recognizing Faces in a Test Image

1. **Load Encodings:** The saved encodings and student IDs are loaded from `SaveFile.p`.
2. **Process Test Image:** The test image is loaded, and faces are detected and encoded.
3. **Compare Faces:** The detected faces are compared against the stored encodings to identify known faces.
4. **Result:** The system prints whether the detected face matches any of the known faces and, if so, the corresponding student ID.

## Usage

1. **Install Dependencies:**
   ```bash
   pip install opencv-python face_recognition numpy
   ```

2. **Run the Encoding Script:**
   ```bash
   python encode_faces.py
   ```

3. **Run the Recognition Script:**
   ```bash
   python recognize_faces.py
   ```
