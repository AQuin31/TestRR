import streamlit as st
import plotly.graph_objects as go
import pandas as pd

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
            "Position": [1.73, 1]  # Top right
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
            "Position": [0, 1.3]  # Top
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
            "Position": [1.73, -1]  # Right lower
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
            "Position": [-1.73, -1]  # Left lower
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
            "Position": [-1.73, 1]  # Left upper
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
            "Position": [0, 2.3]  # Higher top position
        }
    }

def create_raci_data():
    """Create RACI matrix data structure"""
    return {
        "Platform Feature Changes": {
            "Leadership": {
                "BJ Dines": "A",
                "Josh Leitz": "A",
                "Brian Snyder": "C"
            },
            "Development": {
                "Angeline Quinones": "R",
                "Richard Metze": "R",
                "Mayowa Akinyemi": "R",
                "Seth Morris": "C"
            },
            "Support": {
                "Gordon Gower": "C",
                "Kim Schnepper": "I"
            },
            "Curriculum": {
                "Kathe Arnold": "C"
            }
        },
        "Content Updates": {
            "Leadership": {
                "Josh Leitz": "A"
            },
            "Curriculum": {
                "Kathe Arnold": "R",
                "Kara Holland": "R",
                "Brandon Hellman": "R",
                "Aiyana Pomato": "R"
            },
            "Development": {
                "Seth Morris": "I"
            },
            "Support": {
                "Gordon Gower": "C"
            }
        },
        "Bug Fixes": {
            "Development": {
                "Angeline Quinones": "A",
                "Richard Metze": "R",
                "Mayowa Akinyemi": "R"
            },
            "Support": {
                "Gordon Gower": "C",
                "Kim Schnepper": "R"
            }
        },
        "User Access Management": {
            "Leadership": {
                "Josh Leitz": "A"
            },
            "Development": {
                "Seth Morris": "R",
                "Angeline Quinones": "C"
            },
            "Support": {
                "Kim Schnepper": "R",
                "Gordon Gower": "C"
            }
        },
        "Third-party Integrations": {
            "Leadership": {
                "Brian Snyder": "A",
                "Josh Leitz": "C"
            },
            "Development": {
                "Angeline Quinones": "R",
                "Seth Morris": "R"
            },
            "Support": {
                "Kim Schnepper": "C"
            }
        },
        "Training Material Updates": {
            "Training": {
                "Leslie King": "R",
                "Heather Caldwell": "R"
            },
            "Curriculum": {
                "Kathe Arnold": "A"
            },
            "Support": {
                "Gordon Gower": "C"
            }
        },
        "Customer Support Escalations": {
            "Support": {
                "Gordon Gower": "R",
                "Kim Schnepper": "R"
            },
            "Leadership": {
                "LaRae Kendrick": "A",
                "Brian Snyder": "C"
            },
            "Development": {
                "Angeline Quinones": "C"
            }
        },
        "Performance Monitoring": {
            "Development": {
                "Seth Morris": "R",
                "Angeline Quinones": "A"
            },
            "Support": {
                "Gordon Gower": "C"
            },
            "Leadership": {
                "Josh Leitz": "I"
            }
        },
        "Security Updates": {
            "Development": {
                "Angeline Quinones": "A",
                "Seth Morris": "R"
            },
            "Leadership": {
                "Josh Leitz": "I",
                "BJ Dines": "I"
            }
        },
        "Data Management": {
            "Development": {
                "Seth Morris": "R",
                "Angeline Quinones": "A"
            },
            "Support": {
                "Kim Schnepper": "C"
            },
            "Leadership": {
                "Josh Leitz": "I"
            }
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
        node_text.append(f"{team}\n({len(data['Team Members'])} members)")
        
        # Set fixed sizes and ROYGBIV colors
        if team == "Leadership":
            node_sizes.append(180)  # Larger size for Leadership
        else:
            node_sizes.append(120)  # Standard size for all other departments
        
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
            line=dict(color='white', width=2),
            opacity=1.0
        ),
        textposition="middle center",
        textfont=dict(
            color='black',
            size=14,
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
            range=[-2.5, 3.0]
        ),
        yaxis=dict(
            showgrid=False, 
            zeroline=False, 
            showticklabels=False,
            range=[-2.5, 2.5]
        ),
        plot_bgcolor='white',
        height=800
    )
    
    return fig

def create_raci_table(selected_activity, raci_data):
    """Create a formatted RACI table for Streamlit"""
    if selected_activity not in raci_data:
        return pd.DataFrame()
    
    # Initialize empty lists for the table data
    rows = []
    
    # Process the data for the selected activity
    activity_data = raci_data[selected_activity]
    for department, members in activity_data.items():
        for person, role in members.items():
            rows.append({
                "Department": department,
                "Team Member": person,
                "Role": role,
                "Description": get_raci_description(role)
            })
    
    return pd.DataFrame(rows)

def get_raci_description(role):
    """Return description for RACI role"""
    descriptions = {
        "R": "Responsible (Does the work)",
        "A": "Accountable (Approves)",
        "C": "Consulted (Provides input)",
        "I": "Informed (Kept updated)"
    }
    return descriptions.get(role, "")

def create_workflow_diagram(selected_activity):
    """Create a Plotly-based workflow diagram"""
    workflows = {
        "Platform Feature Changes": {
            "steps": [
                "Feature Request",
                "Development Team Assessment",
                "Leadership Review",
                "Development Implementation",
                "Support Team Testing",
                "Final Approval",
                "Deployment",
                "User Communication"
            ]
        },
        "Content Updates": {
            "steps": [
                "Content Update Need",
                "Curriculum Team Review",
                "Development of Updates",
                "Quality Check",
                "Leadership Approval",
                "Implementation",
                "Documentation Update"
            ]
        }
    }
    
    if selected_activity not in workflows:
        return None
        
    steps = workflows[selected_activity]["steps"]
    n_steps = len(steps)
    
    # Create figure
    fig = go.Figure()
    
    # Calculate positions
    y_pos = 0
    spacing = 100
    
    # Add nodes and connections
    for i, step in enumerate(steps):
        # Add node
        fig.add_shape(
            type="circle",
            xref="x", yref="y",
            x0=i*spacing-20, y0=-20,
            x1=i*spacing+20, y1=20,
            line_color="#1f77b4",
            fillcolor="white"
        )
        
        # Add text
        fig.add_annotation(
            x=i*spacing, y=0,
            text=step,
            showarrow=False,
            font=dict(size=10)
        )
        
                    # Add arrow to next step
        if i < n_steps - 1:
            fig.add_annotation(
                x=i*spacing+40,
                y=0,
                xref="x",
                yref="y",
                axref="x",
                ayref="y",
                ax=(i+1)*spacing-40,
                ay=0,
                arrowhead=2,
                arrowsize=1.5,
                arrowwidth=2,
                arrowcolor="#1f77b4",
                showarrow=True
            )
    
    # Update layout
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='white',
        width=n_steps * spacing + 100,
        height=200,
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[-50, n_steps * spacing + 50]
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[-50, 50]
        ),
        margin=dict(l=20, r=20, t=20, b=20)
    )
    
    return fig

def main():
    st.markdown('<h1 style="margin-top: 0.5rem;">SchoolsPLP Organizational Structure</h1>', unsafe_allow_html=True)
    
    teams = create_team_data()
    raci_data = create_raci_data()
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Org Structure", "RACI Matrix", "Activity Workflows"])
    
    with tab1:
        col1, col2 = st.columns([3, 2])
        
        with col2:
            selected_team = st.selectbox("Select a Department:", list(teams.keys()))
            team_members = list(teams[selected_team]["Team Members"].keys())
            selected_member = st.selectbox("Select a Team Member:", team_members)
            
            if selected_member:
                member_data = teams[selected_team]["Team Members"][selected_member]
                st.markdown(f"### {selected_member}")
                st.markdown(f"**Role:** {member_data['Role']}")
                if "Responsibilities" in member_data:
                    st.markdown(f"**Responsibilities:** {member_data['Responsibilities']}")
                st.markdown(f"**Reports To:** {member_data['Reports_To']}")
        
        with col1:
            st.plotly_chart(create_team_visualization(selected_team), use_container_width=True)
    
    with tab2:
        st.markdown("### Responsibility Assignment Matrix")
        st.markdown("""
        This matrix shows who is Responsible, Accountable, Consulted, or Informed for different activities:
        - **R** (Responsible): Person who performs the work
        - **A** (Accountable): Person who makes final decisions and has ultimate ownership
        - **C** (Consulted): Person who needs to provide input before decisions
        - **I** (Informed): Person who needs to be kept updated on progress
        """)
        
        # Activity selector
        selected_activity = st.selectbox(
            "Select Activity:",
            list(raci_data.keys())
        )
        
        # Display RACI table
        raci_table = create_raci_table(selected_activity, raci_data)
        if not raci_table.empty:
            st.dataframe(
                raci_table,
                column_config={
                    "Department": st.column_config.TextColumn("Department"),
                    "Team Member": st.column_config.TextColumn("Team Member"),
                    "Role": st.column_config.TextColumn("RACI Role"),
                    "Description": st.column_config.TextColumn("Role Description")
                },
                hide_index=True
            )
            
            # Add filters
            st.markdown("### Filter View")
            selected_dept = st.multiselect(
                "Filter by Department",
                options=raci_table["Department"].unique()
            )
            
            if selected_dept:
                filtered_table = raci_table[raci_table["Department"].isin(selected_dept)]
                st.dataframe(filtered_table, hide_index=True)
    
    with tab3:
        st.markdown("### Activity Workflows")
        workflow_activity = st.selectbox(
            "Select Activity to View Workflow:",
            ["Platform Feature Changes", "Content Updates"]
        )
        
        workflow_fig = create_workflow_diagram(workflow_activity)
        if workflow_fig:
            st.plotly_chart(workflow_fig, use_container_width=True)
        else:
            st.info("Workflow diagram not available for this activity yet.")
            
        st.markdown("""
        **Understanding Workflows:**
        - Each circle represents a step in the process
        - Arrows show the progression between steps
        - Click and drag to pan, scroll to zoom
        """)

if __name__ == "__main__":
    main()
