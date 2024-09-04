"""
This code calculates the cell recovery for preparations obtained from umbilical cord blood
based on the data entered by the user.
"""

import pandas as pd

results = []

# A loop is used to calculate the recovery for multiple preparations 
# and store the results in a single table.
while True:
    print("Enter the value of WBC1 (or 'q' to quit):")
    WBC1 = input()
    if WBC1.lower() == 'q':
        break
    WBC1 = float(WBC1)

    print("Enter the value of WBC2:")
    WBC2 = float(input())

    print("Enter the blood volume without CPD:")
    V2 = int(input())

    print("Enter the blood volume with CPD:")
    V_CPD = int(input())

    # Calculating recovery based on the blood volume with CPD.
    # If the blood volume without CPD >= 120, then V1 is 42, otherwise V1 is 22.
    if V2 >= 120:
        V1 = 42
        recovery = round((WBC2*V1)*100/(WBC1*V2),2)
        results.append([WBC1, WBC2, V2, V_CPD, recovery, 'Recovery with division (%)'])
    else:
        V1 = 22
        recovery = round((WBC2*V1)* 100/(WBC1*V2),2)
        results.append([WBC1, WBC2, V2, V_CPD, recovery, 'Recovery without division (%)'])

column_names = ['WBC1', 'WBC2', 'Volume without CPD', 'Volume with CPD', 'Recovery (%)', 'Type of recovery']
df = pd.DataFrame(results, columns=column_names)

print(df)
