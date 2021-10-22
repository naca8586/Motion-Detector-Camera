# For User arguments
import sys
# OpenCV
import cv2

# CLI Arguments
# eg: vfext.py SRC//video.mp4 0 100 1000
str(sys.argv)

# Open Video
cap= cv2.VideoCapture(sys.argv[1])

# CLI Argument frame start position
i = 2

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
		
	# Write frame
	cv2.imwrite (str(sys.argv[i])+'.jpg',frame)
	
	i += 1

# CleanUp
cap.release()
cv2.destroyAllWindows()