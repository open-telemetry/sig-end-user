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

 - Insert pivot_table_1
 - Insert pivot_table_2 

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
    - Convert each option into a dummy variable (0/1) using IF(ISERR(SEARCH(I$1,$H2)),0,1).
    - insert an image here
    - Each option becomes its own column (e.g., deployment_k8s, deployment_vm, etc.).
 - > 10 options:
    - To keep your sheet manageable, create a separate sheet for that question.
    - Use the respondent_id to link it back when needed (e.g., through VLOOKUP)
    - And this time, the only change in the formula is checking the matching case in the main data sheet, i.e, $O2 as shown in the screenshot, will be found in the data!$O2

**Aggregation Tip:**

 - For multi-select questions: use SUM() across the dummy columns to get counts per option.
 - For single-select questions: in one of your Pivot Table sheets, get the counts and percentages.

## Data Validation
Before starting analysis, and as you run functions, it’s important to randomly validate that the outputs you have are accurate. This can be done by:

 - The number of rows or respondents matches the original after transformation
 - As you perform multiple response transformations, compare the sum of the new columns with the Google Forms summary.
  - Insert a validation video?

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
3. Set Values to “COUNTA” (or SUM for dummy variables) to get frequencies.
4. Add the same variable again to Values, set to “% of  Column Total” to get percentages.
5. Sort by descending frequency for clarity.
 - Reference initial video on freq

**Step 2: Group Summaries**

To explore patterns across groups (e.g., region, organization size, number of collectors, etc):

**Case 1**: Crossing 2 single select variables, e.g organization size x otel in production
 - Insert cross-tabs-1
 - Insert cross_tabs_2
 - Insert cross-tabs_3

**Case 2**: crossing a single select with a multiple response variable, e.g, team type x collector deployment location

 - insert image
 - Insert cross-tabs-4

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
 - Insert viz_01
 - Insert viz_02
 - Insert viz_03

 **Tips:**

 - Any category that has less than 5% should not be presented in the graph
 - Avoid having multiple illustrations saying the same thing on the graph, e.g, having an axis of percentage when the bars are already showing labels

 **Step 2: Side-by-Side Comparisons**
 Use a Pivot Table with multiple columns, as created in Group summaries.

 - Highlight the data and select “Stacked column chart” or “Grouped column chart.”
 - Grouped column charts are especially effective for side-by-side categorical comparisons.
 - Use consistent colors and formatting across charts to keep visuals cohesive.

## Combining multiple data sets

When surveys are conducted yearly or periodically, comparing results across years can reveal important trends — such as changes in adoption, satisfaction, or priorities. However, combining survey datasets requires careful attention to consistency and structure.
 - Consistent Question Wording
 - Similar response options
 - Compatible data/variable formats
 - Ensure the surveys target the same respondent population

 - Insert comparison_01















 


