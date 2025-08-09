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
This project analyzes the relationship between advertising budgets across three channnels (TV, Radio and Newspaper) and their impact on sales. The major aim is to uncover insights through which advertising channels drive sales, identify the trends and provide recommendations for optimizing advertising budgets.

### Data Sources
The primary data source is "Advertising Budget and Sales.csv" file, containing 200 records with the following columns:

- TV Ad Budget ($): Advertising budget spent on TV.
- Radio Ad Budget ($): Advertising budget spent on Radio.
- Newspaper Ad Budget ($): Advertising budget spent on Newspaper.
- Sales ($): The sales made from the adveritisment.
  
### Questions
1. What is the combined effect of TV and Radio advertising on sales when Newspaper spending is minimal (e.g. < 10)?

2. Are there specific combinations of advertising budgets that consistently lead to high sales (e.g. Sales > 20)?

### Tools
- Excel (Data cleaning)
- pgSQL (Data sorting)
- Python (Panda - Data Aggregation)
- Power BI (Data Visualization)

### Data Cleaning and Preparation
In the initial data preparation phase, the following tasks were performed as listed below:

1. Checked for missing or null values
2. Ensured the numerical columns (e.g., TV Ad Budget, Radio Ad Budget, Newspaper Ad Budget and Sales) were kept as float for accurate computations
3. Checked for outliers using z-scores
   - TV Ad Budget ($): No extreme outliers
   - Radio Ad Budget ($): No extreme outliers
   - Newspaper Ad Budget ($): One outlier (144)
   - Sales ($): No extreme outliers  


### Data Extraction and Querying
The dataset is quereied using pgSQL:


### Exploratory Data Analysis

### Results and Findings

### Recommendations


### Limitations

### References
