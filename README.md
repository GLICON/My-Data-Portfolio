# My-Data-Portfolio

### Project Overview

This data analysis aims to provide answers to some questions by evaluating Amazon smartwatches and smartphones actual prices, discounted prices, percentage discounts and ratings.


### Data Sources

Sales Data: The primary dataset used for this analysis is the "amazon.csv" file, containing detailed information about each sale made by the company.

### Tools

- Excel (Data cleaning)
- SQL Server (Data Analysis)
- Excel (Data visualization)

### Data Cleaning/Preparation

In the initial data preparation phase, we performed the following tasks:
1. Data loading and inspection
2. Filtering out of necessary data
3. Handling missing values
4. Data formatting

### Exploratory Data Analysis

EDA involved exploring Amazon smartwristwatches and smartphones to answer key questions, such as:

1.Are Amazon discounts more competitive in the smartwatches or smartphones category?

2.Do smartwatches discounts exhibit more variability than smartphones discounts? Are the distributions of the discounts symmetric or skewed?

3.How does the smartwatches discount percentages vary with the ratings?

4.Is there a correlation (linear relationship) between the discount percentage on smartwatches/smartphones and the actual prices/ratings? If yes, what is the liner relationship?

5.Do higher-priced smartwatches receive larger absolute discounts compared to lower-priced ones or highly rated ones or both?


### Data Analysis

<img width="521" alt="Screenshot 2025-06-04 at 11 24 16" src="https://github.com/user-attachments/assets/8ef7d3ed-ad16-48a6-bf11-2c6969e14068" />
### Results/Findings

1. Amazon offered more competitive discounts on smartwatches, with an average discount of 69.82% compared to 23.29% for smartphones. The median and mode discounts for smartwatches are 74.5% and 75.0%, much higher than the 25% and 28% seen in smartphones. This implies that consumers looking for the best deals are more likely to find deeper and more frequent discounts on smartwatches than on smartphones on Amazon. Retailers may be using aggressive pricing strategies for smartwatches to attract buyers and increase sales in this category.

2. Smartwatches discounts exhibit more variability than smartphones discounts, as shown by a higher 
S.D. of 13.48 compared to 8.71 for smartphones.The greater variability suggests that consumers may encounter a broader variety of discount levels when shopping for smartwatches. Retailers might be experimenting with more diverse pricing strategies to attract different customer segments in the smartwatch market.

3. It can be deduced from the scatter plot in Figure 4 that products with very high percentage discounts have the most ratings. Therefore, we can say that the discount percentage may have a linear relationship with the ratings of Amazon smartwatches. For better clarity, regression analysis is required, From the result gotten later in the study, the relationship was non-linear.

4. There is a moderately weak positive linear relationship (correlation coefficient, R = 0.36) between the actual price of smartwatches and their discount percentage on Amazon. The relationship is statistically significant (p = 0.002), though only 13% of the variation in discount percentage is explained by price (R² = 0.13). 

5. The regression slope is 0.001. It is positive and it indicates that the higher-priced smartwatches tend to receive slightly larger absolute discounts. Offering larger absolute discounts on higher-priced smartwatches may be a strategic move to boost sales volume and clear high-margin inventory. This pricing strategy can also enhance the perceived value of premium products, encouraging more conversions.


### Recommendations

1. Amazon should increase the averaqge discount on next smartwatch releases to around 70-75%, aligning with the current high median (74.5%) and mode (75%) discounts, while maintaining larger absolute disounts on higher-priced models to attract premium buyers and clear inventory :)

2. For smartphones, Amazzon can raise the average discount to approximately 25 - 30%, closer  to the current median (25%) and mode (28%) to experiment with varied discount levels to match the 13.48% standard deviation seen in smartwatches, targeting diverse customer segments.

3. Amazon can analyze the non-linear relationship between disocunt percentages and product ratings for both smartwatches and smartphones, using rreal-time data from the upcoming discount period starting June 2025, to optimize pricing and boost engagement.

### Limitations

1. The weak correlation between smartwatch prices and disoucnt percentages limits the predictive power of the regression model, as other factors like brand, demand, or inventory levels likely influence discounts but were not analyzed.


