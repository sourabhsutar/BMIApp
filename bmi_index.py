dataList = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, 
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, 
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

def calculateBMI(weightKg,heightCm):
    try:
        bmi = round(weightKg/(heightCm/100)**2,2)
    except(ValueError, ZeroDivisionError):
        bmi = 0
    
    return bmi

def BMICatgHealthRisk(bmi):
    BMIInfo = []
    if(bmi <= 18.4):
        BMIInfo = ['Underweight','Malnutrition risk']
    elif(18.4 <= bmi <= 24.9):
        BMIInfo = ['Normal weight','Low risk']
    elif(25 <= bmi <= 29.9):
        BMIInfo = ['Overweight','Enhanced risk']
    elif(18.4 <= bmi <= 24.9):
        BMIInfo = ['Normal weight','Low risk']
    elif(30 <= bmi <= 34.9):
        BMIInfo = ['Moderately obese','Medium risk']
    elif(35 <= bmi <= 39.9):
        BMIInfo = ['Severely obese','High risk']
    else:
        BMIInfo = ['Very severely obese','Very high risk']

    return BMIInfo

overweightCount = 0
for index,data in enumerate(dataList):
        bmi = calculateBMI(float(data['WeightKg']),float(data['HeightCm']))
        dataList[index]['BMI'] = bmi
        BMICategory,HealthRisk = BMICatgHealthRisk(bmi)
        dataList[index]['BMICategory'] = BMICategory
        dataList[index]['HealthRisk'] = HealthRisk
        if(BMICategory == 'Overweight'):
            overweightCount += 1


print(dataList)
print(f"Total OverWeight Count  {overweightCount}")