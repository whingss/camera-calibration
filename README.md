# Camera-calibration  
Camera calibration script which outputs focal lengths along x and y axis, along with coordinates of a principle point (outputs intristic parameters of a camera).  

# Usage
Install requirments.txt by:  
-cd'ing into the camera-calibration folder. 
-entering: pip install -r requirements.txt. 

## Using checkerboard.jpeg  
Print out the file  
Take 10-15 images from various angles/brightnesses and replace the ones in the 'images' folder  
Run the program  

## Using an alternative checkerboard  
Print out your desired checkerboard  
Count the number of 'points' on your checkerboard, on the example checkerboard there are 17 points x axis and 11 points y axis. Replace the CHECKERBOARD_SIZE variable accordingly  
Run the program  

