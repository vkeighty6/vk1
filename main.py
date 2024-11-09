# Step 1: Country of Document Issuance and Identification Number
if st.session_state['identity_step'] == 1:
    st.subheader("Step 1: In which country was your document issued?")
    country = st.selectbox("Select the country",
                           ["Select", "United States", "Canada", "United Kingdom", "Australia", "Other"])

    # Add IDENTIFICATION NUMBER text field
    identification_number = st.text_input("Identification Number", placeholder="Enter your identification number")

    # Add FULL NAME as Identification Document text field
    full_name = st.text_input("Full Name as in Identification Document", placeholder="Enter your full name")

    # Check if country is selected before showing it
    if country != "Select":
        st.write("Country of Document Issuance: ", country)

    if identification_number:
        st.write("Identification Number: ", identification_number)

    if full_name:
        st.write("Full Name: ", full_name)

    if st.button("Next", key="next_step_1"):
        if country != "Select" and identification_number and full_name:
            st.session_state['identity_step'] = 2  # Move to Step 2: Select Document Type
            # No need for experimental rerun here either
        else:
            st.error("Please select a country, provide your identification number, and your full name before proceeding.")
