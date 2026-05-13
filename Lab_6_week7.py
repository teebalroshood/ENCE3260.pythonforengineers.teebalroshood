import cv2
import numpy as np

# Load image
img = cv2.imread("img_3.jpg")

# Make a copy for drawing
output = img.copy()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur slightly to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Threshold image
# Chocolates are darker -> use inverse threshold
_, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

count = 0

for contour in contours:

    # Area of contour
    area = cv2.contourArea(contour)

    # Ignore tiny noise regions
    if area > 500:

        count += 1

        # Get center of contour
        M = cv2.moments(contour)

        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            # Draw contour
            cv2.drawContours(output, [contour], -1, (0, 255, 0), 2)

            # Draw number
            cv2.putText(
                output,
                str(count),
                (cx - 10, cy),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

# Print final count
print("Total chocolates detected:", count)

# Show images
cv2.imshow("Threshold", thresh)
cv2.imshow("Detected Chocolates", output)

cv2.waitKey(0)
cv2.destroyAllWindows()