import streamlit as st
import time
from core.love_calculation import RatioCalculation

class UiApp:
    def __init__(self):
        st.markdown(
            '<h1>Love Ratio 💞</h1>',
            unsafe_allow_html=True
        )
        st.set_page_config(
            page_title="Love Ratio",
            page_icon="💞",
        )
        st.markdown(
            "<h6>You're in talking stage? Find out your Love Ratio 💘</h6>",
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <style>
            .stProgress > div > div > div > div {
                background-color: #FF4B4B;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        self.container = st.container(border=True)
        self.ratio_calculation = RatioCalculation()
        self.ratio_counter()

    def ratio_counter(self):
        with self.container:
            self.talking_partner = st.text_input("Who got your attention right now? 😻", key="partner")
            self.your_name = st.text_input("And you are?", key="lover")

            self.how_long = st.text_input("How long you've known each other?", key="talking_stage", help="Number of days")
            self.hours_talking = st.text_input("How long you spent talking to each other everyday?", key="talking_hours", help="Number of hours")
            
            if self.how_long and self.hours_talking:
                if st.button("Calculate"):
                    self.calculate_love(self.hours_talking, self.how_long)
                    if self.love_loading():
                        st.text_input(f"{self.your_name} and {self.talking_partner} have", value=f"{self.interaction_love} LOVE RATIO 💝", key="interaction_result")
                        st.text_input(f"{self.your_name} and {self.talking_partner} spent", value=f"{self.available_ratio} most of the time talking everyday ⏰", key="available_result")
            else:
                st.warning("Enter hours and days")

    def calculate_love(self, hours, days):
        self.interaction_love = self.ratio_calculation.interaction_ratio(days, hours)
        self.available_ratio = self.ratio_calculation.available_life(hours)

    def love_loading(self):
        progress_text = "Calculating Love Ratio..."
        love_bar = st.progress(0, text=progress_text)

        for ratio in range(100):
            time.sleep(0.2)
            love_bar.progress(ratio + 1, text=progress_text)
        time.sleep(1)
        st.success("Calculating Love Ratio Completed 💌")
        return True