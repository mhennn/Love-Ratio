import streamlit as st
import time
from core.love_calculation import RatioCalculation
from streamlit_extras.let_it_rain import rain

class UiApp:
    def __init__(self):
        self.DIGITS = [1,2,3,4,5,6,7,8,9,0]
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

            self.how_long = st.text_input("How long you've known each other?", key="talking_stage", help="Number of days").replace('.','')
            self.hours_talking = st.text_input("How long you spent talking to each other everyday?", key="talking_hours", help="Number of hours").replace('.','',1)
            
            if self.how_long and self.hours_talking:
                try:
                    if int(self.how_long) in self.DIGITS and int(self.hours_talking) in self.DIGITS:
                        pass
                except ValueError:
                    st.warning("Input number Only.")
                else:
                    if st.button("Calculate"):
                        self.calculate_love(self.hours_talking, self.how_long)
                        if self.love_loading():
                            st.text_input(f"{self.your_name} and {self.talking_partner} have", value=f"{self.interaction_love} LOVE RATIO 💝", key="interaction_result")
                            st.text_input(f"{self.your_name} and {self.talking_partner} spent", value=f"{self.available_ratio} most of the time talking everyday ⏰", key="available_result")
                            if self.ratio_calculation.talking_ratio >= 50 and self.ratio_calculation.available_life_ratio >= 50:
                                self.rain_both()
                            elif self.ratio_calculation.talking_ratio >= 50 and self.ratio_calculation.available_life_ratio <50:
                                self.rain_one()
                            elif self.ratio_calculation.talking_ratio < 50 and self.ratio_calculation.available_life_ratio >= 50:
                                self.rain_one()
                            else:
                                self.rain_none()
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
    
    def rain_both(self):
        rain("💘💝", font_size=54, falling_speed=5, animation_length=2)

    def rain_one(self):
        rain("💘🙂", font_size=54, falling_speed=5, animation_length=2)
    
    def rain_none(self):
        rain("🥲😭", font_size=54, falling_speed=5, animation_length=2)