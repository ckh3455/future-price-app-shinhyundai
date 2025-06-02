#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import numpy as np
import datetime

# 🌟 기본 데이터 (연도별 거래가)
historical_data = {
    2015: 15.3,
    2016: 19.35,
    2017: 23.7,
    2018: 26.7,
    2019: 29,
    2020: 30,
    2021: 36,
    2022: None,  # 거래 없음
    2023: 44,
    2024: 51,
    2025: 69.7
}

# 🚀 Streamlit 앱 시작
st.title("압구정동 신현대 35평 미래가격 예측 앱")
st.write("현재 입력된 데이터와 연평균 성장률(CAGR)을 이용해 목표 금액 도달 시점을 예측합니다.")

# 📥 사용자 입력
current_year = st.number_input("현재 연도 (예: 2025)", min_value=2015, max_value=2100, value=2025)
current_month = st.number_input("현재 월 (1~12)", min_value=1, max_value=12, value=6)
current_day = st.number_input("현재 일 (1~31)", min_value=1, max_value=31, value=2)
current_price = st.number_input("현재 거래가 (억)", min_value=1.0, value=69.7)
target_price = st.number_input("목표 금액 (억)", min_value=1.0, value=100.0)

if st.button("예측하기"):
    # 🧮 CAGR 계산
    initial_year = 2015
    initial_price = historical_data[2015]
    years_elapsed = current_year - initial_year
    if years_elapsed == 0:
        st.error("CAGR 계산 불가: 연도 차이가 없습니다.")
    else:
        cagr = (current_price / initial_price) ** (1 / years_elapsed) - 1

        # ⏳ 목표 금액 도달 시점 계산
        if cagr <= 0:
            st.warning("CAGR가 0 이하로 예측 불가")
        else:
            years_needed = np.log(target_price / current_price) / np.log(1 + cagr)
            predicted_date = datetime.date(current_year, current_month, current_day) + datetime.timedelta(days=int(years_needed * 365))

            # 📅 결과 출력
            st.success(f"예상 도달 시점: **{predicted_date}**")
            st.info(f"계산된 CAGR: **{cagr:.2%}**")

# 📊 참고: 연도별 데이터 출력
if st.checkbox("연도별 데이터 보기"):
    st.write(historical_data)

