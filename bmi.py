"""
clss BMI:
    関連する属性:
        -身長(m)
        -体重(kg)
        -BMIという値そのもの
    ルール:
        -BMIは22が適正 10以上　40以下の範囲<=常識的な範囲
        -表示する時には小数点以下第2位まで四捨五入
            -ex:23.689 =>23.69
            -ex:23.681 =>23.68
    できること:
        -BMIの計算


"""


class BMI:
    def __init__(self, height_m, weight_kg):
        # self.height_m = height_m
        # self.weight_kg = weight_kg
        self.value = self.weight_kg / self.height_m ** 2


noriya = BMI(height_m=1.7, weight_kg=65)
# print(noriya.height_m)
# print(noriya.weight_kg)
print(noriya.value)
