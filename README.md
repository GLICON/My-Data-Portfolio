# Advertising Budget and Sales
This project analyzes the relationship between advertising budgets across three channnels (TV, Radio and Newspaper) and their impact on sales.

## Table of Contents

- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Questions](#questions)
- [Tools](#tools)
- [Data Cleaning and Preparation](#data-cleaning-and-preparation)
- [Data Extraction and Querying](#data-extraction-and-querying)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Results and Findings](#results-and-findings)
- [Recomendations](#recommendations)
- [Limitations](#limitations)
- [References](#references)

### Project Overview
This project analyzes the relationship between advertising budgets across three channnels (TV, Radio and Newspaper) and their impact on sales. The major aim is to uncover insights into advertising effectiveness, optimal budget allocation and high-performing combinations.

### Data Sources
The primary data source is "Advertising Budget and Sales.csv" file, containing 200 records with the following columns:

- TV Ad Budget ($): Advertising budget spent on TV.
- Radio Ad Budget ($): Advertising budget spent on Radio.
- Newspaper Ad Budget ($): Advertising budget spent on Newspaper.
- Sales ($): The sales made from the adveritisment.

  
### Questions
1. How does the TV advertising vary across different budget ranges (e.g. Low, Medium or High)?
   
2. What is the combined effect of TV and Radio advertising on sales when Newspaper spending is minimal (e.g. < 10)?
  
3. Are there specific combinations of advertising budgets that consistently lead to high sales (e.g. Sales > 20)?

### Tools
- Excel (Data cleaning)
- pgSQL (Data querying)
- Python (Panda - Statistical analysis and Data Aggregation)
- Power BI (Data Visualization)

### Data Cleaning and Preparation
In the initial data preparation phase, the following tasks were performed as listed below:

1. Checked for missing or null values
2. Ensured the numerical columns (e.g., TV Ad Budget, Radio Ad Budget, Newspaper Ad Budget and Sales) were kept as float for accurate computations
3. Checked for outliers using z-scores:
   - TV Ad Budget ($): No extreme outliers
   - Radio Ad Budget ($): No extreme outliers
   - Newspaper Ad Budget ($): One outlier (144)
   - Sales ($): No extreme outliers
All outliers are demmed plausible.

### Data Extraction and Querying
The dataset is imported into pgSQL after the following query:

<img width="487" height="138" alt="Screenshot 2025-08-09 at 12 33 24" src="https://github.com/user-attachments/assets/1ee6323b-709e-4a26-8ec3-424fd13c96d8" />

The dataset is queried using pgSQL:
Q1: TV Budget Ranges (Low: <100, Medium: 100-200, High < 200)
<img width="512" height="354" alt="Screenshot 2025-08-19 at 12 54 04" src="https://github.com/user-attachments/assets/e94d3b8a-1223-4acf-a1db-ebe6462a829d" />

Q2: TV and Radio Advertisement Effect (Newspaper ad budget < 10)
<img width="410" height="93" alt="Screenshot 2025-08-19 at 13 05 39" src="https://github.com/user-attachments/assets/c8d25c65-1b58-4e62-8bb0-05d8e5dbebf4" />

Q3: Budget Combinations (Sales > 20)


Exploratory Data Analysis








### Exploratory Data Analysis

### Results and Findings

### Recommendations


### Limitations

### References
