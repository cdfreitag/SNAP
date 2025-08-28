# SNAP
The purpose of the project is to create an intersecion of the need for SNAP at a household level according to community areas and the availability of SNAP stores in their community areas in all the various forms from supermarkets to convenience stores.

    Datasets:

     1. American Community Survey Data 
 Available on: https://data.census.gov/table?q=acs&y=2023 
 
 We have considered the 2019-2023 American Community Survey (ACS) 5-year estimates for  this project.
 
 This data was published in Dec 2024 and is the most recent data available at this time. The data is broken down to the local statistics for multiple topics from work status to  education level, language spoken at home, nativity, veteran status, and selected monthly homeowner costs. The data is segregated by households, by age, family size,  number of workers and disability status to name a few. The data also includes estimates and their margins of error.
 
 For the purpose of this project we have considered the "Estimate!!Households receiving food stamps/SNAP!!Households"
 
 This will give us census tracts in Illinois with SNAP, which will need to be converted into community areas to enable analysis
 
     2. Historical SNAP Retail locator 
 Available on: https://www.fns.usda.gov/snap/retailer/historical-data

 This data provides the kind of store (convenience, supermaket, meat/poultry, etc) that accept SNAP across American cities with the precise latitute and longitude. We looked at Chicago specific stores and had to filter down for active stores.    
 
     3. Census Tracts
 This was retrived from the Chicago data portal to join Historical SNAP retail locator and the ACS data
 
     4. Chicago boundaries map
 This was also retrived from the Chicago data portal to join Historical SNAP retail locator and the ACS data


    Methodology:
We first had to parse the American Community Survey data for the relevant columns which was then translated into community area level from census tract level. The more tedious part of the analysis was cleaning the Historical SNAP retail locator which had misspellings of Chicago, and inaccuracies in zipcode data which is reflected in the code. After joining the two, we developed our own SNAP Analysis where we had columns like Total households, SNAP households, percentage of SNAP households in a community area, and the number and type of store, segregated by community area. Our team then analyzed the data to deliver the data statements which could be validated/disproven by ground reporting.

    For future reporting:
We highly reccomend journalists looking to refactor the code to evaluate the challenges such as misspellings and incorrect entries in the historical SNAP data and reconciling the margin of error in the ACS data before attempting the same. 

All data and code for this project are organized in our repository (see the project’s data folder and code notebook). Here’s how to make the most of it:

Data Files: The file snap_retailers_chicago.csv contains all SNAP-authorized retailers in Chicago (2004–2024), with their coordinates, store type, and community area. 
The file chicago_snap_households.csv contains the ACS-derived metrics for each community area – including total households, SNAP households, and the percentage on SNAP (plus some demographics for context, if needed). 

We also include snap_gap_by_community.xlsx which compiles key results (like store counts, ratios, rankings by community) for quick reference. 
All source data citations are documented: USDA FNS for retailer data, U.S. Census Bureau ACS for household data, etc. 
If you use these data, please credit those sources.

We acknowledge that data like this benefits from periodic updates. 
The USDA releases updated retailer data annually (usually mid-year for the prior year), and the ACS publishes new 5-year estimates each year. We recommend updating the analysis with 2025 data when available, to capture any effects post-pandemic or after the policy changes.  Our code is set up to accommodate new data with minimal changes – for instance, one can swap in the 2018–2022 ACS data file when it’s out. 

We hope journalists, researchers, and community organizations can use this work as a framework to investigate SNAP access in other cities or to dig deeper into Chicago’s situation. The combination of public data and open-source analysis makes it possible to hold policymakers accountable: if certain neighborhoods have been left behind, the data will show it. 

Feel free to reach out to our team if you have questions on using the data janarthananjanani99@gmail.com

This project is the original work of Sara Cooper, Christiana Freitag, Janani Jana and Menatalla Ibrahim with assistance from Matt Kiefer for Medill School of Journalism, Northwestern University. August 29,2025.
    
