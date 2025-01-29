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
                    "Reports_To": " "
                },
                "Brian Snyder": {
                    "Role": "Director of Innovation and Partnerships",
                    "Responsibilities": "Oversees SchoolsPLP Sales, Backbone, and EDS teams",
                    "Reports_To": " "
                },
                "Josh Leitz": {
                    "Role": "Chief Operations Officer",
                    "Responsibilities": "Oversees operations and curriculum",
                    "Reports_To": "CEO"
                },
                "LaRae Kendrick": {
                    "Role": "Director of Educational Support and Implementation",
                    "Responsibilities": "Leads educational support and implementation teams",
                    "Reports_To": "CEO"
                }
            },
            "Position": [0, 1]
        },
        "Finance": {
            "Team Members": {
                "Melanie Gonzalez": {
                    "Role": "Accounting Associate",
                    "Responsibilities": "Accounting and financial support",
                    "Reports_To": "CFO"
                }
            },
            "Position": [1, 0.5]
        },
        "Virtual Learning": {
            "Team Members": {
                "Jeremy Gold": {
                    "Role": "Director of Virtual Learning",
                    "Responsibilities": "Manages virtual learning programs",
                    "Reports_To": "Director of Innovation and Partnerships"
                },
                "Kiff Kanady": {
                    "Role": "Academic Success Coordinator",
                    "Responsibilities": "Coordinates academic success initiatives",
                    "Reports_To": "Director of Virtual Learning"
                }
            },
            "Position": [-1, 0]
        },
        "Sales": {
            "Team Members": {
                "Jeff Martin": {
                    "Role": "Sales",
                    "Responsibilities": "SchoolsPLP Sales",
                    "Reports_To": "Director of Innovation and Partnerships"
                },
                "Craig Whitaker": {
                    "Role": "Sales",
                    "Responsibilities": "SchoolsPLP Sales",
                    "Reports_To": "Director of Innovation and Partnerships"
                }
            },
            "Position": [-1, 0.5]
        },
        "Educational Support": {
            "Team Members": {
                "Gordon Gower": {
                    "Role": "Senior Support and Coaching Lead",
                    "Responsibilities": "Leads support and coaching initiatives",
                    "Reports_To": "Director of Educational Support"
                },
                "Kim Schneper": {
                    "Role": "Support Specialist and Integration Lead",
                    "Responsibilities": "Manages support and integration",
                    "Reports_To": "Senior Support and Coaching Lead"
                },
                "Kevin McCormick": {
                    "Role": "Support Specialist and Special Education Lead",
                    "Responsibilities": "Leads special education support",
                    "Reports_To": "Support Specialist and Integration Lead"
                },
                "Gracie Perez": {
                    "Role": "Support Specialist and Special Projects Lead",
                    "Responsibilities": "Manages special projects",
                    "Reports_To": "Support Specialist and Special Education Lead"
                },
                "Leslie King": {
                    "Role": "Professional Trainer",
                    "Responsibilities": "Conducts professional training",
                    "Reports_To": "Director of Educational Support"
                },
                "Heather Caldwell": {
                    "Role": "Professional Trainer",
                    "Responsibilities": "Conducts professional training",
                    "Reports_To": "Director of Educational Support"
                }
            },
            "Position": [0, 0]
        },
        "Operations": {
            "Team Members": {
                "Kathe Arnold": {
                    "Role": "Director of Curriculum",
                    "Responsibilities": "Oversees curriculum development",
                    "Reports_To": "COO"
                },
                "Kara Holland": {
                    "Role": "Curriculum Specialist",
                    "Responsibilities": "Curriculum development and management",
                    "Reports_To": "Director of Curriculum"
                },
                "Brandon Hellman": {
                    "Role": "Science Curriculum Specialist",
                    "Responsibilities": "Science curriculum development",
                    "Reports_To": "Curriculum Specialist"
                },
                "Aiyana Pomato": {
                    "Role": "Standards Alignments, SSELA",
                    "Responsibilities": "Standards alignment for SSELA",
                    "Reports_To": "Science Curriculum Specialist"
                }
            },
            "Position": [0.5, 0]
        },
        "Technology": {
            "Team Members": {
                "Angeline Quinones": {
                    "Role": "Project Manager",
                    "Responsibilities": "Manages software development projects",
                    "Reports_To": "COO"
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
                },
                "Micah Stetson": {
                    "Role": "Software Developer/System Architect",
                    "Responsibilities": "System architecture and development",
                    "Reports_To": "Project Manager"
                }
            },
            "Position": [1, -0.5]
        },
        "Backbone": {
            "Team Members": {
                "Brian Snyder": {
                    "Role": "Team Lead",
                    "Reports_To": "Director of Innovation and Partnerships"
                },
                "Matt West": {
                    "Role": "Team Member",
                    "Reports_To": "Team Lead"
                },
                "Ken Behrendt": {
                    "Role": "Team Member",
                    "Reports_To": "Team Lead"
                }
            },
            "Position": [-1, -0.5]
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
                    if any(reports_to == tm.get("Role", "") for tm in data["Team Members"].values()):
                        x1, y1 = other_data["Position"]
                        
                        # Determine if this connection should be highlighted
                        if selected_team and (team == selected_team or other_team == selected_team):
                            color = '#1f77b4'  # Blue for active connections
                            width = 2
                        else:
                            color = '#E1E5E8'  # Gray for inactive connections
                            width = 1
                        
                        fig.add_trace(go.Scatter(
                            x=[x0, x1],
                            y=[y0, y1],
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
        
        if selected_team:
            if team == selected_team:
                node_colors.append('#1f77b4')  # Primary blue for selected team
                node_sizes.append(50)
            else:
                node_colors.append('#E1E5E8')  # Gray for other teams
                node_sizes.append(35)
        else:
            node_colors.append('lightblue')
            node_sizes.append(40)

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
    st.title("SchoolsPLP Organizational Structure")
    
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
        **Note:** Black outlined boxes in the org chart denote Managers 
        responsible for overseeing teams and conducting performance reviews.
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
        - Size indicates number of team members
        - Lines show reporting relationships
        - Click on departments to see details
        """)

if __name__ == "__main__":
    main()
