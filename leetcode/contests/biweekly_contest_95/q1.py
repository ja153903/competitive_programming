DIMENSION_THRESHOLD = 10 ** 4
VOLUME_THRESHOLD = 10 ** 9


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_bulky = (length >= DIMENSION_THRESHOLD or width >= DIMENSION_THRESHOLD or height >= DIMENSION_THRESHOLD) or \
                   (length * width * height >= VOLUME_THRESHOLD)
        is_heavy = mass >= 100

        if is_bulky and is_heavy:
            return "Both"
        elif is_bulky:
            return "Bulky"
        elif is_heavy:
            return "Heavy"
        else:
            return "Neither"
