import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import streamlit as st
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
})

# Add a column for radio button selection
df['Select'] = False

# Display the dataframe with a radio button column
edited_df = st.data_editor(
    df,
    column_config={
        "Select": st.column_config.CheckboxColumn(
            "Select",
            help="Select a single row",
            default=False
        )
    },
    disabled=["Name", "Age", "City"],
    hide_index=True,
)

# Create a button to modify the selected row
if st.button("Modify Selected Row"):
    selected_row = edited_df[edited_df['Select']].index
    if len(selected_row) == 1:
        st.write("Modifying row:", selected_row[0])
        # Add your modification logic here
    else:
        st.warning("Please select exactly one row to modify.")
