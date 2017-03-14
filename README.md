---
output:
  html_document: default
  pdf_document: default
---
# College Score Card Ranking 
## **Introduction**
#### College Score Card Ranking is a College-Recommendation Program by Python

![](picture/college rank.jpg)

## Our Mission 

####  Nowadays, getting into an ideal college is an important step for students to receive better education as well as their future career development. However, choosing an appropriate college can be challenging. Our research purpose is to assist students to find their ideal colleges by providing 5 top college information with basic information
####  Students with different backgrounds have different needs and concerns about college requirements. We categorize three major groups of prospective students: International, local and transfer students, and we will evaluate different factors based on each group?s needs.

## Summary Of Research Questions:
- How should we come out with different solutions that can help different types of students (Ex: internaxtional students, local students, transfer students) to find the colleges that suit them most by applying the dataset?
- How can the different factors (like academic rank, tuition fee) be used together within different influence score to come out a total rank of a school?
- We can also predict a college’s future acceptance rate to predict collecting the previous year’s data (from 1996 - 2014) and find functions to describe the relationships between those data. Is there any way to analyze the trend of acceptance rate of a college so that the students have a better idea of which colleges to go?


## Dataset
> We collected our dataset from **_data.gov_**

[Dataset Download Here](https://catalog.data.gov/dataset/college-scorecard/resource/b8f3d10b-0974-40db-b5fa-3c87ecae516b)
 
## Methodology

#### **User Inputs**
> We designed our input panel into two parts: **Recommendation Panel** & **Acceptance Rate Panel** 


#### 1. College Recommendation Panel

> a. Describe your student status: International/Local/Transfer?
- This is a text response, the users will enter their status by
typing a ?string? response 
b. Enter your SAT Score:
- This is a Numerical response, the users are required to type in SAT score they?ve taken
c. Enter your expected Maximum Tuition(per quarter)?
- This is a Numerical response, the users are required to type in
the Maximum tuition per quarter they expect to pay

#### **Influence Score**
> Influence score is the **key** for our recommendation-program. 

#### influence score for each filtered college information will be calculated based on different factors of interest, and the calculation is different for International, local and transfer students.

##### Groups of interest: (*Note: influence score for each college is a single value. It starts from 0; it evaluates and sums up the weight of each factor)


#### Methodology:

a.	International Students:
-   	Tuition: 15% 
-   	SAT: 40%
-   	Ranking: 20%
-   	Acceptance Rate: 35%

b.	Local Students:
-   	Tuition: 20%
-   	Debt: 10%
-   	Gender Ratio: 10%
-   	SAT: 25%
-   	Acceptance Rate: 35%

c.	Transfer Students:
-   	Acceptance Rate: 40%
-   	Tuition: 30%
-   	SAT: 10%
-   	Ranking: 20%


- Sum up the influence score for each college by adding up each factor?s weight
- Select the top 5 influence scores and present the users with the corresponding college information: name, location, tuition, ranking, SAT average, acceptance rate, gender ratio.
- Provide the top college suggestion?s acceptance rate trending from 1996 - 2014, and see if the trend is going up or down.





#### Project Challenges
 Let's take a glance of our original data:

![](picture/dataset.PNG)

Since the data are extracted directly from the system, we can see the column names are unorganized, and there are a large amount of  **_NULL_**s, which made us hard to filter and re-organize the dataset


#### Panel Instruction 

Please View Instruction - [Here](https://youtu.be/S1rcbpwc8S0)


#### Results Present

- College Recommendation

- College Acceptance Rate Trend (2004 - 2013)

> Recommend College OR Check Accept Rate? Enter R or A or Exit: A

> Enter a University Name(Full Name):Cornell University

![](cornell.PNG)

