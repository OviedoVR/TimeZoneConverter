# Time Zone Converter

This app is intended to select a country, get its time zone in UTC format and have its correspondent result from a user-entered PST time.
(**created for Streamlit blogging**)

## Problem to be solved:

    * Customers often inform a deadline in PST time zone format
    * That need to be converted into UTC time zone format for my corresponding country
    * However, one needs to know the corresponding UTC offset and the converted time in a straightfoward way
    * I mean, no boring ads and simple usage

## Steps for the solution:

    1. Create a dictionary with contry and corresponding time zone
    2. Create list of continents
    3. Configure the Streamlit page and title
    4. Create sidebar selector components for continent and country
    5. Get the corresponding UTC time zone for the sidebar selection
    6. Create the "PST to UTC+offset" time zone converter
