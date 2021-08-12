import json 

def getData():                                       #loads data from json file to bmi (Dict)
  try: 
    f = open('bmi_data.json',)
    bmi = json.load(f) 
  except:
    print("Input file missing")
  finally: f.close  
  return bmi  

def calculateBMI(bmi):
  for i in bmi['BMI_DATA']:
    if(i["HeightCm"]>0 and  i["WeightKg"] >0):                    #accepts only positive values for Height and Weight
        bmiValue = i["WeightKg"]/((i["HeightCm"]/100)**2)
        i["BMI_Value"] = bmiValue
    else:
        print("Weight or Height should be greater than zero for "+str(i+1)+"th row")
        bmiValue =0                                                #assigns zero bmiValue to these cases

        
      
    
def bmi_results(bmi):                                           #adds bmiCategory and health risks to the array
  for i in bmi['BMI_DATA']:
    if(i["BMI_Value"] <=18.4 ):
      i["BMI_Category"] = "Underweight"
      i["Health_Risk"] = "Malnutrition risk"
    elif(i["BMI_Value"] >=18.5 and i["BMI_Value"] <= 24.9 ):
      i["BMI_Category"] = "Normal Weight"
      i["Health_Risk"] = "Low risk"
    elif(i["BMI_Value"] >=25 and i["BMI_Value"] <= 29.9 ):
      i["BMI_Category"] = "Overweight"
      i["Health_Risk"] = "Enhanced risk"
    elif(i["BMI_Value"] >=30 and i["BMI_Value"] <= 34.9 ):
      i["BMI_Category"] = "Moderately obese"
      i["Health_Risk"] = " Medium risk"          
    elif(i["BMI_Value"] >=35 and i["BMI_Value"] <= 39.9 ):
      i["BMI_Category"] = "Severely obese"
      i["Health_Risk"] = "High risk"
    elif (i["BMI_Value"] >=40 ):
      i["BMI_Category"] = "Very severely obese"
      i["Health_Risk"] = "Very high risk"  
    print(i)  

def count_on_BMI_Category(category,bmi):           # counts frequency of particular category of people
  count = 0
  for i in bmi["BMI_DATA"]:
    if(i["BMI_Category"]==category):  
     count=count+1
  print("Then number of "+category+" people are: "+str(count))


def main():                                            
  bmi = getData()
  calculateBMI(bmi)
  bmi_results(bmi)
  count_on_BMI_Category("Overweight",bmi)

if __name__ == "__main__":
    main()


