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

1. Checked for missing or null values:No missing value was found.
2. Ensured numeric consistency by handling inconsistent data:  Columns containing floats were rounded to the best decimal poimt for accurate computations.
3. Checked for duplicates:
4. Checked for outliers: 
5. Rearranged arrangement of columns: placed id as the first column in the dataset

The dataset was filtered using SQL to filter out the ids from 0 to 200 with their respective chemical properties for analysis/manipulation. The new csv file is titled "wineQT_filtered.csv".

### Data Extraction and Querying
The dataset is imported into pgSQL after cleaning on Excel for querying and filtering. It is then filtered using SQL to filter out the ids from 0 to 300 with their respective chemical properties for analysis/manipulation. The new csv file is titled "wineQT_filtered.csv". The attributes needed are fixed acidity, volatility acidity, citric acid, density, pH, sulphates, alcohol and quality.

1. Pearson correlation is used to examine the relationship between the quality and the chemical properties. Python (Pandas lib.) is used to find the correlati

### Exploratory Data Analysis

### Results and Findings

### Recommendations


### Limitations

### References
This dataset is pubicly available on Kaggle and UCI machine learning repository, https://archive.ics.uci.edu/ml/datasets/wine+quality
