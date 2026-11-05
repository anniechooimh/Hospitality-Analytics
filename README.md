# Hospitality Analytics Captstone Project
Hospitality Analytics using Python and Power BI to uncover booking trends, customer behavior, revenue drivers, and cancellation patterns in the hotel industry.

<div align="center">
  <img width="280" height="280" alt="image" src="https://github.com/user-attachments/assets/e499fbdc-0d58-494c-bf5b-49639b006afd" />
</div>

- **Prepared by: Annie Chooi**
- **Dataset used: Hotel Booking**
- **Link to Jupyter Notebook in Google Colab: https://github.com/anniechooimh/Hospitality-Analytics**

## Project Overview
The hospitality industry faces ongoing challenges in managing booking cancellations, maximizing occupancy rates, improving customer retention, and optimizing revenue generation. Hotel managers require data-driven insights to better understand customer behavior, booking patterns, and channel performance in order to support strategic decision-making. This analysis explores the hotel booking patterns using past data to uncover a comprehensive view of guest behavior and operational performance. 

The project combines Python for data cleaning, exploratory data analysis (EDA), and machine learning, together with Power BI for interactive dashboard development and storytelling.

## Business Problem
How can historical booking data be leveraged to improve hotel performance, reduce cancellations, optimize occupancy, and identify high-value customer segments?

## Research Objectives
1. Identify the Main Factors Influencing Booking Cancellations
> Analyze booking characteristics such as lead time, deposit type, customer type and market segment to determine what drives cancellations.
2. Analyze Occupancy Patterns
> Examine booking trends across months, hotel types, and length of stay to understand factors affecting hotel occupancy.
3. Evaluate Customer Segments
> Compare different customer groups to identify the most valuable and profitable customer segments based on booking behavior and revenue contribution.
4. Assess Distribution Channel Performance
> Analyze booking channels (Direct, Corporate, TA/TO, Online Travel Agents) to determine which channels generate the highest bookings, revenue, and lowest cancellation rates.
5. Examine Reservation Outcomes
> Analyze factors associated with reservation statuses such as Check-Out, Canceled, and No-Show to improve booking management decisions.

## Dataset information
The analysis is based on five CSV datasets consisting of:
| Filename | Description | Records |
| :--- | :--- | :--- 
| Bookings.csv | Main booking transaction dataset | 119,390 |
| Hotels.csv | Hotel type | 2 (Lookup Table) |
| Customer Types.csv | Customer, deposit, and meal information | 36 (Lookup Table) |
| Market Segments.csv | Market segment and distribution channel information | 26 (Lookup Table) |
| Reservation Status.csv | Reservation outcome information | 3 (Lookup Table) |

### Dataset Size
- Total Records: 119,390
- Analysis Period: July 2015 – August 2017
- Hotel Types:
     - City Hotel
     - Resort Hotel

### Data Dictionary
**Bookings Table Description:**
| Column Name | Data Type | Description | Example Value |
| :--- | :--- | :--- | :--- |
| Booking_ID | Integer | Unique identifier assigned to each booking record. | 18  |
| Hotel_ID | Integer | Identifier of the hotel associated with the booking. | 1 |
| Market_Segment_ID	| Integer	| Identifier of the booking market segment and distribution channel. | 4 |
| Customer_Type_ID	| Integer	| Identifier of the customer classification, deposit type, and meal plan. | 4 |
| Reservation_ID | Integer | Identifier of the reservation status. | 1 |
| is_canceled |	Boolean |	Indicates whether the booking was canceled. | 0 |
| lead_time	| Integer |	Number of days between booking creation and arrival date. | 37 |
| arrival_date_year	| Integer |	Year of guest arrival. | 2015 |
| arrival_date_month | Category |	Month of guest arrival. | July |
| arrival_date_week_number | Integer | Week number of guest arrival. | 27 |
| arrival_date_day_of_month |	Integer |	Day of the month of guest arrival. | 1 |
| stays_in_weekend_nights	| Integer |	Number of weekend nights booked. | 0 |
| stays_in_week_nights | Integer | Number of weekday nights booked. | 4 |
| adults | Integer | Number of adult guests included in the booking. | 2 |
| children | Integer | Number of child guests included in the booking. | 0 |
| babies | Integer | Number of babies included in the booking. | 0 |
| country	| Category | Country of origin of the guest. | PRT |
| is_repeated_guest | Boolean | Indicates whether the guest has booked previously. | 0 |
| previous_cancellations | Integer | Number of previous canceled bookings by the guest. | 0 |
| previous_bookings_not_canceled | Integer | Number of previous completed bookings by the guest. | 0 |
| booking_changes | Integer | Number of modifications made to the booking. | 0 |
| agent	| Category | Travel agent identifier associated with the booking. | 8 |
| company |	Category | Company identifier associated with the booking. | 110 |
| days_in_waiting_list | Integer | Number of days the booking remained on a waiting list. | 0 |
| adr |	Float	| Average Daily Rate charged for the booking. | 97.5 |
| required_car_parking_spaces | Integer |	Number of parking spaces requested by the guest. | 0 |
| total_of_special_requests	| Integer | Number of special requests submitted by the guest. | 0 |
| reservation_status_date	| Date | Date on which the reservation status was recorded. | 5/7/2015 |


**Hotels Table Description:**
| Column Name | Data Type | Description | Example Value |
| :--- | :--- | :--- | :--- |
| Hotel_ID | Integer | Unique identifier assigned to a hotel. | 1 |
| hotel | Text | Name or category of the hotel. | Resort Hotel |


**Market Segments Table Description:**
| Column Name | Data Type | Description | Example Value |
| :--- | :--- | :--- | :--- |
| Market_Segment_ID | Integer | Unique identifier assigned to a market segment record. | 8 |
| market_segment | Category | Market segment through which the booking was acquired. | Groups |
| distribution_channel | Category | Distribution channel used to make the booking. | Corporate |


**Customer Types Table Description:**
| Column Name | Data Type | Description | Example Value |
| :--- | :--- | :--- | :--- |
| Customer_Type_ID | Integer | Unique identifier assigned to a customer type record. | 4 |
| customer_type | Category | Classification of the customer booking behavior. | Contract |
| deposit_type | Category | Deposit policy applied to the booking. | No Deposit |
| meal | Category | Meal package selected for the booking. | BB (Bed & Breakfast) |


**Reservation Status Table Description:**
| Column Name | Data Type | Description | Example Value |
| :--- | :--- | :--- | :--- |
| Reservation_ID | Integer | Unique identifier assigned to a reservation status. | 3 |
| reservation_status | Category | Final status of the reservation. | No-Show |


## Data Cleaning & Preparation
Following preprocessing steps were performed in Python:

| Column Name | Original Type | Updated Type | Action Taken |
| :--- | :--- | :--- | :--- |
| children	| float64 |	int64 |	Filled missing values with 0 |
| agent	| float64 |	Int64	| Filled missing values with 0 (No Agent) |
| company |	float64 |	Int64 |	Filled missing values with 0 (No Company) |
| country	| object	| object |	Replaced missing values with 'Unknown' |
| reservation_status_date |	object	| datetime |	Converted to date format |
| is_canceled |	int64 |	Boolean	| Converted 0/1 to Boolean values |
| is_repeated_guest	| int64 |	Boolean	| Converted 0/1 to Boolean values |
| arrival_date	| Derived |	datetime |	Created from year, month, and day of month fields |
| total_nights |	Derived |	int64	| Total stay duration created from Weekend Nights + Week Nights	|
| total_price |	Derived | float64 | Estimated booking value created from ADR × Total Nights |

Created additional analytical fields in Power BI:
- Lead Time Category created for segmentation analysis
- DAX measures created for Average ADR, Average Stay Length, Booking Count, Cancellation Rate, Occupancy Rate, Total Bookings and Total Revenue.

## Data Model
The bookings dataset was merged with:
- Customer Type
- Market Segment
- Reservation Status
- Hotel Type
to create a centralized analytical dataset.

## Exploratory Data Analysis
The analysis focused on five key business areas:

**1. Cancellation Analysis**

Investigated cancellation behavior across: Lead Time, Customer Type, Deposit Type and Distribution Channel.
  
Key Findings: 
- Cancellation rates increase significantly with longer lead times.
- Transient customers exhibited the highest cancellation rate.
- OTA/TA/TO channels generated the highest booking volume but also the highest cancellation rate.
- Deposit type showed strong influence on cancellation behavior.

Business Impact: High cancellation rates reduce occupancy predictability and revenue realization.

**2. Occupancy Pattern Analysis**

Analyzed occupancy trends by: Hotel Type, Month and Stay Duration.

Key Findings
- City Hotels achieved higher occupancy levels than Resort Hotels.
- Peak demand periods occurred during May and August.
- Resort Hotels attracted longer average stays.

Business Impact: Understanding seasonality supports workforce planning, pricing optimization, and inventory management.

**3. Customer Segment Evaluation**
Customer performance was evaluated using: Booking Volume, Revenue Contribution, Average Daily Rate (ADR) and Cancellation Rate.

Key Findings
- Transient customers generated the highest revenue contribution.
- Group bookings demonstrated lower cancellation rates.
- Customer value and booking reliability varied significantly across segments.

Business Impact: Revenue growth opportunities exist within high-value customer segments while managing cancellation risk.

**4. Distribution Channel Performance**
Channel effectiveness was evaluated across: Direct, TA/TO, Corporate and Groups

Key Findings
- TA/TO channels delivered the highest booking volumes.
- Direct bookings recorded the lowest cancellation rates.
- Direct channels provided the most reliable revenue source.

Business Impact: Reducing dependency on third-party channels can improve booking quality and profitability.

**5. Reservation Outcome Analysis**
Compared: Completed Stays and Cancelled Reservations

Key Findings
- Cancelled reservations exhibited significantly longer lead times.
- Guests who completed stays submitted more special requests.
- Guest engagement appears to correlate with stay completion.

Business Impact: Pre-arrival engagement initiatives may reduce cancellation risk and improve customer experience.


## PowerBI Dashboard
An interactive management dashboard was developed in Power BI to monitor hotel performance.

**Executive KPIs**
- Total Bookings
- Completed Stays
- Revenue
- Occupancy Rate
- Cancellation Rate

**Interactive Filters**
- Hotel Type
- Customer Type
- Market Segment
- Reservation Status
- Arrival Date

**Visualizations**
- Monthly Occupancy Trends
- Revenue Analysis
- Cancellation Analysis
- Customer Segment Performance
- Distribution Channel Performance
- Reservation Outcome Analysis

<img width="1441" height="806" alt="image" src="https://github.com/user-attachments/assets/7cafea6b-461c-4c08-a445-9eba38c916ef" />


## Key Business Insights
### 1. Cancellation Drivers
- Lead time strongly influences cancellation risk. Bookings made within 30 days had an 18.56% cancellation rate, while bookings made more than 365 days in advance reached 67.66%. This suggests booking commitment decreases as the reservation horizon grows.
- Transient customers showed the highest cancellation rate at 40.75%, while Group bookings had the lowest at 10.23%.
3. Although No Deposit bookings account for the largest share of total cancellations, likely due to their high booking volume, a deposit-type-level analysis reveals that approximately 99% of Non-Refund bookings were cancelled, highlighting deposit type as a significant factor associated with cancellation behavior.
   
### 2. Occupancy Patterns
- City Hotels consistently outperformed Resort Hotels in completed bookings. The peak month for City Hotels was May 2017 with 2,339 completed bookings, while Resort Hotels peaked at 1,417 bookings in October 2016.
- Majority of completed bookings are short stays of 1 to 4 nights, especially for City Hotels, while Resort Hotels show a relatively higher proportion of longer stays, suggesting differing guest travel behaviors and occupancy patterns between the two hotel types.

### 3. Customer Segment Evaluation
- Customer segment analysis reveals that Transient customers are the most valuable segment, contributing approximately $19.33 million in revenue and generating the highest Average Daily Rate (ADR) of $104.78. However, this segment also records the highest cancellation rate at 40.75%, indicating a trade-off between revenue generation and booking reliability.
- On the other hand, Contract and Group customers contribute less revenue but demonstrate greater booking stability and lower cancellation rates, making them potentially valuable for occupancy planning and demand forecasting.

### 4. Distribution Channel Performance
- TA/TO (Travel Agents/Tour Operators) channel is the dominant distribution channel, generating 57,718 completed bookings and $20.81 million in revenue. However, it also records a relatively high cancellation rate at 41.03%.
- In contrast, the Direct channel demonstrates the strongest overall performance, combining substantial revenue generation of $4.33 million with the lowest cancellation rate at 17.46%, indicating that direct bookings are both more reliable and more valuable for hotel profitability.

### 5. Reservation Outcomes
- Reservation outcomes are strongly associated with lead time and the number of special requests. Cancelled bookings have the longest average lead time of 147.3 days, nearly twice that of completed stays (79.9 days), suggesting that reservations made further in advance are more susceptible to cancellation.
- Conversely, Check-Out reservations represent the majority of bookings (75,166) and record the highest average number of special requests (0.71 per booking), indicating that guests who engage more with the hotel prior to arrival are more likely to complete their stays.
- No-Show bookings remain relatively low (1,207 bookings) and are characterized by shorter lead times and moderate request levels.

## Predictive Analytics: Random Forest Classifier
### Objective

A predictive machine learning model was developed to determine whether an upcoming hotel booking is likely to be cancelled. The model supports proactive decision-making by identifying reservations with a higher risk of cancellation, enabling hotels to improve occupancy management, revenue forecasting, and customer engagement strategies.

- Target (y): is_canceled (0 = Not Cancelled, 1 = Cancelled)
- Features (X): lead_time, adr, total_nights, customer_type, market_segment, deposit_type
- Excluded: Booking identifiers and target-related fields to prevent data leakage
- Preprocessing: Categorical variables (customer_type, market_segment, deposit_type) were one-hot encoded using pd.get_dummies() with drop_first=True
- Model: Random Forest Classifier (n_estimators=100, max_depth=15, random_state=42)
- Split: 80/20 stratified train-test split (95,512 training records, 23,878 testing records)

| Metric | Score |
| :--- | :--- |
| Accuracy | 0.784 |
| Precision |	0.881 |
| Recall | 0.483 |
| F1-Score | 0.624 |
| AUC-ROC |	0.863 |

The model achieved 78.4% accuracy and an AUC-ROC of 0.863, indicating strong ability to distinguish between cancelled and non-cancelled bookings. The high precision (88.1%) suggests that when the model predicts a cancellation, it is usually correct, making it suitable for proactive retention and occupancy management initiatives.

<img width="1201" height="435" alt="image" src="https://github.com/user-attachments/assets/88edc677-1e65-4e08-aef6-08799e37b614" />

The model correctly identified 14,456 non-cancelled bookings and 4,275 cancelled bookings. Although some cancellations were missed, the relatively low number of false positives (577) demonstrates strong reliability when flagging bookings as likely to cancel.

The ROC curve shows that the model performs substantially better than random classification (AUC = 0.50). An AUC of 0.863 indicates strong predictive capability and confirms that booking characteristics contain meaningful signals for cancellation risk prediction.

Overall, the Random Forest model provides a practical decision-support tool that complements the dashboard's descriptive analysis by helping management anticipate future booking cancellations and take proactive action.

## Business Recommendations
Based on the analysis of booking behavior, cancellations, customer segments, distribution channels, and occupancy patterns, the following strategic recommendations are proposed:

**1. Implement Risk-Tiered Booking Controls**

Focus on high-risk bookings, particularly long lead-time reservations, Transient customers, and OTA/TA/TO channels. Introduce deposit requirements, booking guarantees, automated reminder communications, and reconfirmation processes to reduce cancellation risk and improve booking reliability.

Success Metrics: Cancellation rate by risk tier.

**2. Expand Direct Booking Conversion Programs**

Increase direct booking share by targeting repeat and engaged guests through loyalty benefits, exclusive member offers, post-stay promotions, and direct rebooking incentives. This can reduce dependency on third-party channels and improve booking retention.

Success Metrics: Direct booking share and direct booking cancellation rate.

**3. Develop a Seasonal Occupancy Management Strategy**

Leverage seasonal demand patterns to optimize staffing, room inventory allocation, pricing strategies, minimum-stay policies, and promotional packages. Tailor approaches according to the differing demand profiles of City Hotels and Resort Hotels.

Success Metrics: Occupancy rate, Average Daily Rate (ADR), and average stay length.

**4. Strengthen Pre-Arrival Guest Engagement**

Increase guest interaction before arrival through preference collection, personalized communications, and service prompts. Greater guest engagement can improve commitment to reservations and enhance the overall guest experience.

Success Metrics: Guest request rate and stay completion rate.

**Expected Business Outcomes**

- Reduced booking cancellations
- Improved occupancy utilization
- Increased revenue quality and booking reliability
- Higher proportion of direct bookings
- Better operational and workforce planning
- Enhanced guest engagement and retention

This recommendation framework enables hotel management to shift focus from simply generating bookings to maximizing completed stays, revenue realization, and long-term customer value.


## Tools & Technologies
| Tool | Purpose |
| :--- | :--- |
| Python | Data cleaning, transformation, EDA |
| Pandas | Data manipulation |
| NumPy |	Numerical calculations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Power BI | Dashboard development |
| Excel |	Data validation and review |
| GitHub | Project documentation and version control |


## Repository Contents
| File | Description |
| :--- | :---
| Capstone_Hospitality Analysis.ipynb |	Load and clean dataset; Generated both descriptive and predictive analysis |
| Bookings.csv, Hotels.csv, Customer Types.csv, Market Segments.csv, Reservation Status.csv | Raw datasets |
| bookings_clean.csv | Cleaned dataset produced using the notebook |
| Hotel Booking Dashboard.pbix | Power BI dashboard |
| Presentation Slides_Annie Chooi.pdf | Project report and presentation slides |


