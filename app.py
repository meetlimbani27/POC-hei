import streamlit as st
from search_vendors import search_similar_vendors
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import logging
import os

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Set page title
st.title("Vendor Search POC")

# SendGrid API Key
SENDGRID_API_KEY = 'SG.lPE4yV8YQfyoXXwYxxxx.8CgXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

def send_email_sendgrid(vendor_info):
    """Send email using SendGrid"""
    try:
        logger.debug(f"Attempting to send email via SendGrid to: {vendor_info['email']}")
        
        message = Mail(
            from_email='testapp.windsurf@gmail.com',
            to_emails=vendor_info['email'],
            subject=f"Test Email for Vendor: {vendor_info['vendor_id']}",
            plain_text_content=f"""
            Hello!
            
            This is a test email for:
            Vendor ID: {vendor_info['vendor_id']}
            Email: {vendor_info['email']}
            
            Best regards,
            Your Vendor Search App
            """
        )
        
        logger.debug("Initializing SendGrid client...")
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        
        logger.debug("Sending email...")
        response = sg.send(message)
        
        logger.debug(f"SendGrid Response Code: {response.status_code}")
        logger.debug(f"SendGrid Response Headers: {response.headers}")
        logger.debug(f"SendGrid Response Body: {response.body}")
        
        if response.status_code in [200, 201, 202]:
            logger.info(f"Email sent successfully via SendGrid to {vendor_info['email']}")
            return True, "Email sent successfully via SendGrid"
        else:
            error_msg = f"SendGrid returned status code: {response.status_code}"
            logger.error(error_msg)
            return False, error_msg
            
    except Exception as e:
        error_msg = f"Failed to send email via SendGrid: {str(e)}"
        logger.error(error_msg)
        return False, error_msg

# Create a text input box
search_query = st.text_input("Enter your search query:", key="search_box")

# Debug info display
debug_container = st.empty()

# Add a search button
if st.button("Search"):
    if search_query:
        try:
            results = search_similar_vendors(search_query, limit=15)
            
            if results:
                for idx, result in enumerate(results, 1):
                    with st.expander(f"Match #{idx} - Score: {result['similarity_score']:.4f}"):
                        st.write(f"**Vendor ID:** {result['vendor_id']}")
                        st.write(f"**Email:** {result['email']}")
                        st.write("**Description:**")
                        st.write(result['description'])
                        
                        # Add send email button for each vendor
                        if st.button(f"Send Email to {result['email']}", key=f"email_btn_{idx}"):
                            with st.spinner("Sending email..."):
                                success, message = send_email_sendgrid(result)
                                if success:
                                    st.success(message)
                                else:
                                    st.error(message)
                                    
                        # Show debug logs for this vendor
                        with st.expander("Show email debug logs"):
                            st.code(f"Target Email: {result['email']}\nCheck the terminal for detailed logs")
            else:
                st.info("No matching vendors found.")
                
        except Exception as e:
            st.error(f"Error performing search: {str(e)}")
            logger.error(f"Search error: {str(e)}")
    else:
        st.warning("Please enter a search query.")
