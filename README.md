# Cell Recovery Calculator

## Table of Contents
- [Introduction](#introduction)
- [Technologies](#technologies)
- [Setup](#setup)
- [Features](#features)
- [Usage Examples](#usage-examples)
- [Project Status](#project-status)
- [Sources](#sources)

## Introduction
This project calculates the cell recovery for preparations obtained from umbilical cord blood based on the data entered by the user. The tool is intended to assist laboratory technicians and researchers in evaluating the efficiency of their cell recovery processes by providing quick and accurate recovery percentages.

## Technologies
The project uses the following technologies:
- Python 3.x
- Pandas library (for data handling and tabular representation)

## Setup
To run this project locally, ensure you have Python installed along with the Pandas library. Follow these steps:

1. Clone the repository or download the script.
2. Install Pandas if not already installed:

    ```bash
    pip install pandas
    ```

3. Run the script using Python:

    ```bash
    python cell_recovery_calculator.py
    ```

## Features
- Calculates cell recovery percentages based on user input.
- Supports multiple data entries in a single session.
- Displays results in a tabular format for easy interpretation.
- Differentiates recovery calculations based on blood volume with CPD.


**Explanation of Division:**<br>
When the obtained volume of umbilical cord blood is equal to or greater than 120 ml, an additional 20 ml of CPD (Citrate Phosphate Dextrose) is added to the blood volume.
This is referred to as "division" in the recovery type, which accounts for the increased volume in the calculation of the recovery percentage.

## Usage Examples
After running the script, you will be prompted to enter:
- **WBC1:** The initial white blood cell count.
- **WBC2:** The white blood cell count after processing.
- **Volume without CPD (V2):** Blood volume without CPD.
- **Volume with CPD (V_CPD):** Blood volume with CPD.

### Sample Interaction:
Enter the value of WBC1 (or 'q' to quit): 5000 <br>
Enter the value of WBC2: 4500 <br>
Enter the blood volume without CPD: 100 <br>
Enter the blood volume with CPD: 150

### Sample Output:

| WBC1  |  WBC2  | Volume without CPD | Volume with CPD | Recovery (%) | Type of Recovery               |
|-------|--------|--------------------|-----------------|--------------|--------------------------------|
| 5000  | 4500   | 100                | 150             | 37.8         | Recovery without division (%)  |


## Project Status
The project is currently in the initial version and functional. Future updates may include a graphical user interface (GUI) and additional data validation features.

## Sources
This tool was developed based on standard practices for evaluating cell recovery in laboratory settings.


