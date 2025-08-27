# Wine Quality
The provided dataset is analyzed to uncover actionable insights into factors influencing wine quality. The dataset is related to red variants of the Portuguese "Vinho Verde" wine.

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
This project analyzes the Wine Quality datasets to uncover actionable insights into factors influencing wine quality, with focus on physiochemical properties such as alcohol, acidity and sulphates. The major objective is to provide data-driven recommendations for wine producers to optimize quality, enhance production processes and inform marketing strategies.

### Data Sources
The primary dataset is sourced from the provided "WineQT.csv" file, derived from the UCI Wine Quality dataset. It includes 1143 records with the following columns:

- id: Sequential identifier
- fixed acidity: Tartaric acid (g/dm³)
- volatile acidity: Acetic acid (g/dm³)
- citric acid: Citric acid
- residual sugar: Sugar post-fermentation (g/dm³)
- chlorides: Sodium chloride (g/dm³)
- free sulfur dioxide: Free SO₂ (mg/dm³)
- total sulfur dioxide: Total SO₂ (mg/dm³)
- density: Density SO₂ (g/cm³)
- pH: Acidity level (0-14 scale)
- sulphates: Potassium sulphate (mg/dm³)
- alcohol: Alcohol content (% by volume)
- quality; Expert-rated score (3-8)

### Questions
1. Which chemical properties in the wine have the strongest impact on quality ratings and how can these guide adjustments in the production process?
   
2. What are the typical chemical profiles (e.g. alcohol, volatile acidity) of high-quality wines (score 7 or above) compared to standard wines (score 5-6), and how can these inform production targets?

3. Are there chemical thresholds that consistently define premium wines and how can these be applied to improve quality?

4. How is the quality of wines distributed in our dataset, and what does this mean for inventory management and marketing strategies?

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
This dataset is pubicly available on Kaggle and UCI machine learning repository, https://archive.ics.uci.edu/ml/datasets/wine+quality
