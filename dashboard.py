import streamlit as st
import plotly.graph_objects as go

def create_team_data():
    return {
        "Leadership": {
            "Team Members": {
                "BJ Dines": {
                    "Role": "CEO",
                    "Responsibilities": "Overall company leadership and strategy",
                    "Reports_To": "  "
                },
                "Leah Dines": {
                    "Role": "CFO",
                    "Responsibilities": "Financial oversight and management",
                   "Reports_To": "  "
                },
                "Brian Snyder": {
                    "Role": "Director of Innovation and Partnerships",
                    "Responsibilities": "Oversees Sales, Backbone, and Virtual Instruction",
                    "Reports_To": "CEO & CFO"
                },
                "Josh Leitz": {
                    "Role": "Chief Operations Officer",
                    "Responsibilities": "Oversees operations and curriculum",
                    "Reports_To": "CEO & CFO"
                },
                "LaRae Kendrick": {
                    "Role": "Director of Educational Support and Implementation",
                    "Responsibilities": "Leads educational support teams",
                    "Reports_To": "CEO & CFO"
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
            "Position": [0, 1]  # Top
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
            "Position": [0.866, 0.5]  # 60 degrees
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
            "Position": [0.866, -0.5]  # 120 degrees
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
            "Position": [0, -1]  # Bottom
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
            "Position": [-0.866, -0.5]  # 240 degrees
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
            "Position": [-0.866, 0.5]  # 300 degrees
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
            "Position": [0, 0.5]  # Right
        }
    }

def create_team_visualization(selected_team=None):
    teams = create_team_data()
    fig = go.Figure()

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
                        # Check if any team member reports to a role in this team
                        reports_to_this_team = False
                        for member_data in other_data["Team Members"].values():
                            member_reports_to = member_data.get("Reports_To", "")
                            for leader in data["Team Members"].values():
                                leader_role = leader.get("Role", "")
                                if member_reports_to in [leader_role, "Leadership Team", "CEO", "COO", "CFO"]:
                                    reports_to_this_team = True
                                    break
                            if reports_to_this_team:
                                break
                        
                        if reports_to_this_team:
                            color = '#1f77b4' if selected_team in [team, other_team] else '#E1E5E8'
                            width = 2 if selected_team in [team, other_team] else 1
                            fig.add_trace(go.Scatter(
                                x=[x0, x1], y=[y0, y1],
                                mode='lines',
                                line=dict(color=color, width=width),
                                hoverinfo='none',
                                showlegend=False
                            ))
                    elif any(reports_to == tm.get("Role", "") for tm in data["Team Members"].values()):
                        x1, y1 = other_data["Position"]
                        color = '#1f77b4' if selected_team in [team, other_team] else '#E1E5E8'
                        width = 2 if selected_team in [team, other_team] else 1
                        fig.add_trace(go.Scatter(
                            x=[x0, x1], y=[y0, y1],
                            mode='lines',
                            line=dict(color=color, width=width),
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
        node_text.append(f"{team}<br>{len(data['Team Members'])} members")
        
        # Set base size for all departments, with Leadership being larger
        if team == "Leadership":
            node_sizes.append(100)  # Larger size for Leadership
        else:
            node_sizes.append(70)   # Standard size for all other departments
            
        # Set colors based on selection
        if selected_team:
            if team == selected_team:
                node_colors.append('#1f77b4')  # Selected team color
            else:
                node_colors.append('#E1E5E8')  # Non-selected team color
        else:
            node_colors.append('lightblue')

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
            color='white',  # Text color for department names
            size=14,       # Increased font size
            family="Arial, sans-serif"  # Font family
        ),
        hoverinfo='text',
        showlegend=False
    ))

    fig.update_layout(
        showlegend=False,
        hovermode='closest',
        margin=dict(b=20,l=5,r=5,t=40),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='white',
        height=600
    )
    
    return fig

def main():
    st.markdown("<h1 style='color: #1f77b4;'>SchoolsPLP Organizational Structure</h1>", unsafe_allow_html=True)
    
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

        # Add manager note
        st.markdown("---")
        st.markdown("""
        **Note:** The Leadership Team consists of BJ Dines (CEO), 
        Leah Dines (CFO), Brian Snyder (Director of Innovation and Partnerships), 
        LaRae Kendrick (Director of Educational Support), and 
        Josh Leitz (Chief Operations Officer).
        """)
        
        st.markdown("""
        If you have any concerns or need additional support, 
        please reach out to either Brian or Josh, who will work 
        together to provide assistance.
        """)
    
    with col1:
        st.plotly_chart(create_team_visualization(selected_team), use_container_width=True)
        
        st.markdown("""
        **Understanding the Visualization:**
        - Each circle represents a department
        - Click on departments to see details
        """)

if __name__ == "__main__":
    main()
