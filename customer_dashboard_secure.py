# import streamlit as st
# import pandas as pd
# import os

# # ----------------------------------
# # Configuration
# # ----------------------------------
# EXCEL_FILE = "customers.xlsx"
# PROPERTY_OPTIONS = ["1 BHK", "2 BHK", "3 BHK", "4 BHK", "Villa", "Individual", "Builder"]
# SOURCE_OPTIONS = ["Google", "Instagram/FB", "Friends", "Testimonials","walkin"]

# # Employee credentials (you can add more)
# EMPLOYEE_CREDENTIALS = {
#     "admin": "admin123",
#     "srithi": "emp1@kognitive",
#     "medhini": "kognitive2025"
# }


# # ----------------------------------
# # Helper Functions
# # ----------------------------------
# def initialize_excel():
#     """Create Excel file if not exists."""
#     if not os.path.exists(EXCEL_FILE):
#         df = pd.DataFrame(columns=["Serial No", "Customer Name", "Mobile Number", "Address", "Property", "Status","Source" "Closure"])
#         df.to_excel(EXCEL_FILE, index=False)


# def load_data():
#     return pd.read_excel(EXCEL_FILE)


# def save_data(df):
#     df.to_excel(EXCEL_FILE, index=False)


# def login_page():
#     """Login UI"""
#     st.title("🔐 Employee Login - Kognitive Studios")
#     st.write("Please enter your credentials to continue.")

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if username in EMPLOYEE_CREDENTIALS and EMPLOYEE_CREDENTIALS[username] == password:
#             st.session_state.logged_in = True
#             st.session_state.username = username
#             st.success("✅ Login successful! Redirecting...")
#             st.rerun()

#         else:
#             st.error("❌ Invalid username or password")


# def customer_dashboard():
#     """Main dashboard after login"""
#     st.set_page_config(page_title="Kognitive Studios - Customer Database", layout="wide")

#     st.sidebar.title("👤 Logged in as:")
#     st.sidebar.info(st.session_state.username)
#     if st.sidebar.button("🚪 Logout"):
#         st.session_state.logged_in = False
#         st.rerun()


#     st.title("🏠 Kognitive Studios - Customer Data Entry")

#     st.markdown("### Enter Customer Details")
#     name = st.text_input("Customer Name")
#     mobile = st.text_input("Mobile Number")
#     address = st.text_area("Address")
#     property_type = st.selectbox("Property Type", PROPERTY_OPTIONS)
#     status = st.text_input("Status (e.g., Enquiry, Ongoing, Completed)")
#     Source = st.selectbox("Source", SOURCE_OPTIONS)
#     closure = st.text_input("Closure (optional)")

#     if st.button("💾 Save Customer"):
#         if name and mobile and address:
#             df = load_data()
#             serial_no = len(df) + 1
#             new_entry = {
#                 "Serial No": serial_no,
#                 "Customer Name": name,
#                 "Mobile Number": mobile,
#                 "Address": address,
#                 "Property": property_type,
#                 "Status": status,
#                 "Closure": closure
#             }
#             df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
#             save_data(df)
#             st.success(f"✅ Customer '{name}' added successfully!")
#         else:
#             st.error("Please fill in all required fields (Name, Mobile, Address).")

#     st.markdown("---")
#     st.markdown("### 📋 Customer Database")
#     if os.path.exists(EXCEL_FILE):
#         df = load_data()
#         st.dataframe(df, use_container_width=True)
#     else:
#         st.info("No customer data found yet. Add a new entry above.")


# # ----------------------------------
# # Main App
# # ----------------------------------
# def main():
#     initialize_excel()

#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False

#     if st.session_state.logged_in:
#         customer_dashboard()
#     else:
#         login_page()


# if __name__ == "__main__":
#     main()

#############################################################below code is working and golden code########################################


# import streamlit as st
# import pandas as pd
# import os
# from datetime import datetime

# # ----------------------------------
# # Configuration
# # ----------------------------------
# EXCEL_FILE = "customers.xlsx"
# PROPERTY_OPTIONS = ["1 BHK", "2 BHK", "3 BHK", "4 BHK", "Villa", "Individual", "Builder"]
# SOURCE_OPTIONS = ["Google", "Instagram/FB", "Friends", "Testimonials", "Walk-in"]

# # Employee credentials
# EMPLOYEE_CREDENTIALS = {
#     "admin": "admin123",
#     "srithi": "emp1@kognitive",
#     "medhini": "kognitive2025"
# }


# # ----------------------------------
# # Helper Functions
# # ----------------------------------
# def initialize_excel():
#     """Create Excel file if it does not exist."""
#     if not os.path.exists(EXCEL_FILE):
#         df = pd.DataFrame(columns=[
#             "Serial No", "Timestamp", "Employee Name", "Customer Name", "Mobile Number",
#             "Address", "Property", "Status", "Source", "Closure"
#         ])
#         df.to_excel(EXCEL_FILE, index=False)


# def load_data():
#     return pd.read_excel(EXCEL_FILE)


# def save_data(df):
#     df.to_excel(EXCEL_FILE, index=False)


# # ----------------------------------
# # Login Page
# # ----------------------------------
# def login_page():
#     st.title("🔐 Employee Login - Kognitive Studios")
#     st.write("Please enter your credentials to continue.")

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if username in EMPLOYEE_CREDENTIALS and EMPLOYEE_CREDENTIALS[username] == password:
#             st.session_state.logged_in = True
#             st.session_state.username = username
#             st.success("✅ Login successful!")
#             st.rerun()
#         else:
#             st.error("❌ Invalid username or password")


# # ----------------------------------
# # Employee Dashboard
# # ----------------------------------
# def employee_dashboard():
#     """Employee dashboard — only data entry"""
#     st.title("🏠 Kognitive Studios - Customer Entry Form")
#     st.sidebar.title("👤 Logged in as:")
#     st.sidebar.info(st.session_state.username)
#     if st.sidebar.button("🚪 Logout"):
#         st.session_state.logged_in = False
#         st.rerun()

#     # Input fields
#     name = st.text_input("Customer Name")
#     mobile = st.text_input("Mobile Number")
#     address = st.text_area("Address")
#     property_type = st.selectbox("Property Type", PROPERTY_OPTIONS)
#     source = st.selectbox("Source", SOURCE_OPTIONS)
#     status = st.text_input("Status (e.g., Enquiry, Ongoing, Completed)")
#     closure = st.text_input("Closure (optional)")

#     if st.button("💾 Submit"):
#         if name and mobile and address:
#             df = load_data()
#             serial_no = len(df) + 1
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             employee_name = st.session_state.username  # Auto-fill employee name

#             new_entry = {
#                 "Serial No": serial_no,
#                 "Timestamp": timestamp,
#                 "Employee Name": employee_name,
#                 "Customer Name": name,
#                 "Mobile Number": mobile,
#                 "Address": address,
#                 "Property": property_type,
#                 "Status": status,
#                 "Source": source,
#                 "Closure": closure
#             }

#             df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
#             save_data(df)

#             st.success(f"✅ Customer '{name}' details submitted successfully!")
#             st.info(f"Recorded by: **{employee_name}** at {timestamp}")
#         else:
#             st.error("⚠️ Please fill in all required fields (Name, Mobile, Address).")


# # ----------------------------------
# # Admin Dashboard
# # ----------------------------------
# def admin_dashboard():
#     """Admin view — can see and download all data"""
#     st.title("📊 Admin Dashboard - Kognitive Studios")
#     st.sidebar.title("👤 Logged in as:")
#     st.sidebar.info("Admin")
#     if st.sidebar.button("🚪 Logout"):
#         st.session_state.logged_in = False
#         st.rerun()

#     st.subheader("📋 Customer Database")

#     if os.path.exists(EXCEL_FILE):
#         df = load_data()
#         st.dataframe(df, use_container_width=True)

#         # Download option
#         with open(EXCEL_FILE, "rb") as file:
#             st.download_button(
#                 label="📥 Download Customer Data (Excel)",
#                 data=file,
#                 file_name="customers.xlsx",
#                 mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#             )
#     else:
#         st.info("No data available yet.")


# # ----------------------------------
# # Main App Logic
# # ----------------------------------
# def main():
#     st.set_page_config(page_title="Kognitive Studios - Dashboard", layout="wide")
#     initialize_excel()

#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False

#     if st.session_state.logged_in:
#         if st.session_state.username == "admin":
#             admin_dashboard()
#         else:
#             employee_dashboard()
#     else:
#         login_page()


# if __name__ == "__main__":
#     main()


# def save_data(df):
#     try:
#         # Try saving to the same file
#         df.to_excel(EXCEL_FILE, index=False)
#     except PermissionError:
#         # If Excel file is open, save to a temporary backup
#         backup_file = f"customers_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
#         df.to_excel(backup_file, index=False)
#         st.warning(f"⚠️ Could not save to {EXCEL_FILE} because it’s open. Data saved to backup file: {backup_file}")

##############################################################################################################################


# import streamlit as st
# import pandas as pd
# import gspread
# from google.oauth2.service_account import Credentials
# from datetime import datetime

# # ----------------------------------
# # Configuration
# # ----------------------------------
# SHEET_NAME = "Kognitive_Customers"
# WORKSHEET_NAME = "customers"
# SERVICE_ACCOUNT_FILE = "service_account.json"

# PROPERTY_OPTIONS = ["1 BHK", "2 BHK", "3 BHK", "4 BHK", "Villa", "Individual", "Builder"]
# SOURCE_OPTIONS = ["Google", "Instagram/FB", "Friends", "Testimonials", "Walk-in"]

# EMPLOYEE_CREDENTIALS = {
#     "admin": "admin123",
#     "srithi": "emp1@kognitive",
#     "medhini": "kognitive2025"
# }

# # ----------------------------------
# # Google Sheets Connection
# # ----------------------------------
# def get_sheet():
#     scopes = [
#         "https://www.googleapis.com/auth/spreadsheets",
#         "https://www.googleapis.com/auth/drive"
#     ]
#     creds = Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=scopes
#     )
#     client = gspread.authorize(creds)
#     sheet = client.open(SHEET_NAME).worksheet(WORKSHEET_NAME)
#     return sheet


# def load_data():
#     sheet = get_sheet()
#     data = sheet.get_all_records()
#     return pd.DataFrame(data)


# def save_entry(entry):
#     sheet = get_sheet()
#     existing_rows = sheet.get_all_values()
#     serial_no = len(existing_rows)  # header already counted
#     entry["Serial No"] = serial_no
#     sheet.append_row(list(entry.values()))


# # ----------------------------------
# # Login Page
# # ----------------------------------
# def login_page():
#     st.title("🔐 Employee Login - Kognitive Studios")

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if username in EMPLOYEE_CREDENTIALS and EMPLOYEE_CREDENTIALS[username] == password:
#             st.session_state.logged_in = True
#             st.session_state.username = username
#             st.success("✅ Login successful!")
#             st.rerun()
#         else:
#             st.error("❌ Invalid credentials")


# # ----------------------------------
# # Employee Dashboard
# # ----------------------------------
# def employee_dashboard():
#     st.title("🏠 Kognitive Studios - Customer Entry Form")

#     st.sidebar.info(f"👤 Logged in as: {st.session_state.username}")
#     if st.sidebar.button("🚪 Logout"):
#         st.session_state.logged_in = False
#         st.rerun()

#     name = st.text_input("Customer Name")
#     mobile = st.text_input("Mobile Number")
#     address = st.text_area("Address")
#     property_type = st.selectbox("Property Type", PROPERTY_OPTIONS)
#     source = st.selectbox("Source", SOURCE_OPTIONS)
#     status = st.text_input("Status (Enquiry / Ongoing / Completed)")
#     closure = st.text_input("Closure (optional)")

#     if st.button("💾 Submit"):
#         if name and mobile and address:
#             entry = {
#                 "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                 "Employee Name": st.session_state.username,
#                 "Customer Name": name,
#                 "Mobile Number": mobile,
#                 "Address": address,
#                 "Property": property_type,
#                 "Status": status,
#                 "Source": source,
#                 "Closure": closure
#             }

#             save_entry(entry)

#             st.success(f"✅ Customer '{name}' saved successfully")
#         else:
#             st.error("⚠️ Name, Mobile & Address are required")


# # ----------------------------------
# # Admin Dashboard
# # ----------------------------------
# def admin_dashboard():
#     st.title("📊 Admin Dashboard - Kognitive Studios")

#     st.sidebar.info("👤 Admin")
#     if st.sidebar.button("🚪 Logout"):
#         st.session_state.logged_in = False
#         st.rerun()

#     df = load_data()
#     st.dataframe(df, use_container_width=True)

#     csv = df.to_csv(index=False).encode("utf-8")
#     st.download_button(
#         "📥 Download Customer Data (CSV)",
#         csv,
#         "customers.csv",
#         "text/csv"
#     )


# # ----------------------------------
# # Main App
# # ----------------------------------
# def main():
#     st.set_page_config(page_title="Kognitive Studios", layout="wide")

#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False

#     if st.session_state.logged_in:
#         if st.session_state.username == "admin":
#             admin_dashboard()
#         else:
#             employee_dashboard()
#     else:
#         login_page()


# if __name__ == "__main__":
#     main()
##########################################################above code has alignment issue with column name mismatch##################################


# import streamlit as st
# import pandas as pd
# import gspread
# from google.oauth2.service_account import Credentials
# from datetime import datetime

# # ----------------------------------
# # Configuration
# # ----------------------------------
# SHEET_NAME = "Kognitive_Customers"
# WORKSHEET_NAME = "customers"
# SERVICE_ACCOUNT_FILE = "service_account.json"

# PROPERTY_OPTIONS = ["1 BHK", "2 BHK", "3 BHK", "4 BHK", "Villa", "Individual", "Builder"]
# SOURCE_OPTIONS = ["Google", "Instagram/FB", "Friends", "Testimonials", "Walk-in"]

# EMPLOYEE_CREDENTIALS = {
#     "admin": "admin123",
#     "srithi": "emp1@kognitive",
#     "medhini": "kognitive2025"
# }

# # ----------------------------------
# # Google Sheets Connection
# # ----------------------------------
# def get_sheet():
#     scopes = [
#         "https://www.googleapis.com/auth/spreadsheets",
#         "https://www.googleapis.com/auth/drive"
#     ]
#     creds = Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=scopes
#     )
#     client = gspread.authorize(creds)
#     sheet = client.open(SHEET_NAME).worksheet(WORKSHEET_NAME)
#     return sheet


# def load_data():
#     sheet = get_sheet()
#     data = sheet.get_all_records()
#     return pd.DataFrame(data)


# # ✅ FIXED FUNCTION (ONLY CHANGE)
# def save_entry(entry):
#     sheet = get_sheet()
#     existing_rows = sheet.get_all_values()
#     serial_no = len(existing_rows)  # header already counted

#     row = [
#         serial_no,                        # Serial No
#         entry["Timestamp"],              # Timestamp
#         entry["Employee Name"],          # Employee Name
#         entry["Customer Name"],          # Customer Name
#         entry["Mobile Number"],          # Mobile Number
#         entry["Address"],                # Address
#         entry["Property"],               # Property
#         entry["Status"],                 # Status
#         entry["Source"],                 # Source
#         entry["Closure"]                 # Closure
#     ]

#     sheet.append_row(row, value_input_option="USER_ENTERED")


# # ----------------------------------
# # Login Page
# # ----------------------------------
# def login_page():
#     st.title("🔐 Employee Login - Kognitive Studios")

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if username in EMPLOYEE_CREDENTIALS and EMPLOYEE_CREDENTIALS[username] == password:
#             st.session_state.logged_in = True
#             st.session_state.username = username
#             st.success("✅ Login successful!")
#             st.rerun()
#         else:
#             st.error("❌ Invalid credentials")


# # ----------------------------------
# # Employee Dashboard
# # ----------------------------------
# def employee_dashboard():
#     st.title("🏠 Kognitive Studios - Customer Entry Form")

#     st.sidebar.info(f"👤 Logged in as: {st.session_state.username}")
#     if st.sidebar.button("🚪 Logout"):
#         st.session_state.logged_in = False
#         st.rerun()

#     name = st.text_input("Customer Name")
#     mobile = st.text_input("Mobile Number")
#     address = st.text_area("Address")
#     property_type = st.selectbox("Property Type", PROPERTY_OPTIONS)
#     source = st.selectbox("Source", SOURCE_OPTIONS)
#     status = st.text_input("Status (Enquiry / Ongoing / Completed)")
#     closure = st.text_input("Closure (optional)")

#     if st.button("💾 Submit"):
#         if name and mobile and address:
#             entry = {
#                 "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                 "Employee Name": st.session_state.username,
#                 "Customer Name": name,
#                 "Mobile Number": mobile,
#                 "Address": address,
#                 "Property": property_type,
#                 "Status": status,
#                 "Source": source,
#                 "Closure": closure
#             }

#             save_entry(entry)

#             st.success(f"✅ Customer '{name}' saved successfully")
#         else:
#             st.error("⚠️ Name, Mobile & Address are required")


# # ----------------------------------
# # Admin Dashboard
# # ----------------------------------
# def admin_dashboard():
#     st.title("📊 Admin Dashboard - Kognitive Studios")

#     st.sidebar.info("👤 Admin")
#     if st.sidebar.button("🚪 Logout"):
#         st.session_state.logged_in = False
#         st.rerun()

#     df = load_data()
#     st.dataframe(df, use_container_width=True)

#     csv = df.to_csv(index=False).encode("utf-8")
#     st.download_button(
#         "📥 Download Customer Data (CSV)",
#         csv,
#         "customers.csv",
#         "text/csv"
#     )


# # ----------------------------------
# # Main App
# # ----------------------------------
# def main():
#     st.set_page_config(page_title="Kognitive Studios", layout="wide")

#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False

#     if st.session_state.logged_in:
#         if st.session_state.username == "admin":
#             admin_dashboard()
#         else:
#             employee_dashboard()
#     else:
#         login_page()


# if __name__ == "__main__":
#     main()




#########################################above cde is golden and working#####################################################

import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# ----------------------------------
# Configuration
# ----------------------------------
SHEET_NAME = "Kognitive_Customers"
WORKSHEET_NAME = "customers"
SERVICE_ACCOUNT_FILE = "service_account.json"

PROPERTY_OPTIONS = ["1 BHK", "2 BHK", "3 BHK", "4 BHK", "Villa", "Individual", "Builder"]
SOURCE_OPTIONS = ["Google", "Instagram/FB", "Friends", "Testimonials", "Walk-in"]

EMPLOYEE_CREDENTIALS = {
    "admin": "admin123",
    "srithi": "emp1@kognitive",
    "medhini": "kognitive2025"
}

STATUS_OPTIONS = ["Enquiry", "Ongoing", "Completed", "Closed"]

# ----------------------------------
# Google Sheets Connection
# ----------------------------------
def get_sheet():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=scopes
    )

    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).worksheet(WORKSHEET_NAME)
    return sheet


def load_data():
    sheet = get_sheet()
    data = sheet.get_all_records()
    return pd.DataFrame(data)


def mobile_exists(mobile):
    sheet = get_sheet()
    mobiles = sheet.col_values(5)[1:]  # Mobile Number column (skip header)
    return mobile in mobiles


def save_entry(entry):
    sheet = get_sheet()
    existing_rows = sheet.get_all_values()
    serial_no = len(existing_rows)

    row = [
        serial_no,
        entry["Timestamp"],
        entry["Employee Name"],
        entry["Customer Name"],
        entry["Mobile Number"],
        entry["Address"],
        entry["Property"],
        entry["Status"],
        entry["Source"],
        entry["Closure"]
    ]

    sheet.append_row(row, value_input_option="USER_ENTERED")


# ----------------------------------
# Login Page
# ----------------------------------
def login_page():
    st.title("🔐 Employee Login - Kognitive Studios")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in EMPLOYEE_CREDENTIALS and EMPLOYEE_CREDENTIALS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("✅ Login successful!")
            st.rerun()
        else:
            st.error("❌ Invalid credentials")


# ----------------------------------
# Employee Dashboard
# ----------------------------------
def employee_dashboard():
    st.title("🏠 Kognitive Studios - Customer Entry Form")

    st.sidebar.info(f"👤 Logged in as: {st.session_state.username}")
    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    name = st.text_input("Customer Name")
    mobile = st.text_input("Mobile Number")
    address = st.text_area("Address")
    property_type = st.selectbox("Property Type", PROPERTY_OPTIONS)
    source = st.selectbox("Source", SOURCE_OPTIONS)
    status = st.selectbox("Status", STATUS_OPTIONS)
    closure = st.text_input("Closure (optional)")

    if st.button("💾 Submit"):
        if not (name and mobile and address):
            st.error("⚠️ Name, Mobile & Address are required")
            return

        if mobile_exists(mobile):
            st.warning("⚠️ This mobile number already exists!")
            return

        entry = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Employee Name": st.session_state.username,
            "Customer Name": name,
            "Mobile Number": mobile,
            "Address": address,
            "Property": property_type,
            "Status": status,
            "Source": source,
            "Closure": closure
        }

        save_entry(entry)
        st.success(f"✅ Customer '{name}' saved successfully")


# ----------------------------------
# Admin Dashboard
# ----------------------------------
def admin_dashboard():
    st.title("📊 Admin Dashboard - Kognitive Studios")

    st.sidebar.info("👤 Admin")
    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    df = load_data()

    employee_filter = st.selectbox(
        "Filter by Employee",
        ["All"] + sorted(df["Employee Name"].unique().tolist())
    )

    if employee_filter != "All":
        df = df[df["Employee Name"] == employee_filter]

    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "📥 Download Filtered Data (CSV)",
        csv,
        "customers.csv",
        "text/csv"
    )


# ----------------------------------
# Main App
# ----------------------------------
def main():
    st.set_page_config(page_title="Kognitive Studios", layout="wide")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        if st.session_state.username == "admin":
            admin_dashboard()
        else:
            employee_dashboard()
    else:
        login_page()


if __name__ == "__main__":
    main()
#https://customerdashboardsecurepy-bctzt2zunuzdarxoqrszaj.streamlit.app/