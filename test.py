#BMI判定プログラム
weight = float(input("体重(kg)は？"))
height = float(input("身長(cm)は？"))
#BMI計算
height = height / 100
bmi = weight / (height * height)
result = ""
if bmi <18.5:
    result="痩せ型"
if (18.5 <= bmi)and (bmi < 25):
    result = "標準体重"
if (25 <= bmi) and (bmi < 30):
    result = "肥満(軽)"
if (30 <= bmi):
    result = "肥満(重)"
print("BMI :",bmi)
print("判定:",result)
