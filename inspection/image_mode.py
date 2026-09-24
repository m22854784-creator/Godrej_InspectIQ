import cv2

from inspection.inspection_engine import inspect
from inspection.result_visualizer import draw_result


def run_image_mode(image_path):

    image = cv2.imread(image_path)

    result = inspect(image)

    output = draw_result(
        image,
        result
    )

    cv2.imshow(
        "Godrej InspectIQ",
        output
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()