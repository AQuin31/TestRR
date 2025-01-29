import streamlit as st
import plotly.graph_objects as go

def create_team_data():
    return {
        "Leadership": {
            "Team Members": {
                "BJ Dines": {
                    "Role": "CEO",
                    "Responsibilities": "Overall company leadership and strategy",
                    "Reports_To": "Board of Directors"
                },
                "Leah Dines": {
                    "Role": "CFO",
                    "Responsibilities": "Financial oversight and management",
                    "Reports_To": "CEO"
                },
                "Brian Snyder": {
                    "Role": "Director of Innovation and Partnerships",
                    "Responsibilities": "Oversees Sales, Backbone, and Virtual Instruction",
                    "Reports_To": "CEO"
                },
                "Josh Leitz": {
                    "Role": "Chief Operations Officer",
                    "Responsibilities": "Oversees operations and curriculum",
                    "Reports_To": "CEO"
                },
                "LaRae Kendrick": {
                    "Role": "Director of Educational Support and Implementation",
                    "Responsibilities": "Leads educational support teams",
                    "Reports_To": "CEO"
                }
            },
            "Position": [0, 0]  # Center position
        },
        "Finance": {
            "Team Members": {
                "Melanie Gonzalez": {
                    "Role": "Accounting Associate",
                    "Responsibilities": "Accounting and financial support",
                    "Reports_To": "CFO"
                }
            },
            "Position": [0, 2]  # Top
        },
        "Sales": {
            "Team Members": {
                "Jeff Martin": {
                    "Role": "SchoolsPLP Sales",
                    "Responsibilities": "Sales representative",
                    "Reports_To": "Director of Innovation and Partnerships"
                },
                "Craig Whitaker": {
                    "Role": "SchoolsPLP Sales",
                    "Responsibilities": "Sales representative",
                    "Reports_To": "Director of Innovation and Partnerships"
                },
                "Brian Snyder": {
                    "Role": "Backbone Team Lead",
                    "Responsibilities": "Leads Backbone Communications",
                    "Reports_To": "Director of Innovation and Partnerships"
                },
                "Matt West": {
                    "Role": "Backbone Team Member",
                    "Responsibilities": "Backbone Communications",
                    "Reports_To": "Backbone Team Lead"
                },
                "Ken Behrendt": {
                    "Role": "Backbone Team Member",
                    "Responsibilities": "Backbone Communications",
                    "Reports_To": "Backbone Team Lead"
                },
                "Aaron Eustariemann": {
                    "Role": "EDS Reseller",
                    "Responsibilities": "EDS Sales",
                    "Reports_To": "Director of Innovation and Partnerships"
                },
                "Amanda Fouts": {
                    "Role": "EDS Reseller",
                    "Responsibilities": "EDS Sales",
                    "Reports_To": "Director of Innovation and Partnerships"
                },
                "Gail Lanier": {
                    "Role": "EDS Reseller",
                    "Responsibilities": "EDS Sales",
                    "Reports_To": "Director of Innovation and Partnerships"
                },
                "Rikki Black": {
                    "Role": "AES Reseller",
                    "Responsibilities": "AES Sales",
                    "Reports_To": "Director of Innovation and Partnerships"
                },
                "Eric Moon": {
                    "Role": "JNR Reseller",
                    "Responsibilities": "JNR Sales",
                    "Reports_To": "Director of Innovation and Partnerships"
                },
                "Roger Choate": {
                    "Role": "Learning Partners Reseller",
                    "Responsibilities": "Learning Partners Sales",
                    "Reports_To": "Director of Innovation and Partnerships"
                }
            },
            "Position": [1.73, 1]  # 60 degrees
        },
        "Virtual Instruction": {
            "Team Members": {
                "Jeremy Gold": {
                    "Role": "Director of Virtual Learning",
                    "Responsibilities": "Manages virtual learning programs",
                    "Reports_To": "Director of Innovation and Partnerships"
                },
                "Kifi Kanegy": {
                    "Role": "Academic Success Coordinator",
                    "Responsibilities": "Coordinates academic success initiatives",
                    "Reports_To": "Director of Virtual Learning"
                }
            },
            "Position": [1.73, -1]  # 120 degrees
        },
        "Support": {
            "Team Members": {
                "Gordon Gower": {
                    "Role": "Senior Support Specialist and Coaching Lead",
                    "Responsibilities": "Leads support and coaching initiatives",
                    "Reports_To": "Director of Educational Support and Implementation"
                },
                "Kim Schnepper": {
                    "Role": "Support Specialist and Integration Lead",
                    "Responsibilities": "Manages support and integration",
                    "Reports_To": "Senior Support Specialist and Coaching Lead"
                },
                "Kevin McCormick": {
                    "Role": "Support Specialist and Special Education Lead",
                    "Responsibilities": "Leads special education support",
                    "Reports_To": "Senior Support Specialist and Coaching Lead"
                },
                "Gracie Perez": {
                    "Role": "Support Specialist and Special Projects Lead",
                    "Responsibilities": "Manages special projects",
                    "Reports_To": "Senior Support Specialist and Coaching Lead"
                }
            },
            "Position": [0, -2]  # Bottom
        },
        "Curriculum": {
            "Team Members": {
                "Kathe Arnold": {
                    "Role": "Director of Curriculum",
                    "Responsibilities": "Oversees curriculum development",
                    "Reports_To": "Leadership Team"
                },
                "Kara Holland": {
                    "Role": "Curriculum Specialist",
                    "Responsibilities": "Curriculum development and management",
                    "Reports_To": "Director of Curriculum"
                },
                "Brandon Hellman": {
                    "Role": "Science Curriculum Specialist",
                    "Responsibilities": "Science curriculum development",
                    "Reports_To": "Director of Curriculum"
                },
                "Aiyana Pomato": {
                    "Role": "Standards Alignments, SS/ELA",
                    "Responsibilities": "Standards alignment for SS/ELA",
                    "Reports_To": "Director of Curriculum"
                }
            },
            "Position": [-1.73, -1]  # 240 degrees
        },
        "Development": {
            "Team Members": {
                "Angeline Quinones": {
                    "Role": "Project Manager",
                    "Responsibilities": "Manages software development projects",
                    "Reports_To": "Leadership Team"
                },
                "Richard Metze": {
                    "Role": "Software Developer",
                    "Responsibilities": "Software development",
                    "Reports_To": "Project Manager"
                },
                "Mayowa Akinyemi": {
                    "Role": "Software Developer",
                    "Responsibilities": "Software development",
                    "Reports_To": "Project Manager"
                },
                "Joanne Delphia": {
                    "Role": "Senior Product Designer",
                    "Responsibilities": "Product design and UX",
                    "Reports_To": "Project Manager"
                },
                "Seth Morris": {
                    "Role": "LMS Administrator",
                    "Responsibilities": "Learning Management System administration",
                    "Reports_To": "Project Manager"
                }
            },
            "Position": [-1.73, 1]  # 300 degrees
        },
        "Training": {
            "Team Members": {
                "Leslie King": {
                    "Role": "Professional Trainer",
                    "Responsibilities": "Conducts professional training",
                    "Reports_To": "Leadership Team"
                },
                "Heather Caldwell": {
                    "Role": "Professional Trainer",
                    "Responsibilities": "Conducts professional training",
                    "Reports_To": "Leadership Team"
                }
            },
            "Position": [0, 1]  # Between Finance and Sales
        }
    }

def create_team_visualization(selected_team=None):
    teams = create_team_data()
    fig = go.Figure()

    # Define ROYGBIV color map
    color_map = {
        "Leadership": '#FF0000',     # Red
        "Finance": '#FF7F00',        # Orange
        "Sales": '#FFFF00',          # Yellow
        "Virtual Instruction": '#00FF00',  # Green
        "Support": '#0000FF',        # Blue
        "Curriculum": '#4B0082',     # Indigo
        "Development": '#8F00FF',    # Violet
        "Training": '#FF69B4'        # Pink
    }

    # Add connections between teams
    for team, data in teams.items():
        x0, y0 = data["Position"]
        
        # Find teams that have members reporting to leaders in this team
        for other_team, other_data in teams.items():
            if team != other_team:
                for member in other_data["Team Members"].values():
                    reports_to = member.get("Reports_To", "")
                    if reports_to == "Leadership Team" and team == "Leadership":
                        x1, y1 = other_data["Position"]
                        fig.add_trace(go.Scatter(
                            x=[x0, x1], y=[y0, y1],
                            mode='lines',
                            line=dict(color='#808080', width=1),
                            hoverinfo='none',
                            showlegend=False
                        ))
                    elif any(reports_to == tm.get("Role", "") for tm in data["Team Members"].values()):
                        x1, y1 = other_data["Position"]
                        fig.add_trace(go.Scatter(
                            x=[x0, x1], y=[y0, y1],
                            mode='lines',
                            line=dict(color='#808080', width=1),
                            hoverinfo='none',
                            showlegend=False
                        ))

    # Add team nodes
    node_x = []
    node_y = []
    node_text = []
    node_colors = []
    node_sizes = []
    
    for team, data in teams.items():
        node_x.append(data["Position"][0])
        node_y.append(data["Position"][1])
        node_text.append(team)
        
        # Set fixed sizes and ROYGBIV colors
        if team == "Leadership":
            node_sizes.append(150)  # Larger size for Leadership
        else:
            node_sizes.append(100)  # Standard size for all other departments
        
        # Apply colors from color map
        node_colors.append(color_map[team])

    fig.add_trace(go.Scatter(
        x=node_x,
        y=node_y,
        text=node_text,
        mode='markers+text',
        marker=dict(
            color=node_colors,
            size=node_sizes,
            line=dict(color='white', width=2)
        ),
        textposition="middle center",
        textfont=dict(
            color='black',  # Text color for department names
            size=14,       # Font size
            family="Arial, sans-serif"
        ),
        hovertext=node_text,
        hoverinfo='text',
        showlegend=False
    ))

    fig.update_layout(
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20,l=5,r=5,t=40),
        xaxis=dict(
            showgrid=False, 
            zeroline=False, 
            showticklabels=False,
            range=[-2.5, 2.5]  # Increased range for more space
        ),
        yaxis=dict(
            showgrid=False, 
            zeroline=False, 
            showticklabels=False,
            range=[-2.5, 2.5]  # Increased range for more space
        ),
        plot_bgcolor='white',
        height=800  # Increased height
    )
    
    return fig

def main():
    st.markdown('<h1 style="margin-top: 0.5rem;">SchoolsPLP Organizational Structure</h1>', unsafe_allow_html=True)
    
    teams = create_team_data()
    
    col1, col2 = st.columns([3, 2])
    
    with col2:
        # First dropdown for team selection
        selected_team = st.selectbox("Select a Department:", list(teams.keys()))
        
        # Second dropdown for team member selection
        team_members = list(teams[selected_team]["Team Members"].keys())
        selected_member = st.selectbox("Select a Team Member:", team_members)
        
        # Display member details
        if selected_member:
            member_data = teams[selected_team]["Team Members"][selected_member]
            
            st.markdown(f"### {selected_member}")
            st.markdown(f"**Role:** {member_data['Role']}")
            if "Responsibilities" in member_data:
                st.markdown(f"**Responsibilities:** {member_data['Responsibilities']}")
            st.markdown(f"**Reports To:** {member_data['Reports_To']}")
    
    with col1:
        st.plotly_chart(create_team_visualization(selected_team), use_container_width=True)

if __name__ == "__main__":
    main()
