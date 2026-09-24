import cv2

from inspection.inspection_engine import inspect
from inspection.result_visualizer import draw_result


def run_camera_mode():

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        result = inspect(frame)

        output = draw_result(
            frame,
            result
        )

        cv2.imshow(
            "Godrej InspectIQ Live",
            output
        )

        key = cv2.waitKey(1)

        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()