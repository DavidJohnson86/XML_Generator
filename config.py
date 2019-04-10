squibs = [
    {'Name': "FL1_Driver_Stage_1_Airbag", 'Switch': 'FABD1_SQ1', 'DID': '2300,2364'},
    {'Name': "FL2_Driver_Stage_2_Airbag", 'Switch': 'SQ2', 'DID': '2315,2379'},
    {'Name': "FL3_Passenger_Stage_1_Airbag", 'Switch': 'FABP1_SQ3', 'DID': '2302'},
    {'Name': "FL4_Passenger_Stage_2_Airbag", 'Switch' : 'SQ4', 'DID':'2304'}]
    # "FL5_Driver_Shoulder_Belt_Pretensioner",
    # "FL6_Passenger_Shoulder_Belt_Pretensioner",
    # "FL7_Front_Side_Airbag_Left",
    # "FL8_Front_Side_Airbag_Right",
    # "FL9_Rear_Belt_Pretensioner_Left",
    # "FL10_Rear_Belt_Pretensioner_Right",
    # "FL11_Door_Mounted_IC_Left_Front",
    # "FL12_Door_Mounted_IC_Right_Front",
    # "FL13_Door_Mounted_IC_Left_Rear",
    # "FL14_Door_Mounted_IC_Right_Rear",
    # "FL16_Pyro_Cut_off_switch_STD",
    # "FL17_Pyro_Cut_off_switch_High_voltage",

VOLTAGE_TAG = "PS1.VoltageV"
NOMINAL_VOLTAGE = "13.8"

# REPORT NAME
REPORT_NAME_TAG = "ReportName"
REPORT_NAME = "_SQ_Faults"

# SWITCHING
SWITCHING = "PhysicalFaultState"

# SIGNAL MONITORING
SIGNAL_MONITOR_TAG = "CANSIG_Monitor"
SIGNAL_MONITOR = "AB_Lampe,AB_Systemfehler,AB_KD_Fehler"

# READ DID
READ_DID_TAG = "UDS.ReadDataByID.List"

# CRASH LIST
CRASH_LIST_TAG = "CrashList"
CRASH_LIST = "Crash_ALL, Crash_Rear_2"

# ESP V REF VAL
ESP_V_REF_VAL_TAG = "ESP_v_ref.val type=HEX"
ESP_V_REF_VAL = "0xF0"

#DIAG
DIAG_SERVICE_TAG = ""
DIAG_SERVICE = ""

