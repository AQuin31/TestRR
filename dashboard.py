import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define Role Responsibility Data
role_data = {
    "Role": [
        "BJ Dines (CEO)", "Leah Dines (CFO)", "Brian Snyder (Dir. Innovation & Partnerships)",
        "Josh Leitz (COO)", "LaRae Kendrick (Dir. Educational Support)", "Jeremy Gold (Dir. Virtual Learning)",
        "Kathe Arnold (Dir. Curriculum)", "Angeline Quinones (Project Manager)", "Micah Stetson (Software Consultant)",
        "Gordon Gower (Sr. Support & Coaching Lead)", "Kim Schneper (Support & Integration Lead)",
        "Kevin McCormick (Support & Education Lead)", "Gracie Perez (Special Projects Lead)",
        "Leslie King (Professional Trainer)", "Heather Caldwell (Professional Trainer)",
        "Richard Metze (Software Dev)", "Mayowa Akinyemi (Software Dev)",
        "Joanne Delphia (Sr. Product Designer)", "Seth Morris (LMS Admin)"
    ],
    "Responsibilities": [
        "CEO - Overall company strategy and leadership",
        "CFO - Financial oversight, budgeting, and accounting",
        "Director of Innovation & Partnerships - Oversees SchoolsPLP Sales, Backbone, and EDS teams",
        "COO - Manages operations, supports teams, and oversees curriculum",
        "Director of Educational Support - Leads training, implementation, and support teams",
        "Director of Virtual Learning - Manages online learning coordination",
        "Director of Curriculum - Oversees content development and contractor collaboration",
        "Project Manager - Leads software development and product design teams",
        "Software Consultant - Provides technical expertise and system architecture guidance",
        "Senior Support & Coaching Lead - Provides advanced educational support",
        "Support Specialist & Integration Lead - Manages technical and process integration",
        "Support Specialist & Education Lead - Special projects and support initiatives",
        "Special Projects Lead - Manages unique educational projects",
        "Professional Trainer - Conducts training for schools and staff",
        "Professional Trainer - Conducts training for schools and staff",
        "Software Developer - Develops and maintains company software",
        "Software Developer - Develops and maintains company software",
        "Senior Product Designer - Leads UX/UI and product experience design",
        "LMS Administrator - Manages learning management system"
    ],
    "Reports To": [
        "Board of Directors", "CEO", "CEO", "CEO", "COO",
        "Director of Innovation & Partnerships", "COO", "COO",
        "COO (Consultant)", "Director of Educational Support", "Director of Educational Support",
        "Director of Educational Support", "Director of Educational Support",
        "Director of Educational Support", "Director of Educational Support",
        "Project Manager", "Project Manager", "Project Manager", "Project Manager"
    ],
    "Decision-Making Authority": [10, 9, 8, 9, 8, 7, 7, 7, 6, 6, 5, 5, 5, 4, 4, 4, 4, 5, 4]
}

# Convert to DataFrame
role_df = pd.DataFrame(role_data)

# Streamlit App Title
st.title("📊 Interactive SchoolsPLP Organizational Dashboard")

# Dropdown Selection for Role
selected_role = st.selectbox("Select a Role:", role_df["Role"])

# Display Role Responsibilities
st.subheader("Role Responsibilities & Reporting Structure")
filtered_data = role_df[role_df["Role"] == selected_role]
st.write(filtered_data[["Role", "Responsibilities", "Reports To"]])

# Heatmap Visualization
st.subheader("🔍 Decision-Making Authority Heatmap")
fig, ax = plt.subplots(figsize=(8, 6))
heatmap_data = role_df.sort_values(by="Decision-Making Authority", ascending=False)
sns.heatmap(
    heatmap_data.set_index("Role")[["Decision-Making Authority"]],
    annot=True, cmap="Blues", linewidths=0.5, cbar=True, ax=ax
)
st.pyplot(fig)

# Footer
st.markdown("💡 *Use the dropdown menu to explore roles and responsibilities!*")
