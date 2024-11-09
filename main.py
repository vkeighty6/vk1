import streamlit as st

# Initialize session state for tracking steps
if 'identity_step' not in st.session_state:
    st.session_state['identity_step'] = 1

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Proof of Identity", "Proof of Address"])

if page == "Proof of Identity":
    st.title("Proof of Identity")

# Step 1: Country of Document Issuance
if st.session_state['identity_step'] == 1:
    st.subheader("Step 1: In which country was your document issued?")
    country = st.selectbox("Select the country",
                           ["Select", "United States", "Canada", "United Kingdom", "Australia", "Other"])

    # Add IDENTIFICATION NUMBER text field
    identification_number = st.text_input("IDENTIFICATION NUMBER", placeholder="Enter your identification number")

    # Check if country is selected before showing it
    if country != "Select":
        st.write("Country of Document Issuance: ", country)

    # Check if identification number is provided
    if identification_number:
        st.write("Identification Number: ", identification_number)

    if st.button("Next", key="next_step_1"):
        if country != "Select" and identification_number:
            st.session_state['identity_step'] = 2  # Move to Step 2: Select Document Type
            st.experimental_rerun()  # Rerun to hide Step 1 and show Step 2
        else:
            st.error("Please select a country and provide your identification number before proceeding.")


    # Step 2: Document Submission
    if st.session_state.get('address_step') == 2:
        st.subheader("Step 2/2: Document Submission")
        st.write(
            "We accept only the following documents as proof of address. The document must be issued within the last 12 months and include your full name and address:")
        st.write("• Utility bill: Electricity, water, gas, or landline phone bill.")
        st.write("• Financial, legal, or government: Recent bank statement, affidavit, or government-issued letter.")
        st.write("• Tenancy agreement: Valid and current agreement.")

        doc_type_address = st.selectbox("Select the type of document",
                                        ["Select", "Utility Bill", "Bank Statement", "Affidavit",
                                         "Government-issued Letter", "Tenancy Agreement"])
        st.file_uploader("Upload file", type=["jpeg", "jpg", "png", "pdf", "gif"])

        if st.button("Submit", key="address_submit"):
            st.write("Your proof of address submission is complete.")
