import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
    "meter_to_kilometer": 0.001,  # 1 meter = 0.001 kilometer
    "kilometer_to_meter": 1000,   # 1 kilometer = 1000 meters
    "gram_to_kilogram": 0.001,    # 1 gram = 0.001 kilogram
    "kilogram_to_gram": 1000,     # 1 kilogram = 1000 grams
    "centimeter_to_meter": 0.01,  # 1 cm = 0.01 meter
    "meter_to_centimeter": 100,   # 1 meter = 100 cm
    "mile_to_kilometer": 1.609,   # 1 mile = 1.609 kilometers
    "kilometer_to_mile": 0.621,   # 1 kilometer = 0.621 miles
    "pound_to_kilogram": 0.453,   # 1 pound = 0.453 kilograms
    "kilogram_to_pound": 2.205    # 1 kilogram = 2.205 pounds
    }

    key = f"{unit_from}_to_{unit_to}" 
    if key in conversions:
        return value * conversions[key]
    else:
        return "Conversion not supported"
    
st.title("Unit Converter")
st.write("Easily convert between different units of measurement.")

st.subheader("Select Your Conversion Parameters")
value = st.number_input("Enter the value to convert:")
unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram", "centimeter", "mile", "pound"])
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram", "centimeter", "mile", "pound"])
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    if isinstance(result, str):
        st.error("Invalid conversion. Please select compatible units.")
    else:
        st.success(f"Converted value: {result}")  
    