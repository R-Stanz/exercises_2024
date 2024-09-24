import cv2
import numpy as np
from skimage.measure import LineModelND, ransac

# Load the image
image = cv2.imread('pontos_ransac.png')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold to isolate green points
green_mask = cv2.inRange(image, (0, 255, 0), (0, 255, 0))

# Find contours of green points
contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


# Extract point coordinates
points = []
for contour in contours:
    for point in contour:
        points.append(point[0])

# Convert points to NumPy array
points = np.array(points)

# Reshape points for ransac
points = points.reshape(-1, 2)  # Each row is a point (x, y)

# Perform RANSAC line fitting
model, inliers = ransac(points,
                        LineModelND,
                        min_samples=15,
                        residual_threshold=1,
                        max_trials=100)

# Get inlier points
inlier_points = points[inliers]

# Draw lines on a new image
new_image = image.copy()
for i in range(len(inlier_points) - 1):
    cv2.line(new_image, tuple(inlier_points[i]), tuple(inlier_points[i + 1]), (0, 0, 255), 2)

# Display the result
cv2.imshow('RANSAC Lines', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
