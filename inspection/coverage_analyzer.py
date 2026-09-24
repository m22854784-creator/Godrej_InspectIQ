import cv2


def calculate_coverage(mask):

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    total_area = 0

    for cnt in contours:

        area = cv2.contourArea(cnt)

        if area > 500:
            total_area += area

    return total_area