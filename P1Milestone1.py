
import math
#number of locations for which the AQI will be calculated
#MUST be a POSITIVE integer
print('Air Quality Index Calculator')
num_locations = int(input('How many locations for this report? '))

def airQuality(AQI_final):
    if AQI_final <= 50:
        air_quality = "Good"
    elif AQI_final <=100 and AQI_final > 50:
        air_quality = "Moderate"
    elif AQI_final <= 150 and AQI_final > 100:
        air_quality = "Unhealthy for Sensitive Groups"
    elif AQI_final <= 200 and AQI_final > 150:
        air_quality = "Unhealthy"
    elif AQI_final <= 300 and AQI_final > 200:
        air_quality = "Very Unhealthy"
    else:
        air_quality = "Hazardous"
    return air_quality


#if number of locations is negative, ask again
while num_locations < 0:
    num_locations = int(input('How many locations for this report? '))

for i in range(1,num_locations + 1):
    locName = input("\n"'What is the name of Location '+str(i)+'? ')
    PM_2_5 = float(input("\n"'-> Enter PM-2.5 concentration: '))
    PM_2_5 = int(PM_2_5 * 10.0)
    PM_2_5 = float(PM_2_5 / 10.0)

    
    if PM_2_5 <= 12.0:
        C_low,C_high = 0.0,12.0
        I_low = 0
        I_high = 50
    elif PM_2_5 > 12.0 and PM_2_5 <= 35.4:
        C_low,C_high = 12.1,35.4
        I_low = 100
        I_high = 51
    elif PM_2_5 > 35.4 and PM_2_5 <= 55.4:
        C_low,C_high = 35.5,55.4
        I_low = 101
        I_high = 150
    elif PM_2_5 > 55.4 and PM_2_5 <= 150.4:
        C_low,C_high = 55.5,150.4
        I_low = 151
        I_high = 200
    elif PM_2_5 > 150.4 and PM_2_5 <= 250.4:
        C_low,C_high = 150.5,250.4
        I_low = 201
        I_high = 300
    else:
        C_low,C_high = 250.5,500.4
        I_low = 301
        I_high = 500
    
    #Ip calculation using numbers grabbed from if statements
    a_Ip = round(((I_high - I_low)/(C_high - C_low) * (PM_2_5 - C_low) + I_low))
    print("\n"'   PM-2.5 concentration of',PM_2_5,'is index level',a_Ip)
    
    PM_10 = float(input("\n"'-> Enter PM-10 concentration: '))
    #rounds down the float of pm-10 entered by user
    PM_10 = math.trunc(PM_10)

    if PM_10 < 0:
        PM_10 = float(input("\n"'-> Enter a PM-10 concentration: '))
        PM_10 = int(PM_10)

    if PM_10 <= 54:
        C_low,C_high = 0,54
        I_low = 0
        I_high = 50
    elif PM_10 <= 154 and PM_10 > 54:
        C_low,C_high = 55,154
        I_low = 51
        I_high = 100
    elif PM_10 <= 254 and PM_10 > 154:
        C_low,C_high = 155,254
        I_low = 101
        I_high = 150
    elif PM_10 <= 354 and PM_10 > 254:
        C_low,C_high = 255,354
        I_low = 151
        I_high = 200
    elif PM_10 <= 424 and PM_10 > 354:
        C_low,C_high = 355,424
        I_low = 201
        I_high = 300
    
    else:
        C_low,C_high = 425,604
        I_low = 301
        I_high = 500 

    #Ip calculation for pm-10 concentration
    b_Ip = round(((I_high - I_low)/(C_high - C_low) * (PM_10 - C_low) + I_low))
    print("\n"'   PM-10 concentration of',PM_10,'is index level',b_Ip)
    
    NO_2 = float(input("\n"'-> Enter NO-2 concentration: '))
    NO_2 = math.trunc(NO_2)


    if NO_2 <= 54:
        C_low,C_high = 0,54
        I_high = 50
        I_low = 0
    
    elif NO_2 <= 100 and NO_2 > 53:
        C_low,C_high = 54,100
        I_high = 100
        I_low = 51
    
    elif NO_2 <= 360 and NO_2 > 100:
        C_low,C_high = 101,360
        I_high = 150 
        I_low = 101
    
    elif NO_2 <= 649 and NO_2 > 360:
        C_low,C_high = 361,649
        I_high = 200
        I_low = 151
    
    elif NO_2 <= 1249 and NO_2 > 649:
        C_low,C_high = 650,1249
        I_high = 300
        I_low = 201
    
    else:
        C_low,C_high = 1250,2049
        I_high = 500
        I_low = 301

    c_Ip = round(((I_high - I_low)/(C_high - C_low) * (NO_2 - C_low) + I_low))
    print("\n"'   NO-2 concentration of',NO_2,'is index level',c_Ip)
    
    #final comparison across all Ip's, takes the maximum AQI value
    AQI = [a_Ip,b_Ip,c_Ip]
    AQI_final = max(AQI)

    air_quality = airQuality(AQI_final)

    #final print statements
    print("\n"'AQI for',locName,'is', AQI_final)
    print('Air Quality:',air_quality)


        
        
    






