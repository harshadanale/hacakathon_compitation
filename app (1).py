import streamlit as st
import pandas as pd

# Load dataset
ds = pd.read_csv("local_services_dataset.csv")
ds['location_clean'] = ds['location'].astype(str).str.strip().str.lower()

# Title
st.title("🔎 Local Services Finder")

# Dropdown for location
all_locations = sorted(ds['location'].unique())
location_input = st.selectbox("Select a location:", ["-- Choose --"] + all_locations)

if location_input != "-- Choose --":
    # Filter
    services = ds[ds['location'] == location_input]
    if not services.empty:
        st.subheader(f"Services in {location_input}")
        for _, row in services.iterrows():
            with st.container():
                st.markdown(
                    f"""
                    <div style="background-color:#f9f9f9; padding:15px; border-radius:10px; margin-bottom:10px;
                                box-shadow: 0px 2px 6px rgba(0,0,0,0.1);">
                        <h4 style="margin:0;">{row['name']}</h4>
                        <p style="margin:2px 0;">⭐ {row['rating']} | {row['service']}</p>
                        <p style="margin:2px 0;">📍 {row['location']} | 📞 {row['contact']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    else:
        st.warning("No services found for this location.")
