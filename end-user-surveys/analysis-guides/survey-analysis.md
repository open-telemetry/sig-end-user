# OpenTelemetry Survey Data Analysis Tutorial
***A step-by-step walkthrough for analyzing survey data across SIGs in the OTel community.*** 

***Author: Ernest Owojori***: ***Page 3 of 3***

## Data Preparations
Survey data often contains missing values, duplicates, or inconsistent category names, especially when questions allow open text or multiple responses. Start by getting a clear overview of what you’re working with.

**Cleaning 1: Frequency & Percentage Check**

Before editing anything, use Pivot Tables to generate frequency and percentage tables for each variable.
This helps you quickly spot:

 - Unfinished responses and missing values (blank cells)
 - Inconsistent categories (e.g., “AWS Fargate” vs “aws fargate”)
 - Outliers or unexpected entries

***Why this matters: This simple step often surfaces most data issues early and informs how you’ll clean each variable***.

Note: 

 - Using pivot tables to get frequencies and percentages should not be used for multiple response variables and open-ended variables.
 - Some blank cells can be due to the conditional formatting of the form.

**Steps to using pivot tables:** 

https://github.com/user-attachments/assets/ce119f86-07db-4946-8efc-d6c78a293548

https://github.com/user-attachments/assets/774df128-c6b9-46f1-b763-8d04b40fb4c4

**Cleaning 2: Standardize Responses**

 - Category Names: Use consistent capitalization and naming (e.g., “AWS Fargate” everywhere).
 - Remove Duplicates: Check for duplicate rows, especially when respondents accidentally submit multiple times.

## Data Transformation
Once the data is clean, structure it for analysis. This involves creating unique identifiers and transforming variables for easier manipulation.

**Step 1: Create a Respondent ID**

Insert a new column named **respondent_id** and number each row sequentially from 1 to n.
This ID will become the key for linking transformed data back to the original sheet.

**Step 2: Single-Select Variables**

Keep single-select categorical variables in their raw form initially.
You’ll transform them later, only when needed for specific statistical tests or advanced analysis.

**Step 3: Multiple-Select Variables**
For questions where respondents can select multiple answers:
 - ≤ 10 options:
    - Convert each option into a dummy variable (0/1) using `IF(ISERR(SEARCH(I$1,$H2)),0,1)`.
![69D61F99-06A9-4EB5-B7B0-76EF895EC32D_1_105_c](https://github.com/user-attachments/assets/653bbb97-8d39-4c09-a880-4a8633cff97c)  
    
    - Each option becomes its own column (e.g., deployment_k8s, deployment_vm, etc.).
      
 - Greater than 10 options:
    - To keep your sheet manageable, create a separate sheet for that question.
    - Use the respondent_id to link it back when needed (e.g., through `VLOOKUP`)
    - And this time, the only change in the formula is checking the matching case in the main data sheet, i.e., $O2 as shown in the screenshot, will be found in the data!$O2

**Aggregation Tip:**

 - For multi-select questions: use `SUM()` across the dummy columns to get counts per option.
 - For single-select questions: in one of your Pivot Table sheets, get the counts (using `COUNTA`) and percentages.

## Data Validation
Before starting analysis, and as you run functions, it’s important to randomly validate that the outputs you have are accurate. This can be done by:

 - The number of rows or respondents matches the original after transformation.
 - As you perform multiple response transformations, compare the sum of the new columns with the Google Forms summary.

## Exploratory Data Analysis (EDA)
Once your data is cleaned and structured, the next step is to explore it systematically.
EDA helps you understand distributions, spot patterns, and identify areas that warrant further analysis. In this tutorial, we’ll focus on using Google Sheets PivotTables and Charts, as these are the primary tools most SIGs use.

### Descriptive Statistics
The foundation of survey analysis is understanding how respondents answered each question.
In this stage, your goal is to summarize each variable and generate basic group comparisons.

**Step 1: Generate Frequencies and Percentages**
For each categorical or binary variable:

1. Go to Insert → Pivot Table.
2. Set the Rows to the variable you want to summarize.
3. Set Values to `COUNTA` (or `SUM` for dummy variables) to get frequencies.
4. Add the same variable again to Values, set to “% of Column Total” to get percentages.
5. Sort by descending frequency for clarity.
https://github.com/user-attachments/assets/ce119f86-07db-4946-8efc-d6c78a293548

https://github.com/user-attachments/assets/774df128-c6b9-46f1-b763-8d04b40fb4c4

**Step 2: Group Summaries**

To explore patterns across groups (e.g., region, organization size, number of collectors, etc):

**Case 1**: Crossing 2 single select variables, e.g. organization size x OTel in production.

https://github.com/user-attachments/assets/c33220b3-85af-4ecc-ba24-64c02d569208

https://github.com/user-attachments/assets/954743e1-16cb-4e47-b5cb-c2c9665ff1ec

https://github.com/user-attachments/assets/bb351316-8ebc-4cac-975c-4412c7563edc

**Case 2**: crossing a single select with a multiple response variable, e.g., team type x collector deployment location.

![4369B9A1-D196-4A42-83B5-3C9A43388BBD_1_105_c](https://github.com/user-attachments/assets/9cf6692f-dc7c-4ef7-a44f-04278ea9856f)

https://github.com/user-attachments/assets/8bee9dbc-3e0c-4fd9-9d93-97a40af368cc

**Tips for Groups Summaries:** 

 - Some categories with a sample size of less than 10% of the total number of respondents in the survey can be dropped. 
    - For example, Architecture (2), DevRel (1), Operations (1), Product (1) above cannot be used to make a decision. Therefore, dropping them is better.
    - Order the categories: if there is a clear order like team size (1-49 < 50-99 < 100-999 < 1000+), use this order. But for the case of team type, stick to one desired order across all parts of the analysis.
- Calculate the percentage across each category to make a fair decision.
- For interpretation of insights:
    - If the sample is less than 10% of N, don’t decide on it.
    - If the sample is within 10% - 24% of N, decide carefully.
    - If the sample is 25% or above of N, a decision can be made.

## Data Visualization

Charts make patterns clearer and are essential for communicating your findings to the community.

**Step 1: Basic Charts**
Use the Pivot Table outputs as your data source:

 - Bar Charts → Best for categorical variables (e.g., deployment environments, regions).
 - Pie Charts (or their doughnut chart variant) → Use sparingly, only for variables with 2 categories.

**How to Create:**
1. Highlight the Pivot Table result (excluding totals).
2. Click Insert → Chart.
3. Choose the chart type (e.g., “Column chart” or “Bar chart”).
4. Adjust titles, labels, and legends for clarity.


https://github.com/user-attachments/assets/63bb79aa-9389-4d06-8e3b-f3f92767101b

https://github.com/user-attachments/assets/cc034042-2f42-4e87-b916-3cb26a5e9321

https://github.com/user-attachments/assets/9ebbf38d-5e39-4988-ae46-e54c99a9bd0b


 **Tips:**

 - Any category that has less than 5% should not be presented in the graph
 - Avoid having multiple illustrations saying the same thing on the graph, e.g., having an axis of percentage when the bars are already showing labels

 **Step 2: Side-by-Side Comparisons**
 Use a Pivot Table with multiple columns, as created in Group summaries.

 - Highlight the data and select “Stacked column chart” or “Grouped column chart.”
 - Grouped column charts are especially effective for side-by-side categorical comparisons.
 - Use consistent colors and formatting across charts to keep visuals cohesive.

## Combining Multiple Data Sets

When surveys are conducted yearly or periodically, comparing results across years can reveal important trends — such as changes in adoption, satisfaction, or priorities. However, combining survey datasets requires careful attention to consistency and structure.
 - Consistent Question Wording
 - Similar response options
 - Compatible data/variable formats
 - Ensure the surveys target the same respondent population



https://github.com/user-attachments/assets/816e4c7f-97f9-4aab-b582-30ac9c9141c2
