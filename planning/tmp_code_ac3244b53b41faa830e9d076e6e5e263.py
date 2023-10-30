import cv2

# Load the image
image = cv2.imread('path_to_your_image')

# Define new width and height
new_width = 800
new_height = 800

# Resize the image
resized_image = cv2.resize(image, (new_width, new_height), interpolation = cv2.INTER_CUBIC)

# Save the resized image
cv2.imwrite('path_to_save_resized_image', resized_image)