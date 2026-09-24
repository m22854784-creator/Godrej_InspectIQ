import cv2

from config import GREEN
from config import ORANGE
from config import RED


def draw_result(image, result):

    output = image.copy()

    status = result["status"]
    score = result["score"]
    coverage = result["coverage"]

    color = GREEN

    if score < 80:
        color = ORANGE

    if status == "FAIL":
        color = RED

    # Draw Glue Region

    cv2.drawContours(
        output,
        result["contours"],
        -1,
        color,
        3
    )

    # Draw Actual Difference Regions

    for contour in result["defect_contours"]:

        area = cv2.contourArea(contour)

        if area < 2000:
            continue

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            output,
            (x, y),
            (x + w, y + h),
            RED,
            3
        )

        cv2.putText(
            output,
            "DEFECT",
            (x, max(y - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            RED,
            2
        )

    # Status Panel

    cv2.rectangle(
        output,
        (20, 20),
        (550, 190),
        color,
        3
    )

    cv2.putText(
        output,
        f"STATUS : {status}",
        (40, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        3
    )

    cv2.putText(
        output,
        f"SCORE : {score}",
        (40, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        3
    )

    cv2.putText(
        output,
        f"COVERAGE : {int(coverage)}",
        (40, 170),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

    return output