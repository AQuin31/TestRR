import streamlit as st
import plotly.graph_objects as go
from collections import defaultdict

# Set page configuration
st.set_page_config(page_title="SchoolsPLP Team Connections", layout="wide")

def create_team_data():
    return {
        "Leadership": {
            "Team Members": ["BJ Dines (CEO)", "Leah Dines (CFO)", "Josh Leitz (COO)", 
                           "Brian Snyder (Dir. Innovation & Partnerships)"],
            "Key Collaborations": ["Educational Support", "Product", "Curriculum", "Virtual Learning"],
            "Position": [0, 0]  # Central position
        },
        "Educational Support": {
            "Team Members": ["LaRae Kendrick (Dir. Educational Support)", 
                           "Gordon Gower (Sr. Support & Coaching Lead)",
                           "Kim Schneper (Support & Integration Lead)",
                           "Kevin McCormick (Support & Education Lead)",
                           "Leslie King (Professional Trainer)",
                           "Heather Caldwell (Professional Trainer)"],
            "Key Collaborations": ["Leadership", "Product", "Curriculum"],
            "Position": [-1, 1]  # Top left
        },
        "Product": {
            "Team Members": ["Angeline Quinones (Project Manager)",
                           "Richard Metze (Software Dev)",
                           "Mayowa Akinyemi (Software Dev)",
                           "Joanne Delphia (Sr. Product Designer)",
                           "Seth Morris (LMS Admin)"],
            "Key Collaborations": ["Leadership", "Educational Support", "Curriculum"],
            "Position": [1, 1]  # Top right
        },
        "Curriculum": {
            "Team Members": ["Kathe Arnold (Dir. Curriculum)"],
            "Key Collaborations": ["Leadership", "Educational Support", "Product", "Virtual Learning"],
            "Position": [-1, -1]  # Bottom left
        },
        "Virtual Learning": {
            "Team Members": ["Jeremy Gold (Dir. Virtual Learning)"],
            "Key Collaborations": ["Leadership", "Curriculum", "Educational Support"],
            "Position": [1, -1]  # Bottom right
        }
    }

def create_team_visualization():
    teams = create_team_data()
    
    # Create nodes (teams)
    node_x = []
    node_y = []
    node_text = []
    for team, data in teams.items():
        node_x.append(data["Position"][0])
        node_y.append(data["Position"][1])
        node_text.append(team)
    
    # Create edges (collaborations)
    edge_x = []
    edge_y = []
    for team, data in teams.items():
        x0, y0 = data["Position"]
        for collab in data["Key Collaborations"]:
            if collab in teams:
                x1, y1 = teams[collab]["Position"]
                edge_x.extend([x0, x1, None])
                edge_y.extend([y0, y1, None])
    
    # Create the visualization
    fig = go.Figure()
    
    # Add edges
    fig.add_trace(go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines'
    ))
    
    # Add nodes
    fig.add_trace(go.Scatter(
        x=node_x, y=node_y,
        text=node_text,
        mode='markers+text',
        hoverinfo='text',
        marker=dict(
            size=40,
            line_width=2,
            color='lightblue'
        ),
        textposition="middle center"
    ))
    
    # Update layout
    fig.update_layout(
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20,l=5,r=5,t=40),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='white'
    )
    
    return fig

def main():
    st.title("SchoolsPLP Team Connections")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.plotly_chart(create_team_visualization(), use_container_width=True)
        
        st.markdown("""
        **Understanding Team Connections:**
        - Each circle represents a team within SchoolsPLP
        - Lines show primary collaboration paths between teams
        - This view complements the org chart by showing cross-functional relationships
        """)
    
    with col2:
        teams = create_team_data()
        selected_team = st.selectbox("Select a Team:", list(teams.keys()))
        
        st.markdown(f"### {selected_team}")
        
        # Team Members
        st.markdown("**Team Members:**")
        for member in teams[selected_team]["Team Members"]:
            st.markdown(f"- {member}")
            
        # Key Collaborations
        st.markdown("\n**Key Collaborations:**")
        for collab in teams[selected_team]["Key Collaborations"]:
            st.markdown(f"- {collab}")
        
        # Add interaction hint
        st.markdown("---")
        st.markdown("""
        **Tip:** Click on different teams to see their members and collaborations.
        This view helps understand how teams work together across the organization.
        """)

if __name__ == "__main__":
    main()
