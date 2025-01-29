import streamlit as st
import networkx as nx
import plotly.graph_objects as go
from collections import defaultdict

# Set page configuration
st.set_page_config(page_title="SchoolsPLP Team Connections", layout="wide")

def create_team_data():
    return {
        "Leadership": {
            "Team Members": ["BJ Dines (CEO)", "Leah Dines (CFO)", "Josh Leitz (COO)", 
                           "Brian Snyder (Dir. Innovation & Partnerships)"],
            "Key Collaborations": ["All Teams", "Finance", "Operations", "Sales & Partnerships"]
        },
        "Educational Support": {
            "Team Members": ["LaRae Kendrick (Dir. Educational Support)", 
                           "Gordon Gower (Sr. Support & Coaching Lead)",
                           "Kim Schneper (Support & Integration Lead)",
                           "Kevin McCormick (Support & Education Lead)",
                           "Leslie King (Professional Trainer)",
                           "Heather Caldwell (Professional Trainer)"],
            "Key Collaborations": ["Product Team", "Curriculum", "Virtual Learning"]
        },
        "Product Team": {
            "Team Members": ["Angeline Quinones (Project Manager)",
                           "Richard Metze (Software Dev)",
                           "Mayowa Akinyemi (Software Dev)",
                           "Joanne Delphia (Sr. Product Designer)",
                           "Seth Morris (LMS Admin)"],
            "Key Collaborations": ["Educational Support", "Curriculum", "Virtual Learning"]
        },
        "Curriculum": {
            "Team Members": ["Kathe Arnold (Dir. Curriculum)"],
            "Key Collaborations": ["Educational Support", "Virtual Learning", "Product Team"]
        },
        "Virtual Learning": {
            "Team Members": ["Jeremy Gold (Dir. Virtual Learning)"],
            "Key Collaborations": ["Educational Support", "Curriculum", "Product Team"]
        }
    }

def create_responsibilities_data():
    return {
        "BJ Dines (CEO)": {
            "Responsibilities": "Overall company strategy and leadership",
            "Team": "Leadership",
            "Key Projects": ["Strategic Planning", "Company Growth", "Partnership Development"],
            "Common Collaborations": ["Executive Team", "Board of Directors", "All Department Heads"]
        },
        "Leah Dines (CFO)": {
            "Responsibilities": "Financial oversight, budgeting, and accounting",
            "Team": "Leadership",
            "Key Projects": ["Budget Planning", "Financial Reporting", "Resource Allocation"],
            "Common Collaborations": ["CEO", "Department Heads", "External Auditors"]
        },
        # Add all other roles similarly...
    }

def create_team_network():
    teams = create_team_data()
    G = nx.Graph()
    
    # Add nodes for each team
    for team in teams:
        G.add_node(team)
    
    # Add edges based on collaborations
    for team, data in teams.items():
        for collab in data["Key Collaborations"]:
            if collab in teams:
                G.add_edge(team, collab)
    
    # Calculate layout
    pos = nx.spring_layout(G)
    
    # Create the visualization
    edge_trace = go.Scatter(
        x=[], y=[],
        line=dict(width=2, color='#888'),
        hoverinfo='none',
        mode='lines')

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace['x'] += (x0, x1, None)
        edge_trace['y'] += (y0, y1, None)

    node_trace = go.Scatter(
        x=[], y=[],
        text=[],
        mode='markers+text',
        textposition="top center",
        hoverinfo='text',
        marker=dict(
            showscale=False,
            size=30,
            line_width=2))

    for node in G.nodes():
        x, y = pos[node]
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])
        node_trace['text'] += tuple([node])

    fig = go.Figure(data=[edge_trace, node_trace],
                   layout=go.Layout(
                       showlegend=False,
                       hovermode='closest',
                       margin=dict(b=20,l=5,r=5,t=40),
                       xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                   )
    
    return fig

def main():
    st.title("SchoolsPLP Team Connections")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.plotly_chart(create_team_network(), use_container_width=True)
        
        st.markdown("""
        **Understanding Team Connections:**
        - Nodes represent different teams within SchoolsPLP
        - Lines show primary collaboration paths
        - Closer nodes indicate more frequent collaboration
        """)
    
    with col2:
        teams = create_team_data()
        selected_team = st.selectbox("Select a Team:", list(teams.keys()))
        
        st.markdown(f"### {selected_team} Team")
        
        # Team Members
        st.markdown("**Team Members:**")
        for member in teams[selected_team]["Team Members"]:
            st.markdown(f"- {member}")
            
        # Key Collaborations
        st.markdown("\n**Key Collaborations:**")
        for collab in teams[selected_team]["Key Collaborations"]:
            st.markdown(f"- {collab}")
            
        # Additional context box
        st.markdown("---")
        st.markdown("""
        **Note:** This view complements the existing org chart by showing how 
        teams typically collaborate and work together across the organization.
        """)

if __name__ == "__main__":
    main()
