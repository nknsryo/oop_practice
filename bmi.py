
import self as self


class BMI:
    def __init__(self, height_m, weight_kg):
        self.value = weight_kg / height_m ** 2
        if not (10 <= self.value <= 40):
            raise ValueError(f"MBIが正常値を外れています!!{self.value}")

    def __str__(self):
        return f"{self.value:.2f}"


noriya = BMI(height_m=1.7, weight_kg=65)
print(noriya.value)
