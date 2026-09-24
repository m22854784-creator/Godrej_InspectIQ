import cv2

from inspection.reference_comparator import compare_with_reference

image = cv2.imread(
    r"dataset\defective\Designer (2).png"
)

contours = compare_with_reference(
    image
)

print("Contours Found:", len(contours))