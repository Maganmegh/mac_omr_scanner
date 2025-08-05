import cv2
import numpy as np

# Load the image (ensure the image is in the same folder)
img = cv2.imread("sample_omr.jpg")
if img is None:
    print("Image not found. Make sure 'sample_omr.jpg' is in the same folder.")
    exit()

# Convert to grayscale and threshold
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Find contours (mock detection logic for now)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"Detected {len(contours)} contours (sample OMR processing logic).")
