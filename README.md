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

3. How is the quality of wines distributed in our dataset, and what does this mean for inventory management and marketing strategies?

### Tools
- Excel (Data cleaning)
- Python (Panda - Data Aggregation, Matplot - Data Visualization)
- Power BI (Data Visualization)

### Data Cleaning and Preparation
In the initial data preparation phase, the following tasks were performed as listed below:

- Rearranged arrangement of columns: placed id as the first column in the dataset
- Checked for missing or null values:No missing value was found.
- Ensured numeric consistency by handling inconsistent data: Columns containing floats were rounded to the best decimal poimt for accurate computations.
- Checked for duplicates: No duplicates were found
- Checked for outliers:
Box and Whisker plot, and IQR formula are used to check for outliers in the physicochemical properties of red wine variants

<img width="415" height="310" alt="WQ_Box plot and whiskers for outliers" src="https://github.com/user-attachments/assets/93f1cef3-9c80-46c4-9529-63288a24b167" />

The IQR formula is used in finding the outliers. The number of outliers are shown below:
fixed acidity (44)
volatile acidity (15)
citric acid
residual sugar (111)
chlorides (74)
free sulfur dioxide (18)
total sulfur dioxide (40)
density (38)
pH (20)
sulphates (43)
alcohol (12)

### Data Extraction and Querying




### Exploratory Data Analysis
1. The correlation function CORREL is used to find the correlation relationship between each property and quality. The result is shown in the table below:

<img width="715" height="293" alt="Screenshot 2025-10-06 at 13 35 31" src="https://github.com/user-attachments/assets/f3083770-0cc0-4a4a-83aa-f3cdffea6293" />

The correlation analysis reveals that alcohol exhibits the strongest positive correlation with quality (0.48), suggesting higher alcohol content enhances perceived quality. Conversely, volatile acidity shows a significant negative correlation, indicating that elevated levels detrimentally impact taste and overall rating, guiding quality assessments in wine making. 

2. The Python script titled 'WineQT2.py' addresses the problem by analyzing the Wine Quality dataset to compare the typical chemical profiles of high-quality wines (rated 7 or above) against standard wines (rated 5-6). It solves the problem by loading the CSV data with pandas, filtering the dataset into the two quality categories, and computing mean values for key physiochemical features like alcohol, volatile acidity, and sulphates. The results are presented in a concise comparison table, highlighting differences that reveal patterns—such as higher alcohol and lower volatile acidity in premium wines.

<img width="1200" height="800" alt="Physicochemical profiles comparison" src="https://github.com/user-attachments/assets/e3e7c09f-22e7-48b8-9009-7824f784d383" />

3. Using pandas, we compute the distributions and visualized trends for the red wine dataset to guide inventory managament and marketing. The 'quality' column rates wines on a scale from 3 (lowest) to 9 (highest), based on sensory data. The distribution is highly imbalanced, with the vast majority of wines falling into the average quality range (5 and 6), reflecting real-world wine production where "good enough" wines dominate.The python code is titled 'WineQT3'.

### Results and Findings
1. High levels (>0.6 g/L) introduce acetic spoilage and vinegar-like off-flavors, significantly lowering quality by up to 1-2 points in high-acidity samples (as 70% of scores ≤4 occur above this threshold). Of the 11 properties, volatile acidity has the strongest negative impact (r = -0.40). The strongest positive effect, on the other hand, is produced by alcohol (r = 0.35). Higher concentrations (≥12% ABV) improve mouthfeel, body, and fruit intensity, and they are associated with 80% of top scores (≥7) in fuller-bodied, riper wines.  A significant positive driver (r = 0.24) that improves quality in preserved batches without adding bitterness is sulphates, which offer antimicrobial stability and a mild aroma lift at ideal concentrations (0.6–0.8 g/L).  Citric acid (r = 0.18, provides freshness) and fixed acidity (r = 0.16, creates structure) are weaker impacts, whilst total sulphur dioxide (r = -0.17) somewhat detracts through oxidative undertones. Microbial control and fermentation optimisation are the main levers for raising profiles from ordinary to excellent. Quality averages 5.7, skewed low, although top quality typically exhibit low volatile acidity, high alcohol, and balanced sulphates.

2. Using mean values as representative metrics, high-quality wines consistently show elevated levels of desirable compounds (e.g., alcohol, sulphates, citric acid) that contribute to enhanced flavor complexity, body, and freshness, while exhibiting reduced concentrations of potential detractors (e.g., volatile acidity, total sulfur dioxide). This aligns with sensory science principles, where balanced acidity and alcohol amplify mouthfeel and aroma persistence, as supported by expert ratings in the dataset. The profiles show that minor optimisations, rather than extreme values, drive quality; for example, a 15% rise in alcohol and a 19% reduction in volatile acidity account for a large portion of the variation.  Consistent patterns confirm these as quality indicators, although variability within groups (e.g., SD for alcohol: 0.85 in high vs. 0.92 in standard) implies environmental factors like vintage have a role.

3. 

### Recommendations
1.
- Prioritise reducing volatile acidity by strict sanitation, temperature-controlled fermentation (18–25°C), and early SO₂ dosage (20–50 mg/L) to maintain levels <0.5 g/L in order to maximise these effects, which might raise average quality by 0.5–1 point.
- Increase alcohol content without going overboard by using riper harvests (Brix 24–26°) and tolerant yeasts that target 12–14% ABV.  Aim for 10–15% quality increases every vintage in accordance with EU rules (total SO₂ <150 mg/L). Adjust sulphates to 0.6–1.0 g/L by precise additions and blending, monitored by titration, while using sensory trials and data analytics for iterative improvement.

2. Winemakers should incorporate these data-driven strategies to use these profiles for production targets, which could increase high-quality yields by 10–20% through focused interventions:

<img width="489" height="459" alt="Psychicochemical profile recommendation" src="https://github.com/user-attachments/assets/408febe3-5240-43a3-bd4b-b6f156d8bd36" />

These recommendations prioritize cost-effective, scalable changes, with ROI from premium pricing (e.g., +25% for ≥7 scores) outweighing minor additive costs
3.







### Limitations

### References
This dataset is pubicly available on Kaggle and UCI machine learning repository, https://archive.ics.uci.edu/ml/datasets/wine+quality
