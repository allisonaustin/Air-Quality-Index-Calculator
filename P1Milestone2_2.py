
import math
highest_AQI = []
loc_names = []
PM_25List = []

#function for defining final air quality based on maximum AQI across IP's
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

#number of locations for which the AQI will be calculated
#MUST be a POSITIVE integer
print('Air Quality Index Calculator')
num_locations = int(input('How many locations for this report? '))

#while the user inputs a negative number of locations, or 0, ask again
while num_locations <= 0:
    num_locations = int(input('How many locations for this report? '))

for i in range(1,num_locations + 1):
    AQI = []
    locName = input("\n"'What is the name of Location '+str(i)+'? ')
    PM_2_5 = float(input("\n"'-> Enter PM-2.5 concentration: '))
    PM_2_5 = int(PM_2_5 * 10.0)
    PM_2_5 = float(PM_2_5 / 10.0)
    
    if PM_2_5 <= 12.0:
        C_low,C_high,I_low,I_high = 0.0,12.0,0,50
    elif PM_2_5 > 12.0 and PM_2_5 <= 35.4:
        C_low,C_high,I_low,I_high = 12.1,35.4,51,100
    elif PM_2_5 > 35.4 and PM_2_5 <= 55.4:
        C_low,C_high,I_low,I_high = 35.5,55.4,101,150
    elif PM_2_5 > 55.4 and PM_2_5 <= 150.4:
        C_low,C_high,I_low,I_high = 55.5,150.4,151,200
    elif PM_2_5 > 150.4 and PM_2_5 <= 250.4:
        C_low,C_high,I_low,I_high = 150.5,250.4,201,300
    elif PM_2_5 <= 500.4 and PM_2_5 > 250.4:
        C_low,C_high,I_low,I_high = 250.5,500.4,301,500

    #Ip calculation using numbers grabbed from if statements
    #PM-2.5 concentration must be positive for this calculation to execute
    if PM_2_5 >= 0 and PM_2_5 <= 500.4:
        a_Ip = round(((I_high - I_low) * (PM_2_5 - C_low) / (C_high - C_low) + I_low))
        AQI.append(a_Ip)
        print("\n"'   PM-2.5 concentration of',PM_2_5,'is index level',a_Ip)
        if PM_2_5 > 0:
            PM_25List.append(PM_2_5)

    PM_10 = float(input("\n"'-> Enter PM-10 concentration: '))
    #rounds down the float of pm-10 entered by user
    PM_10 = math.trunc(PM_10)

    while PM_10 < 0:
        PM_10 = float(input("\n"'-> Enter a PM-10 concentration: '))
        PM_10 = int(PM_10)

    if PM_10 <= 54:
        C_low,C_high,I_low,I_high = 0,54,0,50
    elif PM_10 <= 154 and PM_10 > 54:
        C_low,C_high,I_low,I_high = 55,154,51,100
    elif PM_10 <= 254 and PM_10 > 154:
        C_low,C_high,I_low,I_high = 155,254,101,150
    elif PM_10 <= 354 and PM_10 > 254:
        C_low,C_high,I_low,I_high = 255,354,151,200
    elif PM_10 <= 424 and PM_10 > 354:
        C_low,C_high,I_low,I_high = 355,424,201,300
    
    elif PM_10 <= 604 and PM_10 > 424:
        C_low,C_high,I_low,I_high = 425,604,301,500 

    if PM_10 >= 0 and PM_10 <= 604: 
        b_Ip = round(((I_high - I_low) * (PM_10 - C_low) / (C_high - C_low) + I_low))
        print("\n"'   PM-10 concentration of',PM_10,'is index level',b_Ip)
        AQI.append(b_Ip)

    NO_2 = int(float(input("\n"'-> Enter NO-2 concentration: ')))

    if NO_2 <= 54:
        C_low,C_high,I_low,I_high = 0,53,0,50

    elif NO_2 <= 100 and NO_2 > 53:
        C_low,C_high,I_low,I_high = 54,100,51,100
    
    elif NO_2 <= 360 and NO_2 > 100:
        C_low,C_high,I_low,I_high = 101,360,101,150
    
    elif NO_2 <= 649 and NO_2 > 360:
        C_low,C_high,I_low,I_high = 361,649,151,200
    
    elif NO_2 <= 1249 and NO_2 > 649:
        C_low,C_high,I_low,I_high = 650,1249,201,300
    
    elif NO_2 <= 2049 and NO_2 > 1249:
        C_low,C_high,I_low,I_high = 1250,2049,301,500

    if NO_2 >= 0 and NO_2 <= 2049:
        c_Ip = round(((I_high - I_low) * (NO_2 - C_low) / (C_high - C_low) + I_low))
        print("\n"'   NO-2 concentration of',NO_2,'is index level',c_Ip)
        AQI.append(c_Ip)

    SO_2 = float(input("\n"'-> Enter SO-2 concentration: '))
    SO_2 = math.trunc(SO_2)

    if SO_2 <= 35:
        C_low,C_high,I_low,I_high = 0,35,0,50
    
    elif SO_2 <= 75 and SO_2 > 35:
        C_low,C_high,I_low,I_high = 36,75,51,100
    
    elif SO_2 <= 185 and SO_2 > 75:
        C_low,C_high,I_low,I_high = 76,185,101,150
    
    elif SO_2 <= 304 and SO_2 > 185:
        C_low,C_high,I_low,I_high = 186,304,151,200
    
    elif SO_2 <= 604 and SO_2 > 304:
        C_low,C_high,I_low,I_high = 305,604,201,300
    
    elif SO_2 <= 1004 and SO_2 > 604:
        C_low,C_high,I_low,I_high = 605,1004,301,500

    if SO_2 >= 0 and SO_2 <= 1004:
        d_Ip = round(((I_high - I_low) * (SO_2 - C_low) / (C_high - C_low) + I_low))
        print("\n"'   SO-2 concentration of',SO_2,'is index level',d_Ip)
        AQI.append(d_Ip)

    CO = float(input("\n"'-> Enter CO concentration: '))
    #truncating CO concentration to one decimal
    #we take the int of moving the decimal to the right by one of CO
    #and taking the float of moving it back to the left ( CO / 10 )
    CO = int(CO * 10.0)
    CO = float(CO / 10.0)

    if CO <= 4.4:
        C_low,C_high,I_low,I_high = 0,4.4,0,50
    
    elif CO <= 9.4 and CO > 4.4:
        C_low,C_high,I_low,I_high = 4.4,9.4,51,100
    
    elif CO <= 12.4 and CO > 9.4:
        C_low,C_high,I_low,I_high = 9.5,12.4,101,150
    
    elif CO <= 15.4 and CO > 12.5:
        C_low,C_high,I_low,I_high = 12.5,15.4,151,200
    
    elif CO <= 30.4 and CO > 15.4:
        C_low,C_high,I_low,I_high = 15.5,30.4,201,300
    
    elif CO <= 50.4 and CO > 30.4:
        C_low,C_high,I_low,I_high = 30.5,50.4,301,500

    if CO >= 0 and CO <= 50.4:
        e_Ip = round(((I_high - I_low) * (CO - C_low) / (C_high - C_low) + I_low))
        print("\n"'   CO concentration of',CO,'is index level',e_Ip)    
        AQI.append(e_Ip)

    O_3 = float(input("\n"'-> Enter O3 concentration: '))
    O_3 = math.trunc(O_3)

    if O_3 <= 164 and O_3 >= 125:
        C_low,C_high,I_low,I_high = 125,164,101,150
    elif O_3 <= 204 and O_3 > 164:
        C_low,C_high,I_low,I_high = 165,204,151,200
    elif O_3 <= 404 and O_3 > 204:
        C_low,C_high,I_low,I_high = 205,404,201,300
    elif O_3 <= 604 and O_3 > 404:
        C_low,C_high,I_low,I_high = 405,604,301,500 

    if O_3 >= 125 and O_3 <= 604:
        f_Ip = round(((I_high - I_low) * (O_3 - C_low) / (C_high - C_low) + I_low))
        print("\n"'   O3 concentration of',O_3,'is index level',f_Ip)
        AQI.append(f_Ip)

    #final comparison across all Ip's, takes the maximum AQI value
    AQI_final = max(AQI)
    
    #adding the final aqi's of all the locations and names into lists we will use later to find the max
    loc_names.append(locName)
    highest_AQI.append(AQI_final)

    #final print statements
    print("\n"'AQI for',locName,'is', AQI_final)

    #calling air quality function to retrieve the air quality of the maximum AQI
    air_quality = airQuality(AQI_final)
    print('Air Quality:',air_quality) 

#summary of all locations (if number of locations is more than 1)
if num_locations > 1:
    #location name of the highest AQI is the same index as the max AQI from the highest_AQI list
    i = highest_AQI.index(max(highest_AQI))
    locNameMax = loc_names[i]
    print("\n"'Summary:',"\n"'   Location with highest AQI is',locNameMax,'('+str(max(highest_AQI))+')')
    
    if len(PM_25List) > 0:
        #calculating average PM-2.5 concentration across all locations
        b = float(sum(PM_25List))
        avgPM25 = float(b / len(PM_25List))
        avgPM25 = int(avgPM25 * 10.0)
        avgPM25 = float(avgPM25 / 10.0)
        print("\n""   Average PM-2.5 concentration:",avgPM25)
