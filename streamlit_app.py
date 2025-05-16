import streamlit as st
import pandas as pd

st.set_page_config(page_title="Сегментация клиентов", layout="wide")

cleandf=pd.read_csv('clean_dataset.csv', index_col=False)
df=pd.read_csv('final_data.csv',index_col=False)
df['customer_id']=cleandf['customer_unique_id']
df['state']=cleandf['customer_state']
st.title("Сегментация клиентов")
col1, col2 = st.columns([1.5, 3])
with col1:
    client_id = st.selectbox(
    "Выберите клиента",
    sorted(df['customer_id'].unique()),
    key="client_select"
    )
    client_data=df[df['customer_id']==client_id]
    avg_price=client_data['price'].mean()
    state=client_data['state'].to_string(index=False)
    st.subheader("📋 Информация о клиенте")
    st.metric(f"Штат",f"{state}")
    st.metric(f"Средняя стоимость заказа",f"${avg_price}")
with col2:
    risk = df[df["customer_id"] == client_id]["cluster"].values[0]
    if risk==-1:
        st.markdown("Недостаточно информации о клиенте")
    elif risk<=2:
        st.success("🔒 Низкий риск оттока - клиент лоялен")
        st.markdown("Вероятность оттока клиента")
        st.progress(1/18+risk/9)
    elif risk<=5:
        st.warning("⚠️ Средний риск оттока - требуется внимание")
        st.markdown("Вероятность оттока клиента")
        st.progress(1/18+risk/9)
    else:
        st.error("🚨 Высокий риск оттока - срочные действия!")
        st.markdown("Вероятность оттока клиента")
        st.progress(1/18+risk/9)

st.markdown("---")

st.subheader("🎯 Рекомендации для клиента")

if risk <= 2:
    st.info("""
    - Поддерживать текущий уровень сервиса
    - Предложить программу лояльности
    - Персонализированные предложения
    """)
elif risk <= 5:
    st.warning("""
    - Анализ причин снижения активности
    - Специальные предложения
    - Опрос удовлетворенности
    """)
else:
    st.error("""
    - Персональный менеджер для работы с клиентом
    - Специальные условия и скидки
    - Глубокий анализ причин оттока
    """)

st.markdown("---")
