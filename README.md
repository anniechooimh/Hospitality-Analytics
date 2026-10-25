# Hospitality Analytics Captstone Project
Hospitality Analytics using Python and Power BI to uncover booking trends, customer behavior, revenue drivers, and cancellation patterns in the hotel industry.

<div align="center">
  <img width="280" height="280" alt="image" src="https://github.com/user-attachments/assets/e499fbdc-0d58-494c-bf5b-49639b006afd" />
</div>

- **Prepared by: Annie Chooi**
- **Dataset used: Hotel Booking**

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

## Dataset information
### Dataset Overview
The project uses 5 dataset csv files:
| Filename | Description | Records |
| :--- | :--- | :--- 
| Bookings.csv | Main booking transaction dataset | 119,390 |
| Hotels.csv | Hotel type information | 2 |
| Customer Types.csv | Customer, deposit, and meal information | Lookup Table |
| Market Segments.csv | Market segment and distribution channel information | Lookup Table |
| Reservation Status.csv | Reservation outcome information | Lookup Table |

### Data Dictionary
**Bookings Table Description:**
| Column Name | Data Type | Description | Example Value |
| :--- | :--- | :--- | :--- |
| Booking_ID | Integer | Unique identifier assigned to each booking record. |   |
| Hotel_ID | Integer | Identifier of the hotel associated with the booking. |   |
| Market_Segment_ID	| Integer	| Identifier of the booking market segment and distribution channel. |   |
| Customer_Type_ID	| Integer	| Identifier of the customer classification, deposit type, and meal plan. |   |
| Reservation_ID | Integer | Identifier of the reservation status. |   |
| is_canceled |	Boolean |	Indicates whether the booking was canceled. |   |
| lead_time	| Integer |	Number of days between booking creation and arrival date. |   |
| arrival_date_year	| Integer |	Year of guest arrival. |   |
| arrival_date_month | Category |	Month of guest arrival. |   |
| arrival_date_week_number | Integer | Week number of guest arrival. |   |
| arrival_date_day_of_month |	Integer |	Day of the month of guest arrival. |   |
| stays_in_weekend_nights	| Integer |	Number of weekend nights booked. |   |
| stays_in_week_nights | Integer | Number of weekday nights booked. |   |
| adults | Integer | Number of adult guests included in the booking. |   |
| children | Integer | Number of child guests included in the booking. |   |
| babies | Integer | Number of babies included in the booking. |   |
| country	| Category | Country of origin of the guest. |   |
| is_repeated_guest | Boolean | Indicates whether the guest has booked previously. |   |
| previous_cancellations | Integer | Number of previous canceled bookings by the guest. |   |
| previous_bookings_not_canceled | Integer | Number of previous completed bookings by the guest. |   |
| booking_changes | Integer | Number of modifications made to the booking. |   |
| agent	| Category | Travel agent identifier associated with the booking. |   |
| company |	Category | Company identifier associated with the booking. |   |
| days_in_waiting_list | Integer | Number of days the booking remained on a waiting list. |   |
| adr |	Float	| Average Daily Rate charged for the booking. |   |
| required_car_parking_spaces | Integer |	Number of parking spaces requested by the guest. |   |
| total_of_special_requests	| Integer | Number of special requests submitted by the guest. |   |
| reservation_status_date	| Date | Date on which the reservation status was recorded. |   |


**Hotels Table Description:**
| Column Name | Data Type | Description | Example Value |
| :--- | :--- | :--- | :--- |
| Booking_ID | Integer | Unique identifier assigned to each booking record. |   |


**Market Segments Table Description:**
| Column Name | Data Type | Description | Example Value |
| :--- | :--- | :--- | :--- |
| Booking_ID | Integer | Unique identifier assigned to each booking record. |   |


**Customer Types Table Description:**
| Column Name | Data Type | Description | Example Value |
| :--- | :--- | :--- | :--- |
| Booking_ID | Integer | Unique identifier assigned to each booking record. |   |


**Reservation Status Table Description:**
| Column Name | Data Type | Description | Example Value |
| :--- | :--- | :--- | :--- |
| Booking_ID | Integer | Unique identifier assigned to each booking record. |   |



Derived Features

The new features you created during data preparation.

Feature Engineering
Feature	Formula	Descriptionarrival_date	Year + Month + Day	Full arrival date
total_nights	Weekend Nights + Week Nights	Total stay duration
total_guests	Adults + Children + Babies	Total number of guests
total_price	ADR × Total Nights	Estimated booking value
lead_time_category	Grouped Lead Time	Booking lead time bands



## PowerBI Dashboard
<img width="1335" height="755" alt="image" src="https://github.com/user-attachments/assets/aa052f56-a0b9-49ef-8be9-9c6df77ed495" />


