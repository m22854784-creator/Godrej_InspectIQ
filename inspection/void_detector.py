import cv2

def detect_voids(mask):

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    large_contours = 0

    for contour in contours:

        area = cv2.contourArea(contour)

        if area > 20000:
            large_contours += 1

    return large_contours