# import streamlit as st
#
# # Poll options and vote storage
# poll_options = {'Option 1': 0,'Option 2': 0, 'Option 3': 0,'Option 4': 0}
# poll=poll_options.items()
#
# # Function to save poll results to a file
# def save_results():
#     try:
#         with open("poll_results.txt", "w") as obj1:
#             for option,votes in poll: #unpack
#                 obj1.write(f"{option}: {votes} votes\n")
#     except Exception as e:
#         st.error(f"Error saving results: {e}")
#
# # Function to load poll results from a file
# def load_results():
#     try:
#         with open("poll_results.txt", "r") as obj2:
#             lines = obj2.readlines() # ["Option 1: 0 votes\n" ,"Option 2: 0 votes\n"," Option 3: 0 votes\n"," Option 4: 0\n"]
#             for i in lines:
#                 options,votes = i.strip().split(': ')
#                 poll_options[options] = int(votes.split()[0])
#     except FileNotFoundError:
#         pass  # If file doesn't exist, continue with default values
#     except Exception as e:
#         st.error(f"Error loading results: {e}")
#
# # Function to reset poll results
# def reset_results():
#     for i in poll_options.keys():
#         poll_options[i] = 0
#     save_results()  # Save reset results to file
#
# # Main function for the Polling App
# def main():
#     st.title("POLL CAST")
#     st.markdown("### Vote for Your Favorite Option")
#
#     # Load results if available
#     load_results()
#
#     # Sidebar for navigation
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Select a page", ("Vote", "Results"))
#
#     # Buttons for refresh and reset
#     st.sidebar.button("Refresh Results", on_click=load_results)
#     if st.sidebar.button("Reset Poll"):
#         reset_results()
#         st.success("Poll has been reset.")
#
#     if page == "Vote":
#         # Radio button to choose the poll option
#         vote = st.radio("Choose an option:", list(poll_options.keys()))
#
#         # Button to submit the vote
#         if st.button("Vote"):
#             poll_options[vote] += 1
#             st.success(f"You voted for: {vote}")
#             save_results()  # Save results after voting
#
#     elif page == "Results":
#         # Display the current poll results
#         st.subheader("Current Poll Results:")
#         for option, votes in poll_options.items():
#             st.write(f"{option}: {votes} votes")
#
#         # Display the results as a bar chart
#         st.bar_chart(poll_options)
#
#     # Additional information
#     st.markdown("### Thank you for participating!")
#
# if __name__ == "__main__":
#     main()









#
#
#
#
#
# import streamlit as st
#
# # Set Streamlit page configuration
# st.set_page_config(
#     page_title="POLL CAST",
#     page_icon="🌟",
#     layout="centered"
# )
#
# # Add custom CSS for background and theme
# def apply_custom_css():
#     st.markdown("""
#         <style>
#         /* Background color */
#         body {
#             background-color: #f0f2f6;
#         }
#
#         /* Background image */
#         .stApp {
#             background: url("EBQEHBQAAAAAAAQIDBBEFEhMxMjRxFCFBUYHBBjORsWFyodHwIhVCUmKisuEjQ4KS8f/aAAwDAQACEQMRAD8A+oktUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACShRdd3RuyX8p5VVEb2dFE1zlCfi+fw7WY7Slt7NWcXz+HaxtKTs1ZxfP4drG0pOzVnF8/h2sbSk7NWcXz+HaxtKTs1bxWsc6S3zuuXYz2K4mcmFdiqmM5VzJqAAAAAAAe6KvlFPJvo4nk7mVEZ1Q3XAx7sdiI2tKz1KfI4GPdjsQ1pNSnyOBj3Y7ENaTUp8jgY92OxDWk1KfI4GPdjsQ1pNSnyOBj3Y7ENaTUp8mjnyN+LxJUKud7AeAAAAAAAAAAAAAAAAAAAu7l5z0fU13dyTheKWzNCcAAAACvuhzcvl+5GdviacR8uf54tOSFcAAAAAAA90M+OnHE8q3Syo4o6w3pFWoAAAAAGhqZX4vElxuVNW+XkPAABPY6Kryud91zfIY11ZQ22aIrqyld4uh2y2o1bWUnstBxdDtltQ2snZaDi6HbLahtZOy0HF0O2W1DaydloOLodstqG1k7LQjtFhjTi2nK9LraPabkzOTC5h6aaZmGvNyIAAAAAAAu7l5z0fU13dyTheKWzNCcAAAACvuhzcvl+5GdviacR8uf54tOSFcAAAAAAA90M+OnHE8q3Syo4o6w3pFWoAAAAAGgnlfi8SXG5U1b5YDwAAW9zM/5XijXc3JGG421NCeAAAACG2c3LwMqOKGq9wS0pJVoAAAAAACeyV/07bavvVxjXTrQ22rmpOa3xku69qNeylI7VHkcZLuvahspO1R5HGS7r2obKTtUeRxku69qGyk7VHkcZLuvahspO1R5MV7QrRSndyNOPI9JCmnVqh5Xdiu3OX872uNyGXALgFwC4AAA9Upb2UW8iknsZ5O57TOVUSzWqurJyfX9F2CIyjJ7XVNU5y8HrEAAAAAAAAAW9zM/5XijXc3JGG421NCeAAAACG2c3LwMqOKGq9wS0pJVoAAAAAAAAAAAAADKd1/7/wA3gzSWXPjpIxq3SztccN2RloAAIrVmT0JYGVO+Gu7wS0hJVgAAAAAA9iM3mYe6rzMGqZg1TMMWSKpUuaS7yT8yDexWVcU0/wCKIn1T7OEzomuv/DMx1h7hNTydtxKt3abkTNPh3Il21VbmIq8Yz+q1YqipScn1Qfm71yHtcZxkys1RTMzLP66p2/RDZ0naLnmx+uqdv0Q2dJ2i55n66p2/RDZ0naLnmfrqnb9ENnSdoueZ+uqdv0Q2dJ2i55sVLXOorm+R/sj2KIhjVerqjKZQGTWAAAAAAAAAAAAAAidXl/bet7GQoxlM1/5cpn6SnTgqot/5s4j6ws2WSU4vqvTvJczrU5wi0Rq3IifCW44eHej/AHI0as+Sw2lHmcPDvR/uQ1Z8jaUeZw8O9H+5DVnyNpR5vFepGcJ3NP8AwSyNPqFMTEwxrrpmicp8GmJKtAMSlvdtxhXcpoy1vGcvqzt26q89XwjP6PFKrvkr8rv5PBmjDYmLlNOtvnP9JSMThZt11avDGX6wkJSIAEZ07mMsmTwAAYNTNVqu6XzIob9WWIn80S6DD0a2Hj8swjo1nHepdc3f4GWExNVOpRHjM5/o8xmFpq165/u0xl+q8XigAAAAAAAAAAAAAAAAAAAAAD14o1JXX6LX1OYmvLPpMfWXVU0Z5dYn6Qms1VzbXUoxw5S3weIm5VNHhER9u9T43Dxbpivxqmr79ywT1cAAMxk45OtNeTGT2JmNzAeAEdd3JeKIOPnKimfxhP0fGdyqPwlTVTg+XsjLa2VVm/s8pjwifrMyuL2H2mdM+Mx9IiF2lLfRTeVpMv7Nc126ap3zEOdv0RRcqpjdEzD2bGoMonJ5kDWkyBrSZA1pMnmUt6QbmJm1cyuR/TO6f3TbWFi9bztz/VG+J9lS0O9spsXVFV6qYXmDpmmzTEwgpZ8dJGGF+fR1bMX8ivpLaHUOTAAHujTdaSisr7fA8mcozZUUzVOULPF0+2P1MNrDf2WrzOLp9sfqNrB2WrzOLp9sfqNrB2WrzQWig6Dudz5L+Qypq1mm5bmicpRGTAAAAAAAAAAAAHly3uXIQqsTVZuZXeGd0/unUYam9bztcUb4/ZQqlBXPfLoqO6Ie9z8svBepZaJ4q/RWaX4aPVeLpRAGJS3uUwruU0RnV/M2du3VXOVP8yZM2AAZhd19WdTe2Wpo1o19yCvK9Xdd5UYrFRdtasxlVE7vquMJhZtXdaJzpmN/0UahVSt4bGz5kdFYHU4b5NHSPs5PFfOr6z90huaAAAAAYavMLtum5TNNTZau1W6oqpUqy3ruOZvW5t1zRPg6ixci5RFceKKhHfTjd1O/yM8FRNV+nLw72GNrinD1Z+Pd9WzOmcsAALG5/OR88GYXOFusfMhuCOsQABrN1M5aPqb7W5BxXFCkbEYAAAAAAAAAAAGJLfchru2qbtOrU2WrtVqrXpa+qctVGUzDrKJziJS7nxzn4L82ltoqjuqr9P59VRpevvpo9f59Fwt1MAQWh3NeWJU4+rK5T0j/AHLjR1OdqrrP+15s1a9739pSv+bIZ4HEa0xb6z/qa8fhtWJudKcv/FZLNVgENojyXlXpKzTqxc8dy20Zeq1ptzu39FCoUkr2Gzpx3iS7EkdZao1KIp8oiHIXa9e5VV5zMvRm1gESrcuxLxd/8EKjGU1V5eHdEdZz/ZOuYKqmjPx75npGX7pSaggAC/PcinPlbntj/BV3cLRcqmqc+9e2r9VqiKI3Q8x3Hp0b5Jzv3ryuP8GVjDU2a9anowxN2b1vVq6qRZKUAAS2apwUlLsT23ch5VGcZM7dWrVmm4wn8OxmGzht7TWcYT+HYxs4O01nGE/h2MbODtNaCvWdd3u7JdyGdNMRuaq7k1znKM9YAAAAAAAAAAAAr23dGjuVHhrQ97SU4pveynldy5Fymy3aruzq0byKqaZiatyo/brcZ/1r/bVf+pj/AGHen/tx/pT/AO07cf35/VmHtfubbpQo2aX+ZOokkqFSF/I8raSM6dGXrFM1TTER+Ex7I9/F272WU5y2RqaGGa7uvq/0b2y1qa3/AFN32/FVtMt8UWMv7WYnLKY7pdBgrGxpmM84nvjoisWf8rxRloz5/pPsx0r8iOsfaWwL9zoBLZ7TRpXqrc3emr4b7kKfSGksJZr2V6e/fllM+y1wGHu1U69H3SO12N/0w/0v/Cv/ALW0b5x/6z+yw2GJ8/1QVKsK0pOnm3rqu6uwvMFjbWKomq1OcR3ePupMXYqs15VRlm8kxFDyKo1tXPvezTOrrZdzX1J71+d+w5jazTVnHhOf0z/d1eyiunKfGMvrl+y3ZnfCPXyHQYOZmxTM+TnMbERfriPNKSEZBb+aqaDwNlrjgczeWTIvA6exc1T1ccCsuccsUxgI6zuRExtc0W8488vumYG3Fd3KfLP9YR0K1/I/BeUVeacHiYnKiekelMZt2Nwsxncj8Zn1qnJYLFWgAAAAAAAAAAAAAAADmveJ0CprKX3osNGcxHr9mq9wS+SnSIDcex/T7NrlgyLjeXr6Ntnjh9nOVTwDxVsdSsk4Rck+u9FPpCxVXciaI6rvRt3VtzFc9Hiz2GpQblOLirkr711v9vI90dYqormquMvL3NJ3YrtxFM92ff7Ji3UgBQtud5I+e/E3O+kOo0Ty8dZQHPrJdsOa9L0O7+FeWr/N7Q53TPzaenusnTqd5mr/ABI+IsbSM6e6qN0pOHv7Ocqu+md8NfWOaq397qKN3cu2ZXQj4HS4SmYsUxPk5fGVRVfrmPNKSEZBb+aqaDwNlrjgcyWb0A6exc1T1ccCruccvExgILRLkuKfG3qpo2dcd+fpMLrA2KYr2lE92WX4xKtZucXngRMBzFPr9pTNIctV6feGwOjcyAAAAAAAAAAAAAAAAOa94nQKmspfeiw0ZzEev2ar3BL5KdIgNx7H9Ps2uWDIuN5evo22eOH2c5VPAK/GVWjfGMrkm7lvYvrJEWKKozmGVN+umMok4yq1roylenJXrexXWJsUUxMxBVfrqjKZWCOxAKFtzvJHz34m530h1GieXjrKA59ZLthzXpeh3fwry1f5vaHO6Z+bT091k6dTikotOWber/C/lPcpnugziO+rclk7HLKn/wAhBnRdM76f1/5WkaViN1X6f8I5zhNvg8xXJZez9ybFE0RESra66a6pmlgMUFv5qpoPA2WuOBzJZvQDp7FzVPVxwKu5xy8TGAyrLK1JqN16uyu7KQsda2lERG9YaOr1LkzO54huXUoNzklck8jIeCwtVu7rV/yU7H34rs6tPr0/+5PRcqEAAAAAAAAAAAAAAAAc17xOgVNZS+9FhozmI9fs1XuCXyU6RAbj2P6fZtcsGRcby9fRts8cPs5yqeAaytnS0niTqOGGElHOjpLEV8MkNmQWYBQtud5I+e/E3O+kOo0Ty8dZQHPrJdsOa9L0O7+FeWr/ADe0Od0z82np7rJ06nR181/nWZ2+KGFzhlSJaMtWTI/H0I97e32tyc0tqC381U0HgbLXHA5ks3oB09i5qnq44FXc45eJjAeoTcMja8G0ZRETvS8Pul6lVlLkcpNdjbPdWPJuq3SjMFcAAAAAAAAAAAAAAAAOa94nQKmspfeiw0ZzEev2ar3BL5KdIgNx7H9Ps2uWDIuN5evo22eOH2c5VPANZWzpaTxJ1HDDCSjnR0liK+GSGzILMAoW3O8kfPfibnfSHUaJ5eOsoDn1ku2HNel6Hd/CvLV/m9oc7pn5tPT3WTp1Ojr5r/Oszt8UMLnDKkS0ZasmR+PoR729vtbk5pbUFv5qpoPA2WuOBzJZvQDp7FzVPVxwKu5xy8TGAIzpSsPulkyb53MGpXAAAAAAAAAAAAAAAADmveJ0CprKX3osNGcxHr9mq9wS+SnSIDcex/T7NrlgyLjeXr6Ntnjh9nOVTwDWVs6Wk8SdRwwwko50dJYivhkhsyCzAKFtzvJHz34m530h1GieXjrKA59ZLthzXpeh3fwry1f5vaHO6Z+bT091k6dTo6+a/wA6zO3xQwucMqRLRlqyZH4+hHvb2+1uTmltQW/mqmg8DZa44HMlm9AOnsXNU9XHAq7nHLxMYAjOlKw+6WTJvncwalcAAAAAAAAAAAAAAAAOa94nQKmspfeiw0ZzEev2ar3BL5KdIgNx7H9Ps2uWDIuN5evo22eOH2c5VPANZWzpaTxJ1HDDCSjnR0liK+GSGzILMAoW3O8kfPfibnfSHUaJ5eOsoDn1ku2HNel6Hd/CvLV/m9oc7pn5tPT3WTp1Ojr5r/Oszt8UMLnDKkS0ZasmR+PoR729vtbk5pbUFv5qpoPA2WuOBzJZvQDp7FzVPVxwKu5xy8TGAIzpSsPulkyb53MGpXAAAAAAAAAAAAAAAADmveJ0CprKX3osNGcxHr");
#             background-size: cover;
#             background-position: center;
#         }
#
#         /* Font settings */
#         .css-18e3th9 {
#             font-family: 'Verdana', sans-serif;
#             color: #333333;
#         }
#
#         /* Title styling */
#         .css-12ttj6m {
#             color: #1f4e79;
#             font-size: 2.5em;
#             font-weight: bold;
#         }
#
#         /* Sidebar styling */
#         .css-1d391kg {
#             background-color: #003366 !important;
#         }
#
#         /* Sidebar text */
#         .css-1d391kg h2 {
#             color: yellow !important;
#         }
#
#         /* Button customization */
#         button {
#             background-color: #4CAF50 !important;
#             border: none;
#             color: white !important;
#             padding: 10px 20px;
#             text-align: center;
#             text-decoration: none;
#             display: inline-block;
#             font-size: 16px;
#             margin: 4px 2px;
#             cursor: pointer;
#         }
#         </style>
#     """, unsafe_allow_html=True)
#
# # Apply the custom CSS
# apply_custom_css()
#
# # Poll options and vote storage
# poll_options = {'Option 1': 0,'Option 2': 0, 'Option 3': 0,'Option 4': 0}
# poll = poll_options.items()
#
# # Function to save poll results to a file
# def save_results():
#     try:
#         with open("poll_results.txt", "w") as obj1:
#             for option, votes in poll:
#                 obj1.write(f"{option}: {votes} votes\n")
#     except Exception as e:
#         st.error(f"Error saving results: {e}")
#
# # Function to load poll results from a file
# def load_results():
#     try:
#         with open("poll_results.txt", "r") as obj2:
#             lines = obj2.readlines()
#             for i in lines:
#                 options, votes = i.strip().split(': ')
#                 poll_options[options] = int(votes.split()[0])
#     except FileNotFoundError:
#         pass
#     except Exception as e:
#         st.error(f"Error loading results: {e}")
#
# # Function to reset poll results
# def reset_results():
#     for i in poll_options.keys():
#         poll_options[i] = 0
#     save_results()
#
# # Main function for the Polling App
# def main():
#     st.title("🌟 POLL CAST")
#     st.markdown("### Vote for Your Favorite Option")
#
#     # Load results if available
#     load_results()
#
#     # Sidebar for navigation
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Select a page", ("Vote", "Results"))
#
#     # Buttons for refresh and reset
#     st.sidebar.button("Refresh Results", on_click=load_results)
#     if st.sidebar.button("Reset Poll"):
#         reset_results()
#         st.success("Poll has been reset.")
#
#     if page == "Vote":
#         vote = st.radio("Choose an option:", list(poll_options.keys()))
#         if st.button("Vote"):
#             poll_options[vote] += 1
#             st.success(f"You voted for: {vote}")
#             save_results()
#
#     elif page == "Results":
#         st.subheader("Current Poll Results")
#         for option, votes in poll_options.items():
#             st.write(f"{option}: {votes} votes")
#         st.bar_chart(poll_options)
#
#     st.markdown("### Thank you for participating!")
#
# if __name__ == "__main__":
#     main()


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