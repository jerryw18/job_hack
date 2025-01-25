import streamlit as st

# Define AI agent responses
def agent_1_response(user_input):
    return f"Agent 1 says: You entered '{user_input}'"

def agent_2_response(user_input):
    return f"Agent 2 says: You entered '{user_input}'"

def agent_3_response(user_input):
    return f"Agent 3 says: You entered '{user_input}'"

# Set up the layout
st.set_page_config(layout="wide")

# Main layout
col1, col2 = st.columns([1, 4], gap="large")

# First column: Title and buttons
with col1:
    # Title
    st.markdown(
        "<h1 style='color:white;background-color:#003366; padding: 10px; text-align:center;'>Joe</h1>",
        unsafe_allow_html=True,
    )

    # Buttons under the title
    st.markdown("<p style='color:white;background-color:#003366; padding: 5px;'>Choose an Agent</p>", unsafe_allow_html=True)

    if "selected_agent" not in st.session_state:
        st.session_state.selected_agent = "Agent 1"

    # Buttons (vertical alignment enforced with markdown spacing)
    button_1 = st.button("Agent 1")
    button_2 = st.button("Agent 2")
    button_3 = st.button("Agent 3")

    # Update selected agent based on button clicks
    if button_1:
        st.session_state.selected_agent = "Agent 1"
    elif button_2:
        st.session_state.selected_agent = "Agent 2"
    elif button_3:
        st.session_state.selected_agent = "Agent 3"

# Second column: Interaction area
with col2:
    # Dynamic title for the selected agent
    st.markdown(f"### {st.session_state.selected_agent}")

    # Input area for user to interact
    user_input = st.text_input("Enter your message:")

    # Handle user interaction
    if st.button("Send", key="send_button"):
        if st.session_state.selected_agent == "Agent 1":
            response = agent_1_response(user_input)
        elif st.session_state.selected_agent == "Agent 2":
            response = agent_2_response(user_input)
        elif st.session_state.selected_agent == "Agent 3":
            response = agent_3_response(user_input)
        else:
            response = "No agent selected."
        st.session_state.output = response  # Save response in session state

    # Display agent's response in an output box
    st.markdown("**Agent Response:**")
    if "output" in st.session_state and st.session_state.output:
        st.text_area("Agent Answer", value=st.session_state.output, height=150, key="response_box", disabled=True)
    else:
        st.text_area("Agent Answer", value="Waiting for input...", height=150, key="response_box", disabled=True)
