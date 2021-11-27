percentageEquivalent = float(input("INPUT GRADE: "))
if percentageEquivalent >=96:
    print("GRADE/MARK: 1.0 ")
    print("DESCRIPTION: EXCELLENT ")
elif round(93<=percentageEquivalent<=96):
    print("GRADE/MARK: 1.25 ")
    print("DESCRIPTION: EXCELLENT ")   
elif round(90<=percentageEquivalent<93):
    print("GRADE/MARK: 1.5 ")
    print("DESCRIPTION: VERY GOOD ")    
elif round(87<=percentageEquivalent<90):
    print("GRADE/MARK: 1.75 ")
    print("DESCRIPTION: VERY GOOD ") 
elif round(84<=percentageEquivalent<87):
    print("GRADE/MARK: 2.0 ")
    print("DESCRIPTION: GOOD ")             
elif round(81<=percentageEquivalent<84):
    print("GRADE/MARK: 2.25 ")
    print("DESCRIPTION: GOOD ")    
elif round(78<=percentageEquivalent<81):
    print("GRADE/MARK: 2.5 ")   
    print("DESCRIPTION: SATISFACTORY ") 
elif round(76<=percentageEquivalent<78):
    print("GRADE/MARK: 2.75 ")
    print("DESCRIPTION: SATISFACTORY ")  
elif round(65<=percentageEquivalent<74): 
    print("GRADE/MARK: 5.0")
    print("DESCRIPTION: FAILURE ")
elif percentageEquivalent == 75:
    print("GRADE/MARK: 3.0 ")
    print("DESCRIPTION: PASSING ")    
