import streamlit as st
import graphviz
import pandas as pd

# Set page configuration
st.set_page_config(page_title="SchoolsPLP Organization Chart", layout="wide")

def create_org_data():
    return {
        "Board of Directors": [],
        "BJ Dines (CEO)": ["Board of Directors"],
        "Leah Dines (CFO)": ["BJ Dines (CEO)"],
        "Josh Leitz (COO)": ["BJ Dines (CEO)"],
        "Brian Snyder (Dir. Innovation & Partnerships)": ["BJ Dines (CEO)"],
        "LaRae Kendrick (Dir. Educational Support)": ["Josh Leitz (COO)"],
        "Jeremy Gold (Dir. Virtual Learning)": ["Brian Snyder (Dir. Innovation & Partnerships)"],
        "Kathe Arnold (Dir. Curriculum)": ["Josh Leitz (COO)"],
        "Angeline Quinones (Project Manager)": ["Josh Leitz (COO)"],
        "Micah Stetson (Software Consultant)": ["Josh Leitz (COO)"],
        "Gordon Gower (Sr. Support & Coaching Lead)": ["LaRae Kendrick (Dir. Educational Support)"],
        "Kim Schneper (Support & Integration Lead)": ["LaRae Kendrick (Dir. Educational Support)"],
        "Kevin McCormick (Support & Education Lead)": ["LaRae Kendrick (Dir. Educational Support)"],
        "Gracie Perez (Special Projects Lead)": ["LaRae Kendrick (Dir. Educational Support)"],
        "Leslie King (Professional Trainer)": ["LaRae Kendrick (Dir. Educational Support)"],
        "Heather Caldwell (Professional Trainer)": ["LaRae Kendrick (Dir. Educational Support)"],
        "Richard Metze (Software Dev)": ["Angeline Quinones (Project Manager)"],
        "Mayowa Akinyemi (Software Dev)": ["Angeline Quinones (Project Manager)"],
        "Joanne Delphia (Sr. Product Designer)": ["Angeline Quinones (Project Manager)"],
        "Seth Morris (LMS Admin)": ["Angeline Quinones (Project Manager)"]
    }

def create_department_colors():
    return {
        "Board of Directors": "lightgrey",
        "CEO": "#E6F3FF",
        "CFO": "#CCE7FF",
        "COO": "#CCE7FF",
        "Director": "#E6F3FF",
        "Lead": "#F0F9FF",
        "Manager": "#F0F9FF",
        "Developer": "#F8FCFF",
        "Designer": "#F8FCFF",
        "Trainer": "#F8FCFF",
        "Admin": "#F8FCFF",
        "Consultant": "#F8FCFF"
    }

def get_node_color(role):
    colors = create_department_colors()
    if "Board of Directors" in role:
        return colors["Board of Directors"]
    elif "CEO" in role:
        return colors["CEO"]
    elif "CFO" in role:
        return colors["CFO"]
    elif "COO" in role:
        return colors["COO"]
    elif "Dir." in role:
        return colors["Director"]
    elif "Lead" in role:
        return colors["Lead"]
    elif "Manager" in role:
        return colors["Manager"]
    elif "Dev" in role:
        return colors["Developer"]
    elif "Designer" in role:
        return colors["Designer"]
    elif "Trainer" in role:
        return colors["Trainer"]
    elif "Admin" in role:
        return colors["Admin"]
    elif "Consultant" in role:
        return colors["Consultant"]
    return "#FFFFFF"

def create_org_chart():
    # Create a new directed graph
    dot = graphviz.Digraph()
    dot.attr(rankdir='TB')
    
    # Set graph attributes
    dot.attr('node', shape='box', 
            style='filled,rounded', 
            fontname='Arial',
            margin='0.3,0.1')
    dot.attr('edge', color='#666666')
    
    # Get organizational data
    org_data = create_org_data()
    
    # Add all nodes first
    for role in org_data.keys():
        dot.node(role, role, fillcolor=get_node_color(role))
    
    # Add edges (reporting relationships)
    for role, reports_to in org_data.items():
        for superior in reports_to:
            dot.edge(superior, role)
    
    return dot

def create_responsibilities_data():
    return {
        "BJ Dines (CEO)": "Overall company strategy and leadership",
        "Leah Dines (CFO)": "Financial oversight, budgeting, and accounting",
        "Josh Leitz (COO)": "Manages operations, supports teams, and oversees curriculum",
        "Brian Snyder (Dir. Innovation & Partnerships)": "Oversees SchoolsPLP Sales, Backbone, and EDS teams",
        "LaRae Kendrick (Dir. Educational Support)": "Leads training, implementation, and support teams",
        "Jeremy Gold (Dir. Virtual Learning)": "Manages online learning coordination",
        "Kathe Arnold (Dir. Curriculum)": "Oversees content development and contractor collaboration",
        "Angeline Quinones (Project Manager)": "Leads software development and product design teams",
        "Micah Stetson (Software Consultant)": "Provides technical expertise and system architecture guidance",
        "Gordon Gower (Sr. Support & Coaching Lead)": "Provides advanced educational support",
        "Kim Schneper (Support & Integration Lead)": "Manages technical and process integration",
        "Kevin McCormick (Support & Education Lead)": "Special projects and support initiatives",
        "Gracie Perez (Special Projects Lead)": "Manages unique educational projects",
        "Leslie King (Professional Trainer)": "Conducts training for schools and staff",
        "Heather Caldwell (Professional Trainer)": "Conducts training for schools and staff",
        "Richard Metze (Software Dev)": "Develops and maintains company software",
        "Mayowa Akinyemi (Software Dev)": "Develops and maintains company software",
        "Joanne Delphia (Sr. Product Designer)": "Leads UX/UI and product experience design",
        "Seth Morris (LMS Admin)": "Manages learning management system"
    }

def main():
    st.title("SchoolsPLP Organizational Structure")
    
    # Create tabs
    tab1, tab2 = st.tabs(["Organizational Chart", "Role Details"])
    
    with tab1:
        # Display the organizational chart
        st.graphviz_chart(create_org_chart())
        
        st.markdown("""
        **Understanding the Chart:**
        - Boxes show reporting relationships from top to bottom
        - Colors indicate different organizational levels
        - Lines show direct reporting relationships
        """)
    
    with tab2:
        # Create role selector and display responsibilities
        responsibilities = create_responsibilities_data()
        selected_role = st.selectbox(
            "Select a Role to View Details:",
            list(responsibilities.keys())
        )
        
        st.markdown("### Role Details")
        st.markdown(f"**Role:** {selected_role}")
        st.markdown(f"**Responsibilities:** {responsibilities[selected_role]}")
        st.markdown(f"**Reports To:** {create_org_data()[selected_role][0]}")

if __name__ == "__main__":
    main()
