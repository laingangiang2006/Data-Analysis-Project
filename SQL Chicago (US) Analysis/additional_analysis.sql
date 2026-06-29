-- ============================================================
-- File: additional_analysis.sql
-- Project: Chicago Crime & Socioeconomic Analysis
-- Description: Self-directed analysis beyond course assignments
-- ============================================================

# Top 5 Most Common Crime Types
SELECT PRIMARY_TYPE, COUNT(ID) AS Case_Count
FROM chicago_crime
GROUP BY PRIMARY_TYPE
ORDER BY Case_Count DESC
LIMIT 5;

# Most Arrested Crime Categories
SELECT PRIMARY_TYPE, COUNT(ARREST) AS Arrest_Count
FROM chicago_crime
WHERE ARREST = "TRUE"
GROUP BY PRIMARY_TYPE
ORDER BY Arrest_Count DESC
LIMIT 5;

# Total Non-Arrest Count by Primary Type
SELECT SUM(Not_Arrest_Count) AS Total_Not_Arrests FROM (
    SELECT COUNT(ARREST) AS Not_Arrest_Count
    FROM chicago_crime
    WHERE ARREST = "FALSE"
    GROUP BY PRIMARY_TYPE
    ORDER BY Not_Arrest_Count DESC) AS Subquery;

# Top 5 Community Areas by Case Volume
SELECT COMMUNITY_AREA_NUMBER, COUNT(ID) AS Case_Count
FROM chicago_crime
WHERE COMMUNITY_AREA_NUMBER != ""
GROUP BY COMMUNITY_AREA_NUMBER
ORDER BY Case_Count DESC
LIMIT 5;

# Top 5 Districts by Case Volume
SELECT DISTRICT, COUNT(ID) AS Case_Count
FROM chicago_crime
GROUP BY DISTRICT
ORDER BY Case_Count DESC
LIMIT 5;

# Top 5 Years by Case Volume
SELECT YEAR, COUNT(ID) AS Case_Count
FROM chicago_crime
GROUP BY YEAR
ORDER BY Case_Count DESC
LIMIT 5;
