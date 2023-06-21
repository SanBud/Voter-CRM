import streamlit as st
from typing import Callable


class AddDistrict:
    def __init__(self,get_states: Callable[[str], bool], on_submit: Callable[[str, str], bool]):
        st.header("Add New District")
        states=get_states()
        state_details = {state["State_Name"]: {key: value for key, value in state.items() if key != "State_Name"} for state in states}
        if states is not None:
            state_names = [state["State_Name"] for state in states]
            form = st.form("new_district")
            selected_state = form.selectbox("Select a State", state_names)
            district_name = form.text_input("District name")
            District_No = form.text_input("District Number")
            State_Code = state_details[selected_state]['State_Id']

            if form.form_submit_button("Add New District"):
                success = on_submit(district_name,District_No,State_Code)
                if success:
                    st.success("District Added Successfully")
                else:
                    st.error("Error adding District")
        else:
            st.error("States Record is empty! Please add a state to add districts.")