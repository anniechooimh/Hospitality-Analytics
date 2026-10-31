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
How can hospitality booking data be leveraged to identify the key factors influencing booking cancellations, occupancy patterns, customer value, distribution channel effectiveness, and reservation outcomes in order to support data-driven decision-making and improve hotel performance?

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

## Repository Contents
| File | Description |
| :--- | :---
| Capstone_Hospitality Analysis.ipynb |	Load and clean dataset; Generated both descriptive and predictive analysis |
| Bookings.csv, Hotels.csv, Customer Types.csv, Market Segments.csv, Reservation Status.csv | Raw datasets |
| bookings_clean.csv | Cleaned dataset produced using the notebook |
| Hotel Booking Dashboard.pbix | Power BI dashboard |
| ?!? | Project report and presentation |

## Dataset information
### Dataset Overview
The project uses 5 dataset csv files:
| Filename | Description | Records |
| :--- | :--- | :--- 
| Bookings.csv | Main booking transaction dataset | 119,390 |
| Hotels.csv | Hotel type information | 2 (Lookup Table) |
| Customer Types.csv | Customer, deposit, and meal information | 36 (Lookup Table) |
| Market Segments.csv | Market segment and distribution channel information | 26 (Lookup Table) |
| Reservation Status.csv | Reservation outcome information | 3 (Lookup Table) |

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


**Data Cleaning & Transformation**

The following preprocessing steps were performed in Python prior to analysis and visualization:

| Column Name | Original Type | Updated Type | Action Taken |
| :--- | :--- | :--- | :--- |
| children	| float64 |	int64 |	Filled missing values with 0 |
| agent	| float64 |	Int64	| Filled missing values with 0 (No Agent) |
| company |	float64 |	Int64 |	Filled missing values with 0 (No Company) |
| country	| object	| object |	Missing values replaced with 'Unknown' |
| reservation_status_date |	object	| datetime |	Converted to date format |
| is_canceled |	int64 |	Boolean	| Converted 0/1 to Boolean values |
| is_repeated_guest	| int64 |	Boolean	| Converted 0/1 to Boolean values |
| arrival_date	| Derived |	datetime |	Created from year, month, and day of month fields |
| total_nights |	Derived |	int64	| Total stay duration created from Weekend Nights + Week Nights	|
| total_price |	Derived | float64 | Estimated booking value created from ADR × Total Nights |

**Additional Power BI Transformations**
- Lead Time Category created for segmentation analysis
- DAX measures created for Average ADR, Average Stay Length, Booking Count, Cancellation Rate, Occupancy Rate, Total Bookings and Total Revenue.

## PowerBI Dashboard
<img width="1447" height="812" alt="image" src="https://github.com/user-attachments/assets/7360f0dc-15b7-4715-bea6-17248154b1fd" />

##

