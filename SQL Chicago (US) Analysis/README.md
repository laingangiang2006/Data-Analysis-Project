# Chicago (USA) Analysis

The core questions needed to be answer in this project are:

> What are the most common crime types and which ones lead to the most arrests in Chicago?

> Which community areas and districts are the most crime-concentrated?

> How does school safety and college enrollment vary across Chicago's community areas?

> Is there a relationship between a community area's school safety score and its per capita income?

---

## Dataset Overview

A Chicago SQL analysis datasets, including crime reports, public school performance, and socioeconomic indicators, which explores crime patterns, school safety and enrollment, and the relationship between neighborhood income and community outcomes.

These dump datasets are provided in the course ["SQL: A Practical Introduction for Querying Databases"](https://www.coursera.org/learn/sql-practical-introduction-for-querying-databases) by IBM on Coursera.

---

## Repository Structure

| File | Description |
|------|--------------|
| [README.md](https://github.com/laingangiang2006/Data-Analysis-Project/blob/main/SQL%20Chicago%20(US)%20Analysis/README.md) | Project documentation |
| [Final Project Description](https://github.com/laingangiang2006/Data-Analysis-Project/blob/main/SQL%20Chicago%20(US)%20Analysis/Final%20Project%20-%20Using%20SQL%20in%20MYSQL%20with%20phpMyAdmin.pdf) | Final project description file, including some instructions, problems, ... |
| [Dump Datasets](https://github.com/laingangiang2006/Data-Analysis-Project/tree/main/SQL%20Chicago%20(US)%20Analysis/Dataset) | Dump datasets taken from the course |
| [chicago_assignment_solutions.sql](https://github.com/laingangiang2006/Data-Analysis-Project/blob/main/SQL%20Chicago%20(US)%20Analysis/additional_analysis.sql) | SQL queries solving 10 problems assigned in the project's final project |
| [additional_analysis.sql](https://github.com/laingangiang2006/Data-Analysis-Project/blob/main/SQL%20Chicago%20(US)%20Analysis/chicago_assignment_solutions.sql) | My additional analysis alongside the problems assigned in the assignment |

---

## Tools & Languages

| Tool/Language | Purpose |
|------|---------|
| **SQL, MySQL** | Relational database queries |

---

# Key Findings

## Crime Overview
- There are 533 crimes recorded in the CRIME table.
- The top 5 most common crime types are theft (106), battery (92), criminal damage (58), narcotics (54), and other offense (32).
- The years with the highest crime volume are 2005 (44), 2009 (43), 2003 (42), 2002 (37), and 2007 (36), suggesting crime peaked in the mid-2000s.

## Arrests & Non-Arrests
- There are 163 crimes involving an arrest, of which narcotics, battery, criminal trespass, theft, and assault are the most arrested crime categories.
- Out of 533 total crimes, 370 did not result in an arrest, meaning only about 30% of crimes led to an arrest.
- There are 4 unique types of crimes have been recorded at gas station locations, including theft, narcotics, robbery, criminal trespass.

## Geographic Distribution
- The top 5 community areas by case volume are areas 25 (43 cases), 23 (22), 68 (21), 28 (16), and 29 (16), indicating that crime is heavily concentrated in a few specific neighborhoods.
- District 11 recorded the highest number of cases (48), followed by districts 8 (44), 7 (38), 4 (33), and 12 (32).
- There are 5 community areas whose names start with the letter "B": Belmont Cragin, Burnside, Brighton Park, Bridgeport, and Beverly.

## Education & Schools
- The average school safety score across Chicago public schools is 49.505.
- Washington Park has the lowest school safety score among all community areas.
- 3 schools in community areas 5 to 10 are healthy school certified: Abraham Lincoln Elementary School, Hawthorne Elementary Scholastic Academy, and Rufus M Hitch Elementary School.
- The top 5 community areas by average college enrollment are Archer Heights (2411.5), Montclare (1317.0), Belmont Cragin (1233.556), West Elsdon (1233.333), and North Center (1223.5).

## Socioeconomic Insights
- Washington Park, which has a school safety score of 1, also has a per capita income of only $13,785, suggesting a strong link between low school safety and economic hardship.

---

## License

This project is for educational purposes. 

Dataset credit: From the course, called ["SQL: A Practical Introduction for Querying Databases"](https://www.coursera.org/learn/sql-practical-introduction-for-querying-databases), provided by IBM on Coursera.
