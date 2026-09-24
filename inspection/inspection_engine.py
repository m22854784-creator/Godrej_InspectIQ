from inspection.glue_detector import detect_glue
from inspection.coverage_analyzer import calculate_coverage
from inspection.void_detector import detect_voids
from inspection.reference_comparator import compare_with_reference

from config import PASS_THRESHOLD


def inspect(image):

    mask, contours = detect_glue(image)

    coverage = calculate_coverage(mask)

    voids = detect_voids(mask)

    defect_contours = compare_with_reference(image)

    status = "PASS"
    score = 100

    if coverage < PASS_THRESHOLD:
        status = "FAIL"
        score -= 70

    score -= min(voids * 5, 20)

    score = max(score, 0)

    return {
        "status": status,
        "score": score,
        "coverage": coverage,
        "voids": voids,
        "mask": mask,
        "contours": contours,
        "defect_contours": defect_contours
    }