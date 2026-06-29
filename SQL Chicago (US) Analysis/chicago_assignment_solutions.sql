-- ============================================================
-- File: chicago_assignment_solutions.sql
-- Project: Chicago Crime & Socioeconomic Analysis
-- Description: SQL queries solving 10 assignment problems across crime, schools, and socioeconomic data.
-- ============================================================

# Problems - Solutions

# Now write and execute SQL queries to solve assignment problems

# Problem 1 - Find the total number of crimes recorded in the CRIME table.
SELECT COUNT(*) FROM chicago_crime;

# Problem 2 - Retrieve first 10 rows from the CRIME table.
SELECT * FROM chicago_crime 
LIMIT 10;

# Problem 3 - How many crimes involve an arrest?
SELECT COUNT(ID) AS number_of_crimes
FROM chicago_crime
WHERE ARREST = "True";

# Problem 4 - Which unique types of crimes have been recorded at GAS STATION locations?
SELECT DISTINCT PRIMARY_TYPE FROM chicago_crime
WHERE LOCATION_DESCRIPTION = "GAS STATION";

# Problem 5 - In the CENUS_DATA table list all Community Areas whose names start with the letter "B".
SELECT COMMUNITY_AREA_NAME FROM chicago_socioeconomic_data
WHERE COMMUNITY_AREA_NAME LIKE "B%";

# Problem 6 - Which schools in Community Areas 10 to 15 are healthy school certified?
SELECT School_ID, NAME_OF_SCHOOL FROM chicago_public_schools
WHERE COMMUNITY_AREA_NUMBER BETWEEN 5 AND 10 
AND HEALTHY_SCHOOL_CERTIFIED = "Yes";

# Problem 7 - What is the average school Safety Score?
SELECT ROUND(AVG(SAFETY_SCORE), 3) FROM chicago_public_schools;

# Problem 8 - List the top 5 Community Areas by average College Enrollment [number of students]
SELECT COMMUNITY_AREA_NAME, COUNT(School_ID), ROUND(AVG(COLLEGE_ENROLLMENT), 3) AS avg_college_enrollment
FROM chicago_public_schools
GROUP BY COMMUNITY_AREA_NAME
ORDER BY avg_college_enrollment DESC
LIMIT 5;

# Problem 9 - Use a sub-query to determine which Community Area has the least value for school Safety Score?
SELECT COMMUNITY_AREA_NAME FROM chicago_public_schools
WHERE SAFETY_SCORE = (SELECT MIN(SAFETY_SCORE) FROM chicago_public_schools);

# Problem 10 - [Without using an explicit JOIN operator] Find the Per Capita Income of the Community Area which has a school Safety Score of 1.
SELECT CSD.COMMUNITY_AREA_NAME, CSD.PER_CAPITA_INCOME, CPS.SAFETY_SCORE
FROM chicago_socioeconomic_data CSD, chicago_public_schools CPS
WHERE CSD.COMMUNITY_AREA_NUMBER = CPS.COMMUNITY_AREA_NUMBER
AND CPS.SAFETY_SCORE = 1;
