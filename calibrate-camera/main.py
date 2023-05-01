import numpy as np
import cv2

# change to number of calibration images entered, try to have between 10-15
NUM_CALIBRATION_IMAGES = 11

# number of points on checkerboard (in checkerboard.jpeg)
CHECKERBOARD_SIZE = (17, 11) # number points x axis, number points y axis
# if you want to use a different checkerboard, just adjust these values

# Define the termination criteria for the iterative calibration algorithm
CRITERIA = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Create arrays to store object points and image points from all the images
obj_points = []
img_points = []

# Get a list of image filenames
img_filenames = [f"calibrate-camera/images/img{num}.jpg" for num in range(1, NUM_CALIBRATION_IMAGES)]

# Prepare the object points (0,0,0), (1,0,0), ..., (8,5,0)
objp = np.zeros((CHECKERBOARD_SIZE[0]*CHECKERBOARD_SIZE[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:CHECKERBOARD_SIZE[0], 0:CHECKERBOARD_SIZE[1]].T.reshape(-1,2)

# Loop through all the images and find the checkerboard corners
for img_filename in img_filenames:
    img = cv2.imread(img_filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the corners in the checkerboard pattern
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD_SIZE, None)

    if ret:
        obj_points.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), CRITERIA)
        img_points.append(corners2)

# Calibrate the camera using the object points and image points
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)

# Print the intrinsic parameters
print(f"Distortion coefficients: {dist}")
print(f"fx: {mtx[0][0]}")
print(f"fy: {mtx[1][1]}")
print(f"cx: {mtx[0][2]}")
print(f"cy: {mtx[1][2]}")
