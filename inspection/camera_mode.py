import cv2

from inspection.inspection_engine import inspect
from inspection.result_visualizer import draw_result


def run_camera_mode():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.flip(frame, 1)

        h, w = frame.shape[:2]

        x1 = int(w * 0.25)
        y1 = int(h * 0.25)

        x2 = int(w * 0.75)
        y2 = int(h * 0.75)

        # Draw ROI guide box

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "PLACE COMPONENT HERE",
            (x1, y1 - 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2
        )

        roi = frame[y1:y2, x1:x2]

        result = inspect(roi)

        output_roi = draw_result(
            roi,
            result
        )

        frame[y1:y2, x1:x2] = output_roi

        cv2.imshow(
            "Godrej InspectIQ Live",
            frame
        )

        key = cv2.waitKey(1)

        if key == 27:  # ESC
            break

    cap.release()
    cv2.destroyAllWindows()
