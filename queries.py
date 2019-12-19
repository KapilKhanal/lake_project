
drop_lakes_table = "DROP TABLE IF EXISTS lakes"

create_lakes_table = (""" 
CREATE TABLE lakes(
PROJECT_ID  INTEGER PRIMARY KEY,
DATA_SET_TITLE  VARCHAR(100),
LAKE_NAME  VARCHAR(100),
CITY  VARCHAR(100),
COUNTY  VARCHAR(100),
DNR_ID_Site_Number  VARCHAR(100),
MAJOR_WATERSHED  VARCHAR(100),
WATER_PLANNING_AUTHORITY  VARCHAR(100),
LAKE_SITE_NUMBER  VARCHAR(100),
START_DATE  VARCHAR(100),
START_HOURMIN24  VARCHAR(100),
END_DATE  VARCHAR(100),
END_HOURMIN24  VARCHAR(100),
SAMPLE_DEPTH_IN_METERS  INTEGER,
Seasonal_Lake_Grade_RESULT  VARCHAR(100),
Seasonal_Lake_Grade_QUALIFIER  VARCHAR(100),
Seasonal_Lake_Grade_Units  VARCHAR(100),
Physical_Condition_RESULT  VARCHAR(100),
Physical_Condition_QUALIFIER  VARCHAR(100),
Physical_Condition_Units  VARCHAR(100),
Recreational_Suitability_RESULT  VARCHAR(100),
Recreational_Suitability_QUALIFIER  VARCHAR(100),
Recreational_Suitability_Units  VARCHAR(100),
Secchi_Depth_RESULT_SIGN  VARCHAR(100),
Secchi_Depth_RESULT  VARCHAR(100),
Secchi_Depth_QUALIFIER  VARCHAR(100),
Secchi_Depth_Units  VARCHAR(100),
Total_Phosphorus_RESULT_SIGN  VARCHAR(100),
Total_Phosphorus_RESULT  VARCHAR(100),
Total_Phosphorus_QUALIFIER  VARCHAR(100),
Total_Phosphorus_Units  VARCHAR(100),
longitude  VARCHAR(100),
latitude  VARCHAR(100)
)
""")


lake_insert_query =  """INSERT INTO lakes (PROJECT_ID, DATA_SET_TITLE, LAKE_NAME, CITY, COUNTY,
    DNR_ID_Site_Number, MAJOR_WATERSHED, WATER_PLANNING_AUTHORITY, LAKE_SITE_NUMBER,
    START_DATE, START_HOURMIN24, END_DATE, END_HOURMIN24, SAMPLE_DEPTH_IN_METERS, 
    Seasonal_Lake_Grade_RESULT, Seasonal_Lake_Grade_QUALIFIER, Seasonal_Lake_Grade_Units,
    Physical_Condition_RESULT, Physical_Condition_QUALIFIER, Physical_Condition_Units, 
    Recreational_Suitability_RESULT, Recreational_Suitability_QUALIFIER, Recreational_Suitability_Units, 
    Secchi_Depth_RESULT_SIGN, Secchi_Depth_RESULT, Secchi_Depth_QUALIFIER, Secchi_Depth_Units, 
    Total_Phosphorus_RESULT_SIGN, Total_Phosphorus_RESULT, Total_Phosphorus_QUALIFIER, 
    Total_Phosphorus_Units, longitude, latitude)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    














