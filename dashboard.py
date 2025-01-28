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
        "Overall company strategy and leadership",
        "Financial oversight, budgeting, and accounting",
        "Oversees SchoolsPLP Sales, Backbone, and EDS teams",
        "Manages operations, supports teams, and oversees curriculum",
        "Leads training, implementation, and support teams",
        "Manages online learning coordination",
        "Oversees content development and contractor collaboration",
        "Leads software development and product design teams",
        "Provides technical expertise and system architecture guidance",
        "Provides advanced educational support",
        "Manages technical and process integration",
        "Special projects and support initiatives",
        "Manages unique educational projects",
        "Conducts training for schools and staff",
        "Conducts training for schools and staff",
        "Develops and maintains company software",
        "Develops and maintains company software",
        "Leads UX/UI and product experience design",
        "Manages learning management system"
    ],
    "Reports To": [
        "Board of Directors", "CEO", "CEO", "CEO", "COO",
        "Director of Innovation & Partnerships", "COO", "COO",
        "COO (Consultant)", "Director of Educational Support", "Director of Educational Support",
        "Director of Educational Support", "Director of Educational Support",
        "Director of Educational Support", "Director of Educational Support",
        "Project Manager", "Project Manager", "Project Manager", "Project Manager"
    ],
    "Department": [
        "Leadership", "Leadership", "Innovation & Partnerships",
        "Operations", "Educational Support", "Virtual Learning",
        "Curriculum", "Software Development", "Consulting",
        "Support & Coaching", "Integration", "Education",
        "Special Projects", "Training", "Training",
        "Software Development", "Software Development",
        "Product Design", "LMS Administration"
    ]
}

# Convert to DataFrame
role_df = pd.DataFrame(role_data)

# Streamlit App Title
st.title("SchoolsPLP Organizational Dashboard")

# Dropdown Selection for Role (Without Numbers)
selected_role = st.selectbox("Select a Role:", role_df["Role"])

# Display Role Responsibilities
st.subheader("Role Responsibilities & Reporting Structure")
filtered_data = role_df[role_df["Role"] == selected_role]
st.write(filtered_data[["Role", "Responsibilities", "Reports To"]])

# Heatmap Visualization (WITHOUT NUMBERS)
st.subheader("🔍 Decision-Making Authority Heatmap")
fig, ax = plt.subplots(figsize=(8, 6))

# Assigning a heat level for visualization (all roles are assigned the same importance visually)
role_df["Heat Level"] = 1  # Placeholder since we're not displaying decision-making numbers

heatmap_data = role_df.pivot_table(index="Role", values="Heat Level", aggfunc="sum")

sns.heatmap(
    heatmap_data,
    annot=False,  # No numbers
    cmap="Blues",
    linewidths=0.5,
    cbar=True,
    ax=ax
)

st.pyplot(fig)

# Footer
st.markdown("💡 *Use the dropdown menu to explore roles and responsibilities!*")
