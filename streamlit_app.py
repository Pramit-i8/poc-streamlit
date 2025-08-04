import streamlit as st

st.title("Antipiracy Property Protection Platform (AP3)")

# Simulated Top Bar Navigation
st.markdown("###")
st.markdown(
    """
    <div style="display: flex; gap: 10px;">
        <div style="background-color: #e0e0e0; color: gray; padding: 8px 16px; border-radius: 5px; cursor: not-allowed;">
            File Mapping
        </div>
        <div style="background-color: #e0e0e0; color: gray; padding: 8px 16px; border-radius: 5px; cursor: not-allowed;">
            Define Fields
        </div>
    </div>
    <p style="color: purple; font-size: 14px;">Can’t click on these? OR - can click but then can’t do anything on page?</p>
    """,
    unsafe_allow_html=True
)

# Upload Section
st.markdown("#### Upload one or more files with the same source, timezone, mapping, and upload type.")

col1, col2 = st.columns([1, 2])
with col1:
    st.checkbox("Production Data", value=True, disabled=False)
with col2:
    st.checkbox("Test Data", value=False, disabled=True)
    st.checkbox("Validate Mapping", value=False, disabled=True)
    st.checkbox("Create Mapping", value=False, disabled=True)

# Source (enabled)
st.selectbox("Source", ["Mediastory Korea"], index=0, disabled=False)

# Mapping and Timezone (disabled)
st.selectbox("Mapping", ["[Default]"], index=0, disabled=True)
st.selectbox("Timezone Override", ["[Default]"], index=0, disabled=True)

st.markdown("<p style='color: purple;'>Can’t select an option other than default</p>", unsafe_allow_html=True)

# File Upload (simulated)
st.file_uploader("Choose a file", type=["csv"], disabled=False)

# File List (static)
st.markdown("#### Uploaded Files")
st.table({
    "File Name": ["antipiracy_msk_03302025_ghf8.csv", "antipiracy_03292025_ewh4.csv"],
    "Validation Status": ["Validation In Progress", "Validation Complete - Link"],
    "Rows": [1216, 230]
})
