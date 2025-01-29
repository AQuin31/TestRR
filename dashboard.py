import streamlit as st
import plotly.graph_objects as go
from collections import defaultdict

# Set page configuration
st.set_page_config(page_title="SchoolsPLP Team Connections", layout="wide")

def create_team_data():
    return {
        "Leadership": {
            "Team Members": {
                "BJ Dines (CEO)": {
                    "Role": "Chief Executive Officer",
                    "Responsibilities": "Overall company strategy and leadership",
                    "Key Projects": ["Strategic Planning", "Company Growth", "Partnership Development"]
                },
                "Leah Dines (CFO)": {
                    "Role": "Chief Financial Officer",
                    "Responsibilities": "Financial oversight, budgeting, and accounting",
                    "Key Projects": ["Budget Planning", "Financial Analysis", "Resource Allocation"]
                },
                "Josh Leitz (COO)": {
                    "Role": "Chief Operating Officer",
                    "Responsibilities": "Manages operations, supports teams, and oversees curriculum",
                    "Key Projects": ["Operations Management", "Team Coordination", "Process Improvement"]
                },
                "Brian Snyder (Dir. Innovation & Partnerships)": {
                    "Role": "Director of Innovation & Partnerships",
                    "Responsibilities": "Oversees SchoolsPLP Sales, Backbone, and EDS teams",
                    "Key Projects": ["Partnership Development", "Innovation Initiatives", "Sales Strategy"]
                }
            },
            "Key Collaborations": ["Educational Support", "Product", "Curriculum", "Virtual Learning"],
            "Position": [0, 0]
        },
        "Educational Support": {
            "Team Members": {
                "LaRae Kendrick (Dir. Educational Support)": {
                    "Role": "Director of Educational Support",
                    "Responsibilities": "Leads training, implementation, and support teams",
                    "Key Projects": ["Training Program Development", "Support Strategy", "Implementation Planning"]
                },
                "Gordon Gower (Sr. Support & Coaching Lead)": {
                    "Role": "Senior Support & Coaching Lead",
                    "Responsibilities": "Provides advanced educational support",
                    "Key Projects": ["Support Team Leadership", "Coaching Program", "Quality Assurance"]
                },
                "Kim Schneper (Support & Integration Lead)": {
                    "Role": "Support & Integration Lead",
                    "Responsibilities": "Manages technical and process integration",
                    "Key Projects": ["Integration Management", "Process Development", "Technical Support"]
                },
                "Kevin McCormick (Support & Education Lead)": {
                    "Role": "Support & Education Lead",
                    "Responsibilities": "Special projects and support initiatives",
                    "Key Projects": ["Education Programs", "Support Projects", "Team Training"]
                },
                "Leslie King (Professional Trainer)": {
                    "Role": "Professional Trainer",
                    "Responsibilities": "Conducts training for schools and staff",
                    "Key Projects": ["School Training", "Staff Development", "Training Materials"]
                },
                "Heather Caldwell (Professional Trainer)": {
                    "Role": "Professional Trainer",
                    "Responsibilities": "Conducts training for schools and staff",
                    "Key Projects": ["School Training", "Staff Development", "Training Materials"]
                }
            },
            "Key Collaborations": ["Leadership", "Product", "Curriculum"],
            "Position": [-1, 1]
        },
        "Product": {
            "Team Members": {
                "Angeline Quinones (Project Manager)": {
                    "Role": "Project Manager",
                    "Responsibilities": "Leads software development and product design teams",
                    "Key Projects": ["Product Development", "Team Management", "Release Planning"]
                },
                "Richard Metze (Software Dev)": {
                    "Role": "Software Developer",
                    "Responsibilities": "Develops and maintains company software",
                    "Key Projects": ["Software Development", "Code Maintenance", "Feature Implementation"]
                },
                "Mayowa Akinyemi (Software Dev)": {
                    "Role": "Software Developer",
                    "Responsibilities": "Develops and maintains company software",
                    "Key Projects": ["Software Development", "Code Maintenance", "Feature Implementation"]
                },
                "Joanne Delphia (Sr. Product Designer)": {
                    "Role": "Senior Product Designer",
                    "Responsibilities": "Leads UX/UI and product experience design",
                    "Key Projects": ["UX Design", "UI Implementation", "User Research"]
                },
                "Seth Morris (LMS Admin)": {
                    "Role": "LMS Administrator",
                    "Responsibilities": "Manages learning management system",
                    "Key Projects": ["LMS Administration", "System Maintenance", "User Support"]
                }
            },
            "Key Collaborations": ["Leadership", "Educational Support", "Curriculum"],
            "Position": [1, 1]
        },
        "Curriculum": {
            "Team Members": {
                "Kathe Arnold (Dir. Curriculum)": {
                    "Role": "Director of Curriculum",
                    "Responsibilities": "Oversees content development and contractor collaboration",
                    "Key Projects": ["Curriculum Development", "Content Strategy", "Quality Assessment"]
                }
            },
            "Key Collaborations": ["Leadership", "Educational Support", "Product", "Virtual Learning"],
            "Position": [-1, -1]
        },
        "Virtual Learning": {
            "Team Members": {
                "Jeremy Gold (Dir. Virtual Learning)": {
                    "Role": "Director of Virtual Learning",
                    "Responsibilities": "Manages online learning coordination",
                    "Key Projects": ["Virtual Program Management", "Online Learning Strategy", "Technology Integration"]
                }
            },
            "Key Collaborations": ["Leadership", "Curriculum", "Educational Support"],
            "Position": [1, -1]
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
    
    teams = create_team_data()
    
    with col1:
        st.plotly_chart(create_team_visualization(), use_container_width=True)
        
        st.markdown("""
        **Understanding Team Connections:**
        - Each circle represents a team within SchoolsPLP
        - Lines show primary collaboration paths between teams
        - This view complements the org chart by showing cross-functional relationships
        """)
    
    with col2:
        # First dropdown for team selection
        selected_team = st.selectbox("Select a Team:", list(teams.keys()))
        
        # Second dropdown for team member selection
        team_members = list(teams[selected_team]["Team Members"].keys())
        selected_member = st.selectbox("Select a Team Member:", team_members)
        
        # Display member details
        if selected_member:
            member_data = teams[selected_team]["Team Members"][selected_member]
            
            st.markdown(f"### {selected_member}")
            st.markdown(f"**Role:** {member_data['Role']}")
            st.markdown(f"**Responsibilities:** {member_data['Responsibilities']}")
            
            st.markdown("**Key Projects:**")
            for project in member_data['Key Projects']:
                st.markdown(f"- {project}")
            
            st.markdown("\n**Team Collaborations:**")
            for collab in teams[selected_team]["Key Collaborations"]:
                st.markdown(f"- {collab}")

        # Add interaction hint
        st.markdown("---")
        st.markdown("""
        **Tip:** Use the dropdowns above to explore different teams and team members.
        The visualization shows how teams connect across the organization.
        """)

if __name__ == "__main__":
    main()
