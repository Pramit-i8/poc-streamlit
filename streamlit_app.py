import streamlit as st

# Page config
st.set_page_config(page_title="Disney AP3", layout="wide")

# Disney-style blue header
st.markdown("""
    <div style="background-color:#0072CE; padding:15px 30px; color:white; font-size:22px; font-weight:bold; border-radius: 6px 6px 0 0;">
        Antipiracy Property Protection Platform (AP3)
    </div>
    <div style="background-color:#E3EAF2; padding:10px 30px; display:flex; gap:15px; border-radius: 0 0 6px 6px;">
        <div style="background-color:lightgray; padding:8px 16px; border-radius:5px; color:gray; cursor:not-allowed;">File Mapping</div>
        <div style="background-color:lightgray; padding:8px 16px; border-radius:5px; color:gray; cursor:not-allowed;">Define Fields</div>
        <div style="color:purple; padding-top:5px;">Can’t click on these </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("### Upload one or more files with the same source, timezone, mapping, and upload type.")

# Upload Type section
st.markdown("""
<div style="border:1px solid #ddd; padding:15px; border-radius:6px; margin-bottom:20px;">
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    st.checkbox("Production Data", value=True, disabled=False)
with col2:
    st.checkbox("Test Data", value=False, disabled=True)
    st.checkbox("Validate Mapping", value=False, disabled=True)
    st.checkbox("Create Mapping", value=False, disabled=True)

# Source / Mapping / Timezone section
st.selectbox("Source", ["Mediastory Korea"], index=0, disabled=False)

col3, col4 = st.columns(2)
with col3:
    st.selectbox("Mapping", ["[Default]"], index=0, disabled=True)
with col4:
    st.selectbox("Timezone Override", ["[Default]"], index=0, disabled=True)

st.markdown("<span style='color: purple;'>Can’t select an option other than default</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Upload box
st.markdown("""
<div style="border: 2px dashed #bbb; border-radius: 6px; padding: 20px; text-align: center; background-color: #f9f9f9;">
    <p><strong>Drag and drop files here</strong></p>
    <p style="font-size: 13px; color: gray;">Limit 200MB per file</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Uploaded Files")
st.table({
    "File Name": ["antipiracy_msk_03302025_ghf8.csv", "antipiracy_03292025_ewh4.csv"],
    "Validation Status": ["Validation In Progress", "Validation Complete - Link"],
    "Rows": [1216, 230]
})
