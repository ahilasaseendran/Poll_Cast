import streamlit as st

# Set Streamlit page configuration
st.set_page_config(
    page_title="POLL CAST",
    page_icon="🌟",
    layout="centered"
)

# Add custom CSS for background and theme
def apply_custom_css():
    st.markdown("""
        <style>
        /* Background color */
        body {
            background-color: #f0f2f6;
        }

        /* Background image */
        .stApp {
            background: url("https://www.voxco.com/wp-content/uploads/2021/09/Opinion-Polls1.png");
            background-size: cover;
            background-position: center;
        }

        /* Font settings */
        .css-18e3th9 {
            font-family: 'Verdana', sans-serif;
            color: #333333;
        }

        /* Title styling */
        .css-12ttj6m {
            color: #1f4e79;
            font-size: 2.5em;
            font-weight: bold;
        }

        /* Sidebar styling */
        .css-1d391kg {
            background-color: #003366 !important;
        }

        /* Sidebar text */
        .css-1d391kg h2 {
            color: yellow !important;
        }

        /* Button customization */
        button {
            background-color: #4CAF50 !important;
            border: none;
            color: white !important;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

# Apply the custom CSS
apply_custom_css()

# Poll options and vote storage
poll_options = {'Option 1': 0,'Option 2': 0, 'Option 3': 0,'Option 4': 0}
poll = poll_options.items()

# Function to save poll results to a file
def save_results():
    try:
        with open("poll_results.txt", "w") as obj1:
            for option, votes in poll:
                obj1.write(f"{option}: {votes} votes\n")
    except Exception as e:
        st.error(f"Error saving results: {e}")

# Function to load poll results from a file
def load_results():
    try:
        with open("poll_results.txt", "r") as obj2:
            lines = obj2.readlines()
            for i in lines:
                options, votes = i.strip().split(': ')
                poll_options[options] = int(votes.split()[0])
    except FileNotFoundError:
        pass
    except Exception as e:
        st.error(f"Error loading results: {e}")

# Function to reset poll results
def reset_results():
    for i in poll_options.keys():
        poll_options[i] = 0
    save_results()

# Main function for the Polling App
def main():
    st.title("🌟 POLL CAST")
    st.markdown("### Vote for Your Favorite Option")

    # Load results if available
    load_results()

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page", ("Vote", "Results"))

    # Buttons for refresh and reset
    st.sidebar.button("Refresh Results", on_click=load_results)
    if st.sidebar.button("Reset Poll"):
        reset_results()
        st.success("Poll has been reset.")

    if page == "Vote":
        vote = st.radio("Choose an option:", list(poll_options.keys()))
        if st.button("Vote"):
            poll_options[vote] += 1
            st.success(f"You voted for: {vote}")
            save_results()

    elif page == "Results":
        st.subheader("Current Poll Results")
        for option, votes in poll_options.items():
            st.write(f"{option}: {votes} votes")
        st.bar_chart(poll_options)

    st.markdown("### Thank you for participating!")

if __name__ == "__main__":
    main()
