import streamlit as st
import math

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Mechanical Engineering Toolkit",
    page_icon="⚙️",
    layout="wide"
)

# =========================
# HEADER
# =========================

st.title("⚙️ Mechanical Engineering Toolkit")

st.markdown("""
### Developed By
- **Name:** Muhammad Subhan Babar
- **Roll Number:** 25-ME-195
""")

st.markdown("---")

# =========================
# SIDEBAR MENU
# =========================

menu = st.sidebar.selectbox(
    "Select Tool",
    [
        "Simple Calculator",
        "Scientific Calculator",
        "Mechanical Calculator",
        "Density Checker",
        "Mechanical Unit Converter"
    ]
)

# =========================
# SIMPLE CALCULATOR
# =========================

if menu == "Simple Calculator":

    st.header("🧮 Simple Calculator")

    num1 = st.number_input("Enter First Number", value=0.0)
    num2 = st.number_input("Enter Second Number", value=0.0)

    operation = st.selectbox(
        "Select Operation",
        ["Addition", "Subtraction", "Multiplication", "Division"]
    )

    result = 0

    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1 * num2

    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero")

    st.success(f"Result = {result}")

# =========================
# SCIENTIFIC CALCULATOR
# =========================

elif menu == "Scientific Calculator":

    st.header("🔬 Scientific Calculator")

    number = st.number_input("Enter Number", value=1.0)

    operation = st.selectbox(
        "Choose Function",
        [
            "Square Root",
            "Square",
            "Cube",
            "Sin",
            "Cos",
            "Tan",
            "Log",
            "Factorial"
        ]
    )

    try:

        if operation == "Square Root":
            result = math.sqrt(number)

        elif operation == "Square":
            result = number ** 2

        elif operation == "Cube":
            result = number ** 3

        elif operation == "Sin":
            result = math.sin(math.radians(number))

        elif operation == "Cos":
            result = math.cos(math.radians(number))

        elif operation == "Tan":
            result = math.tan(math.radians(number))

        elif operation == "Log":
            result = math.log10(number)

        elif operation == "Factorial":
            result = math.factorial(int(number))

        st.success(f"Result = {result}")

    except:
        st.error("Invalid Input")

# =========================
# MECHANICAL CALCULATOR
# =========================

elif menu == "Mechanical Calculator":

    st.header("⚙️ Mechanical Calculator")

    mech_type = st.selectbox(
        "Select Formula",
        [
            "Force",
            "Pressure",
            "Work",
            "Power",
            "Density"
        ]
    )

    # FORCE
    if mech_type == "Force":

        mass = st.number_input("Enter Mass (kg)")
        acceleration = st.number_input("Enter Acceleration (m/s²)")

        force = mass * acceleration

        st.success(f"Force = {force} N")

    # PRESSURE
    elif mech_type == "Pressure":

        force = st.number_input("Enter Force (N)")
        area = st.number_input("Enter Area (m²)")

        if area != 0:
            pressure = force / area
            st.success(f"Pressure = {pressure} Pa")
        else:
            st.error("Area cannot be zero")

    # WORK
    elif mech_type == "Work":

        force = st.number_input("Enter Force (N)")
        distance = st.number_input("Enter Distance (m)")

        work = force * distance

        st.success(f"Work Done = {work} Joules")

    # POWER
    elif mech_type == "Power":

        work = st.number_input("Enter Work (J)")
        time = st.number_input("Enter Time (s)")

        if time != 0:
            power = work / time
            st.success(f"Power = {power} Watts")
        else:
            st.error("Time cannot be zero")

    # DENSITY
    elif mech_type == "Density":

        mass = st.number_input("Enter Mass (kg)")
        volume = st.number_input("Enter Volume (m³)")

        if volume != 0:
            density = mass / volume
            st.success(f"Density = {density} kg/m³")
        else:
            st.error("Volume cannot be zero")

# =========================
# DENSITY CHECKER
# =========================

elif menu == "Density Checker":

    st.header("🧱 Material Density Checker")

    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Titanium": 4500,
        "Cast Iron": 7200
    }

    material = st.selectbox(
        "Select Material",
        list(materials.keys())
    )

    density = materials[material]

    st.info(f"Density of {material} = {density} kg/m³")

# =========================
# UNIT CONVERTER
# =========================

elif menu == "Mechanical Unit Converter":

    st.header("📏 Mechanical Unit Converter")

    conversion = st.selectbox(
        "Select Conversion",
        [
            "Length",
            "Mass",
            "Temperature",
            "Pressure"
        ]
    )

    # LENGTH
    if conversion == "Length":

        value = st.number_input("Enter Meter Value")

        cm = value * 100
        mm = value * 1000
        feet = value * 3.28084

        st.success(f"{value} m = {cm} cm")
        st.success(f"{value} m = {mm} mm")
        st.success(f"{value} m = {feet} ft")

    # MASS
    elif conversion == "Mass":

        value = st.number_input("Enter Kilogram Value")

        grams = value * 1000
        pounds = value * 2.20462

        st.success(f"{value} kg = {grams} g")
        st.success(f"{value} kg = {pounds} lbs")

    # TEMPERATURE
    elif conversion == "Temperature":

        c = st.number_input("Enter Celsius Value")

        f = (c * 9/5) + 32
        k = c + 273.15

        st.success(f"{c} °C = {f} °F")
        st.success(f"{c} °C = {k} K")

    # PRESSURE
    elif conversion == "Pressure":

        pa = st.number_input("Enter Pressure in Pascal")

        bar = pa / 100000
        psi = pa / 6895

        st.success(f"{pa} Pa = {bar} bar")
        st.success(f"{pa} Pa = {psi} psi")

# =========================
# FOOTER
# =========================

st.markdown("---")
st.caption("Mechanical Engineering Toolkit using Streamlit 🚀")
