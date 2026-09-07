import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Для Насти...",
    page_icon="🌸",
    layout="centered"
)

import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Для Насти...",
    page_icon="🌸",
    layout="centered"
)

# Кастомный CSS: тёмный фон + светлые карточки
st.markdown("""
    <style>
    /* Главный фон страницы — тёмный */
    .stApp {
        background-color: #1E1E24;
        color: #E2E2E2;
    }
    
    /* Стилизация кнопок */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3.2em;
        background-color: #E8A598;
        color: #1E1E24;
        border: none;
        font-weight: 700;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #F0B7AB;
        color: #1E1E24;
    }
    
    /* Основные текстовые карточки — светлые */
    .card {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        margin-bottom: 20px;
        color: #4A4A4A;
        line-height: 1.6;
    }
    
    /* Маленькие карточки качеств — светлые */
    .feature-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        margin-bottom: 15px;
        border: 1px solid #F0E6DF;
    }
    .feature-icon {
        font-size: 32px;
        margin-bottom: 8px;
    }
    .feature-title {
        font-weight: 600;
        color: #4A4A4A;
        font-size: 15px;
    }
    
    /* Цитата */
    .quote {
        font-style: italic;
        color: #8C7A6B;
        border-left: 3px solid #E8A598;
        padding-left: 15px;
        margin: 15px 0;
    }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 1

# --- ЭКРАН 1 ---
if st.session_state.page == 1:
    st.title("Насть, привет... 🌸")
    st.write("Я сделал эту страницу, чтобы спокойно и без лишнего шума сказать то, что чувствую.")
    
    st.markdown("""
    <div class="card">
        <p>Иногда из-за усталости и эмоционального накала мы начинаем неверно понимать друг друга. Мне очень жаль, что всё так закрутилось, и я хочу, чтобы ты просто прочитала это в тишине, когда у тебя будет время.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Прочитать дальше 💌"):
        st.session_state.page = 2
        st.rerun()

# --- ЭКРАН 2 ---
elif st.session_state.page == 2:
    st.subheader("О том, что произошло...")
    
    st.markdown("""
    <div class="card">
        <p>Я правда очень жалею, что не понял твой жест с «пальчиковыми обнимашками» и отреагировал резко. Мне невероятно больно от мысли, что я мог задеть тебя или вызвать чувство, будто твоё мнение не имеет значения.</p>
        <p>Я знаю, как много на тебе сейчас висит, как сильно ты устаёшь и сколько сложных эмоций приходится проживать каждый день. Меньше всего я хотел стать ещё одним источником стресса.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Немного тепла ✨"):
        st.session_state.page = 3
        st.rerun()

# --- ЭКРАН 3 ---
elif st.session_state.page == 3:
    st.subheader("То, за что я тебя ценю...")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">✨</div>
            <div class="feature-title">Твой свет и искренность</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🛡️</div>
            <div class="feature-title">Умение стоять за близких</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🌿</div>
            <div class="feature-title">Спокойствие и уют</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💬</div>
            <div class="feature-title">Теплота общения</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <p>Ты удивительный и невероятно чуткий человек. Твоё умение отдавать тепло, быть искренней и стоять стеной за тех, кто тебе дорог — это редчайшее качество.</p>
        <div class="quote">
            «За общим шумом и ссорами никогда не потеряется то хорошее, что между нами есть.»
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("И самое главное... ❤️"):
        st.session_state.page = 4
        st.rerun()

# --- ЭКРАН 4 ---
elif st.session_state.page == 4:
    st.title("Я ценю тебя 🤍")
    
    st.markdown("""
    <div class="card">
        <p>Я не жду, что всё мгновенно станет идеально или что ты сразу выдохнешь. Я просто хочу, чтобы ты знала: <b>я не злюсь и очень дорожу нашим общением.</b></p>
        <p>Тебе не нужно ничего отвечать прямо сейчас. Просто береги себя, дай себе время побыть с собой на едине и набраться сил.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Мои «пальчиковые обнимашки» всегда с тобой 🤏✨")