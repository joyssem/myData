import streamlit as st
import pandas as pd
import plotly.express as px
 
# 데이터 로드
@st.cache_data
def load_data():
    df = pd.read_csv("korea_number.csv")
    return df
df = load_data()

# 제목
st.title("🌍 한국의 지역별 인구수")
st.markdown("📊 **한국의 지역별 인구수 시각화한 대시보드입니다.**")

# 탭 구성
tab1, tab2, tab3 = st.tabs(["🌐 세계지도 시각화", "🏆 상위 국가 그래프", "📈 상관관계 분석"])

# 🌐 탭1: 행복 점수 세계지도
with tab1:
    st.subheader(" 지역별 인구수")
    fig_map = px.choropleth(
        df,
        locations="행정기관",
        locationmode="전체",
        color="전체",
        hover_name="행정기관",
        color_continuous_scale="YlGnBu",
        title="2024 세계 행복 점수"
    )
    st.plotly_chart(fig_map, use_container_width=True)

# 🏆 탭2: 행복 점수 상위 10개국 그래프
with tab2:
    st.subheader("상위 10개국")
    top10 = df.sort_values("행정기관", ascending=False).head(10)
    fig_bar = px.bar(
        top10,
        x="전체",
        y="행정기관",
        orientation="h",
        color="전체",
        color_continuous_scale="Blues",
        title="상위 10개국"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# 📈 탭3: 행복 요소 간 상관관계 분석
with tab3:
    st.subheader("요인 간 관계 보기")
    numeric_cols = ["전체", "남자", "여자",
                    "65세이상 전체", "65세이상 남자",
                    "65세이상 여자"]

    selected_x = st.selectbox("X축 변수", numeric_cols, index=1)
    selected_y = st.selectbox("Y축 변수", numeric_cols, index=0)

    fig_scatter = px.scatter(
        df,
        x=selected_x,
        y=selected_y,
        text="Country",
        trendline="ols",
        title=f"{selected_x} vs {selected_y}"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.markdown("📌 선형 추세선을 통해 변수 간 관계를 시각적으로 파악할 수 있습니다.")
