import streamlit as st

# Initialize session state for tracking steps if not already initialized
if 'identity_step' not in st.session_state:
    st.session_state['identity_step'] = 1

if 'address_step' not in st.session_state:
    st.session_state['address_step'] = 1

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Proof of Identity", "Proof of Address"])

if page == "Proof of Identity":
    st.title("Proof of Identity")

    # Step 1: Country of Document Issuance
    if st.session_state['identity_step'] == 1:
        st.subheader("Step 1: In which country was your document issued?")
        country = st.selectbox("Select the country", ["Select", "United States", "Canada", "United Kingdom", "Australia", "Other"])

        if country != "Select":
            st.write("Country of Document Issuance: ", country)

        if st.button("Next", key="next_step_1"):
            if country != "Select":
                st.session_state['identity_step'] = 2  # Move to Step 2: Select Document Type
                st.experimental_rerun()  # Rerun to show Step 2
            else:
                st.error("Please select a country before proceeding.")

    # Step 2: Select the Type of Document
    if st.session_state['identity_step'] == 2:
        st.subheader("Step 2: Select the type of document you wish to upload")

        doc_type = st.selectbox("Select the type of document", ["Select", "Passport", "Identity Card", "Driving License"])

        if doc_type == "Identity Card":
            st.session_state['identity_step'] = 3  # Move to Identity Card Details Page
            st.experimental_rerun()  # Rerun to go to Identity Card details page
        elif doc_type == "Passport":
            # Directly go to "DONE" message if "Passport" is selected
            st.session_state['identity_step'] = 7  # Set identity_step to "DONE"
            st.experimental_rerun()  # Rerun to show "DONE" message
        elif doc_type == "Driving License":
            st.session_state['identity_step'] = 5  # Move to Driving License Upload Page
            st.experimental_rerun()  # Rerun to go to Driving License upload page
        else:
            st.error("Please select a document type.")

        # Back Button to Step 1
        if st.button("Back to Step 1: Select Country"):
            st.session_state['identity_step'] = 1  # Go back to Step 1
            st.experimental_rerun()  # Rerun to go back to Step 1

    # Identity Card Document Upload (Step 3)
    if st.session_state['identity_step'] == 3:
        st.subheader("Step 3: Upload your Identity Card Document")
        st.text("Please upload the front and back sides of your Identity Card.")

        # File Upload for Identity Card (front)
        front_ic = st.file_uploader("Upload the front of your Identity Card", type=["jpeg", "jpg", "png", "pdf", "gif"])

        # File Upload for Identity Card (back)
        back_ic = st.file_uploader("Upload the back of your Identity Card", type=["jpeg", "jpg", "png", "pdf", "gif"])

        if front_ic and back_ic:
            st.write("Identity Card document uploaded successfully!")
            if st.button("Finish", key="finish_ic"):
                st.session_state['identity_step'] = 6  # Proceed to success page
                st.experimental_rerun()  # Rerun to show success message

        # Back Button to Step 2: Select Document Type
        if st.button("Back to Step 2: Select Document Type"):
            st.session_state['identity_step'] = 2  # Go back to Step 2
            st.experimental_rerun()  # Rerun to go back to Step 2

    # Driving License Document Upload (Step 5)
    if st.session_state['identity_step'] == 5:
        st.subheader("Step 5: Upload your Driving License Document")
        st.text("Please upload the front and back sides of your Driving License.")

        # File Upload for Driving License (front)
        front_dl = st.file_uploader("Upload the front of your Driving License", type=["jpeg", "jpg", "png", "pdf", "gif"])

        # File Upload for Driving License (back)
        back_dl = st.file_uploader("Upload the back of your Driving License", type=["jpeg", "jpg", "png", "pdf", "gif"])

        if front_dl and back_dl:
            st.write("Driving License document uploaded successfully!")
            if st.button("Finish", key="finish_dl"):
                st.session_state['identity_step'] = 6  # Proceed to success page
                st.experimental_rerun()  # Rerun to show success message

        # Back Button to Step 2: Select Document Type
        if st.button("Back to Step 2: Select Document Type"):
            st.session_state['identity_step'] = 2  # Go back to Step 2
            st.experimental_rerun()  # Rerun to go back to Step 2

    # DONE Page (Step 7)
    if st.session_state['identity_step'] == 7:
        st.subheader("DONE!")
        st.success("You have selected 'Passport' as your document type. No further action is required at this moment.")
        st.write("Thank you for completing the selection!")

elif page == "Proof of Address":
    st.title("Proof of Address")

    # Step 1: Address Input
    st.subheader("Step 1/2: Enter your address")
    address_line_1 = st.text_input("First line of address")
    address_line_2 = st.text_input("Second line of address")
    town_city = st.selectbox("Town/City", ["Select", "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Other"])
    state_province = st.selectbox("State/Province", ["Select", "California", "Texas", "New York", "Florida", "Illinois", "Other"])
    postal_code = st.text_input("Postal/ZIP code", max_chars=10)

    if st.button("Next", key="address_next"):
        if address_line_1 and town_city != "Select" and state_province != "Select":
            st.session_state['address_step'] = 2
            st.experimental_rerun()  # Rerun to show the next step
        else:
            st.error("Please fill in all required address fields before proceeding.")

    # Step 2: Document Submission
    if st.session_state.get('address_step') == 2:
        st.subheader("Step 2/2: Document Submission")
        st.write("We accept only the following documents as proof of address. The document must be issued within the last 12 months and include your full name and address:")
        st.write("• Utility bill: Electricity, water, gas, or landline phone bill.")
        st.write("• Financial, legal, or government: Recent bank statement, affidavit, or government-issued letter.")
        st.write("• Tenancy agreement: Valid and current agreement.")

        doc_type_address = st.selectbox("Select the type of document", 
                                        ["Select", "Utility Bill", "Bank Statement", "Affidavit", "Government-issued Letter", "Tenancy Agreement"])
        file = st.file_uploader("Upload file", type=["jpeg", "jpg", "png", "pdf", "gif"])

        if file:
            st.write("Document uploaded successfully!")
        
        if st.button("Submit", key="address_submit"):
            st.write("Your proof of address submission is complete.")
