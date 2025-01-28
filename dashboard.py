import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page config
st.set_page_config(layout="wide", page_title="SchoolsPLP Org Structure")

# Create the organizational data
def create_org_data():
    role_data = {
        "Role": [
            "BJ Dines (CEO)", "Leah Dines (CFO)", "Brian Snyder (Dir. Innovation & Partnerships)",
            "Josh Leitz (COO)", "LaRae Kendrick (Dir. Educational Support)", 
            "Jeremy Gold (Dir. Virtual Learning)", "Kathe Arnold (Dir. Curriculum)",
            "Angeline Quinones (Project Manager)", "Micah Stetson (Software Consultant)",
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
        "Reports_To": [
            "Owners", "Owners", "Owners", "Owners", "Owners",
            "Leadership Team", "Leadership Team", "Leadership Team",
            "COO (Consultant)", "Director of Educational Support", 
            "Director of Educational Support", "Director of Educational Support",
            "Director of Educational Support", "Director of Educational Support",
            "Director of Educational Support", "Project Manager", "Project Manager",
            "Project Manager", "Project Manager"
        ]
    }
    return pd.DataFrame(role_data)

def calculate_influence_score(role):
    """Calculate influence score based on role type"""
    if 'CEO' in role or 'CFO' in role:
        return 0.95
    elif 'COO' in role or 'Edu' in role:
        return 0.85
    elif 'Dir.' in role or 'Man' in role:
        return 0.75
    elif 'Sr.' in role or 'Tra' in role or 'Dev' in role:
        return 0.65
    elif 'Lead' in role:
        return 0.55
    else:
        return 0.45

def create_org_chart(df):
    # Calculate influence scores
    df['Influence_Score'] = df['Role'].apply(calculate_influence_score)
    
    # Sort by influence score and reporting structure
    df = df.sort_values(['Influence_Score', 'Reports_To'], ascending=[False, True])
    
    # Create figure with secondary y-axis
    fig = go.Figure()

    # Add bars for influence scores
    fig.add_trace(
        go.Bar(
            x=df['Influence_Score'],
            y=df['Role'],
            orientation='h',
            marker=dict(
                color=df['Influence_Score'],
                colorscale='Blues',
                showscale=True,
                colorbar=dict(
                    title="Collaborative Decision-Making Index",
                    titleside="right"
                )
            ),
            name='Influence Score'
        )
    )

    # Update layout
    fig.update_layout(
        title="SchoolsPLP Organizational Structure",
        title_x=0.5,
        showlegend=False,
        height=800,
        xaxis=dict(
            title="Collaborative Decision-Making Index",
            showgrid=True,
            range=[0, 1]
        ),
        yaxis=dict(
            title="Roles",
            showgrid=True,
            autorange="reversed"
        ),
        plot_bgcolor='white'
    )
    
    return fig

def main():
    st.title("SchoolsPLP Organizational Dashboard")
    
    # Create DataFrame
    df = create_org_data()
    
    # Create two columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Display organizational chart
        fig = create_org_chart(df)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Role Details")
        # Create role selector without index
        selected_role = st.selectbox(
            "Select a Role:",
            options=df['Role'].tolist(),
            index=0
        )
        
        # Display role details
        role_info = df[df['Role'] == selected_role].iloc[0]
        st.markdown(f"**Role:** {role_info['Role']}")
        st.markdown(f"**Responsibilities:** {role_info['Responsibilities']}")
        st.markdown(f"**Reports To:** {role_info['Reports_To']}")
        
        # Add explanation of the visualization
        st.markdown("---")
        st.markdown("""
        **About the Visualization:**
        
        The Collaborative Decision-Making Index represents the level of influence 
        and involvement in decision-making processes. Higher scores indicate 
        greater responsibility in strategic decisions, while maintaining our 
        commitment to collaborative input from all team members.
        """)

if __name__ == "__main__":
    main()
