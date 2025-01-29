import streamlit as st
import plotly.graph_objects as go
from collections import defaultdict

# Set page configuration
st.set_page_config(page_title="SchoolsPLP Team Connections", layout="wide")

# [Previous create_team_data() function remains the same]

def create_team_visualization(selected_team=None):
    teams = create_team_data()
    
    # Create nodes (teams)
    node_x = []
    node_y = []
    node_text = []
    node_colors = []
    node_sizes = []
    
    for team, data in teams.items():
        node_x.append(data["Position"][0])
        node_y.append(data["Position"][1])
        node_text.append(team)
        
        # Highlight selected team and its direct collaborators
        if selected_team:
            if team == selected_team:
                node_colors.append('#1f77b4')  # Primary blue for selected team
                node_sizes.append(50)
            elif team in teams[selected_team]["Key Collaborations"]:
                node_colors.append('#7fB3ff')  # Lighter blue for collaborators
                node_sizes.append(40)
            else:
                node_colors.append('#E1E5E8')  # Gray for other teams
                node_sizes.append(35)
        else:
            node_colors.append('lightblue')
            node_sizes.append(40)
    
    # Create edges (collaborations)
    edge_x = []
    edge_y = []
    edge_colors = []
    
    for team, data in teams.items():
        x0, y0 = data["Position"]
        for collab in data["Key Collaborations"]:
            if collab in teams:
                x1, y1 = teams[collab]["Position"]
                edge_x.extend([x0, x1, None])
                edge_y.extend([y0, y1, None])
                
                # Highlight connections of selected team
                if selected_team and (team == selected_team or collab == selected_team):
                    edge_colors.extend(['#1f77b4', '#1f77b4', '#1f77b4'])  # Blue for active connections
                else:
                    edge_colors.extend(['#E1E5E8', '#E1E5E8', '#E1E5E8'])  # Gray for other connections
    
    # Create the visualization
    fig = go.Figure()
    
    # Add edges
    fig.add_trace(go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(color=edge_colors, width=2),
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
            size=node_sizes,
            color=node_colors,
            line_width=2,
            line=dict(color='white')
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
        plot_bgcolor='white',
        height=500
    )
    
    return fig

def main():
    st.title("SchoolsPLP Team Connections")
    
    teams = create_team_data()
    
    col1, col2 = st.columns([3, 2])
    
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
        The visualization will update to show the selected team's connections.
        """)
    
    with col1:
        # Create visualization with selected team
        st.plotly_chart(create_team_visualization(selected_team), use_container_width=True)
        
        st.markdown("""
        **Understanding Team Connections:**
        - Selected team is shown in dark blue
        - Direct collaborators are shown in light blue
        - Active collaboration paths are highlighted
        - Other teams and connections are shown in gray
        """)

if __name__ == "__main__":
    main()
