import cv2

from inspection.glue_detector import detect_glue


def compare_with_reference(image):

    reference = cv2.imread(
        "reference/good_reference.jpeg"
    )

    if reference is None:
        return []

    reference = cv2.resize(
        reference,
        (image.shape[1], image.shape[0])
    )

    ref_mask, _ = detect_glue(reference)

    current_mask, _ = detect_glue(image)

    difference = cv2.absdiff(
        ref_mask,
        current_mask
    )

    contours, _ = cv2.findContours(
        difference,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    defect_contours = []

    for contour in contours:

        area = cv2.contourArea(contour)

        if area > 2000:
            defect_contours.append(contour)

    return defect_contours