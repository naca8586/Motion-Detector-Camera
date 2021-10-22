# Main Script for Video Vision AI Information
# Google Vision
from google.cloud import vision
# Date and Time for file
from datetime import datetime
# For User arguments
import sys
# OpenCV
import cv2
# File management
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key.json"

# CLI Arguments
# eg: vfext.py SRC//video.mp4 0 100
str(sys.argv)

# Open Video
cap= cv2.VideoCapture(sys.argv[1])

# CLI Argument frame start position
i = 2

# Video frame Extractor
def vfext(i):
	# Loop while Current read position has not reached end of CLI args
	while (i != len(sys.argv)):
		# Set Read location
		cap.set (1,int(sys.argv[i]))
		# Execute Read
		ret, frame = cap.read()
		
		# Error Checking
		if ret == False:
			print ('Frame Error')
			break
		
		# Write frames
		cv2.imwrite (str(sys.argv[i])+'.jpg',frame)
	
		i += 1

	# CleanUp
	cap.release()
	cv2.destroyAllWindows()

def gvai(i):
	with open(str(sys.argv[i])+'.jpg', 'rb') as imgjpg:
		content = imgjpg.read()
	
	client = vision.ImageAnnotatorClient()	
	image = vision.Image(content=content)	
	response = client.label_detection(image=image)
	return response

# Video Frame Extractor	
vfext(i)

# pre trigger response
rpre = gvai(i)
# post trigger response
rpst = gvai(i+1)

# Place holder
rpredset = ['NULL']
rpstdset = ['NULL']

# convert json response to label list
for label in rpre.label_annotations:
	rpredset.append(label.description)

for label in rpst.label_annotations:
	rpstdset.append(label.description)

# Get difference between responses	
triggers = set(rpredset).symmetric_difference(set(rpstdset))

# Write Vision AI Data to file
with open(os.path.join('DAT', os.path.basename(str(sys.argv[1])) +'_data.txt'), 'w') as txt:
	txt.write('Video File: ' + os.path.basename(str(sys.argv[1])) + '\nDate: ' + str(datetime.now()) + '\n\n')
	txt.write('Pre Trigger Data. Frame: ' + str(sys.argv[2]) + '\n' + str(set(rpredset)) + '\n\n')
	txt.write('Post Trigger Data. Frame: ' + str(sys.argv[3]) + '\n' + str(set(rpstdset)) + '\n\n')
	txt.write('Difference.\n' + str(triggers) + '\n')
	
# Cleanup extracted images
while (i != len(sys.argv)):
	os.remove(str(sys.argv[i])+'.jpg')
	i += 1