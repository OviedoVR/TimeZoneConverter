# Required Python modules/packages
import streamlit as st
from datetime import datetime
import pytz

# Create a dictionary with country name and corresponding timezone
timezone_dict = {
    "North America": {
        "United States": "America/New_York",
        "Canada": "America/Toronto",
        "Mexico": "America/Mexico_City",
        "Jamaica": "America/Jamaica",
        "Costa Rica": "America/Costa_Rica",
        "Bahamas": "America/Nassau",
        "Honduras": "America/Tegucigalpa",
        "Cuba": "America/Havana",
        "Dominican Republic": "America/Santo_Domingo"
    },
    "South America": {
        "Brazil": "America/Sao_Paulo",
        "Argentina": "America/Argentina/Buenos_Aires",
        "Chile": "America/Santiago",
        "Colombia": "America/Bogota",
        "Peru": "America/Lima",
        "Uruguay": "America/Montevideo",
        "Ecuador": "America/Guayaquil",
        "Bolivia": "America/La_Paz",
        "Paraguay": "America/Asuncion",
        "Venezuela": "America/Caracas"
    },
    "Europe": {
        "United Kingdom": "Europe/London",
        "France": "Europe/Paris",
        "Germany": "Europe/Berlin",
        "Italy": "Europe/Rome",
        "Spain": "Europe/Madrid",
        "Russia": "Europe/Moscow",
        "Turkey": "Europe/Istanbul",
        "Greece": "Europe/Athens",
        "Poland": "Europe/Warsaw",
        "Ukraine": "Europe/Kiev"
    },
    "Asia": {
        "India": "Asia/Kolkata",
        "Japan": "Asia/Tokyo",
        "China": "Asia/Shanghai",
        "Saudi Arabia": "Asia/Riyadh",
        "South Korea": "Asia/Seoul",
        "Indonesia": "Asia/Jakarta",
        "Malaysia": "Asia/Kuala_Lumpur",
        "Vietnam": "Asia/Ho_Chi_Minh",
        "Philippines": "Asia/Manila",
        "Thailand": "Asia/Bangkok"
    },
    "Australia": {
        "Australia": "Australia/Sydney",
        "New Zealand": "Pacific/Auckland",
        "Fiji": "Pacific/Fiji",
        "Papua New Guinea": "Pacific/Port_Moresby",
        "Samoa": "Pacific/Apia",
        "Tonga": "Pacific/Tongatapu",
        "Solomon Islands": "Pacific/Guadalcanal",
        "Vanuatu": "Pacific/Efate",
        "Kiribati": "Pacific/Tarawa",
        "New Caledonia": "Pacific/Noumea"
    }
}

# Create a list of continents
continents = ["North America", "South America", "Europe", "Asia", "Australia"]


# Streamlit app:
st.set_page_config(
    page_title='Time Zone Coverter', 
    page_icon='🌎',
    layout='centered',
    initial_sidebar_state='expanded',
    menu_items={
        'About': """This app is intended to select a country, get its 
        time zone in UTC format  and have its correspondent result 
        from a user-entered PST time.
        """
    }  

)
st.header('Time Zone Coverter Streamlit app')

# Add some blank space
st.markdown("##")

# Create a dropdown to select a continent
continent = st.sidebar.selectbox("1. Select a continent", continents)

# Create a dropdown to select a country within the selected continent
countries = list(timezone_dict[continent].keys())
country = st.sidebar.selectbox("2. Select a country", countries)

# Display the selected UTC offset
st.markdown("### :earth_americas: Corresponding UTC time:")
timezone = timezone_dict[continent][country]
utc_offset = datetime.now(pytz.timezone(timezone)).strftime('%z')
st.markdown(f"> **{country}** time zone is **UTC{utc_offset[:-2]}:{utc_offset[-2:]}**")

# Add some blank space
st.markdown("##")

# Create input for PST time
st.markdown("### :clock10: PST time to UTC converter:")
pst_input = st.text_input("Enter PST time (e.g., 10:00 AM PST)")

# Convert PST time to UTC+X
try:
    pst_time = datetime.strptime(pst_input, "%I:%M %p PST")
    pst_time = pytz.timezone("US/Pacific").localize(pst_time, is_dst=None)
    target_time = pst_time.astimezone(pytz.timezone(timezone)).strftime("%I:%M %p %Z")
    st.markdown(f"> The corresponding time in **{country}** is **{target_time}**")
except:
    st.markdown("""
    :lock: Invalid input format. Please enter PST time in format 
    '<span style="color:#7ef471"><b> 10:00 AM PST </b></span>'
    """, unsafe_allow_html=True)
