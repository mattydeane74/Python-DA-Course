
# The Airlines delay dataset contains flight data for the United States for Jan 2020

## The dataset was downloaded from Kaggle is saved in the datasets directory

## A clean version of the dataset is saved under Lesson 6 as "cleaned_Jan2020_airline_delay.csv"

This was a very useful dataset as it allowed a few columns to be created, some cleaning was required and there are some nice patterns to explore in the dataset.

The next steps would be to run some multi-dimensional analysis on top of what has been found in the opening exploratory analysis.

1. clear pattern of delays based on time buckets

2. clear patterns with airlines and airports on delays

3. No real evidence of delay pattern based on the flight distance in this dataset.

4. performed some multi-dimensional analysis using Airport and Airlines per time buckets. Clear patterns on flight delays getting
   worse throughout the day. Hub airports look worse and dominant airlines seem to have better records which may come from more
   resources and more power over air control.


Some of the pre-bucketed data not accurate so as the alignment of departure time to the departure time buckets. The time bucket which I created seems very useful.

The merging of airport names to the dataset was not perfect but only affected less than 5 percent of the dataset. For the airport based analysis, I excluded this from the analysis.

Missing airport names and flight count or 0.3% of the dataset;

AZA    495
ECP    476
FCA    264
HHH    186
SCE    116
USA    112
PBG    108
MQT     95
XWA     68
IAG     55
VEL     53
SPN     44
BFM     13
