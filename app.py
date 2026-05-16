import streamlit as st
from huggingface_hub import InferenceClient
import base64
import random
import os
from dotenv import load_dotenv

#УЛУЧШЕННАЯ ФУНКЦИЯ ЗАГРУЗКИ
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception as e:
        print(f"Ошибка чтения файла {bin_file}: {e}")
        return ""
    
#ЗАГРУЗКА ЛОГОТИПА
logo_data = None

logo_names = ['logo.png', 'logo.PNG', 'Logo.png', 'logo.jpg', 'logo.jpeg']

print("Поиск логотипа...")

for logo_name in logo_names:
    if os.path.exists(logo_name):
        logo_data = get_base64(logo_name)
        if logo_data:  # если успешно загрузилось
            print(f"Логотип успешно загружен: {logo_name}")
            break
    else:
        print(f"   Не найден: {logo_name}")

if logo_data is None or logo_data == "":
    print("Логотип не найден.")
    logo_data = ""

#ЗАГРУЗКА ТОКЕНА ИЗ .env 
load_dotenv(".env") 

HF_TOKEN = os.getenv("HF_TOKEN")

#Инициализация клиента
client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct", token=HF_TOKEN)

#СЛУЧАЙНЫЕ ПРИМЕРЫ
examples = [
    "набрать 5кг мышц к лету", "подсушиться и убрать живот к отпуску",
    "набрать массу и стать сильнее", "похудеть на 8 кг за 3 месяца",
    "подготовиться к лету и улучшить рельеф", "увеличить силу и мышечную массу",
    "сбросить вес и улучшить выносливость", "привести тело в тонус после перерыва"
]

random_example = random.choice(examples)

#Инициализация session_state
if "goal" not in st.session_state:
    st.session_state.goal = ""

#2. ФОНЫ
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

img1 = get_base64('6.jpg')
img2 = get_base64('4.png')
img3 = get_base64('1.png')

st.set_page_config(page_title="FitGuide AI", page_icon="logo.png", layout="wide")

#3. TIFFANY СТИЛЬ
st.markdown(f"""
    <style>
    .logo-img {{
        filter: drop-shadow(0 0 15px rgba(92, 225, 214, 0.7));
        transition: 0.5s;
        animation: pulse-logo 3s infinite ease-in-out;
    }}

    @keyframes pulse-logo {{
        0%   {{ filter: drop-shadow(0 0 8px rgba(92, 225, 214, 0.5)); }}
        50%  {{ filter: drop-shadow(0 0 28px rgba(92, 225, 214, 0.95)); }}
        100% {{ filter: drop-shadow(0 0 8px rgba(92, 225, 214, 0.5)); }}
    }}

    .main-logo {{
        width: 85px;
        margin-bottom: 12px;
    }}

    .stApp {{
        background-color: #0F1C1A;
        background-image: linear-gradient(rgba(15,28,26,0.85), rgba(15,28,26,0.85)), 
                         url("data:image/png;base64,{img1}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        animation: scrollBG 45s linear infinite;
    }}

    @keyframes scrollBG {{
        0% {{ background-position: 0% 50%; background-image: linear-gradient(rgba(15,28,26,0.85), rgba(15,28,26,0.85)), url("data:image/png;base64,{img1}"); }}
        33% {{ background-position: 100% 50%; }}
        34% {{ background-position: 0% 50%; background-image: linear-gradient(rgba(15,28,26,0.85), rgba(15,28,26,0.85)), url("data:image/png;base64,{img2}"); }}
        66% {{ background-position: 100% 50%; }}
        67% {{ background-position: 0% 50%; background-image: linear-gradient(rgba(15,28,26,0.85), rgba(15,28,26,0.85)), url("data:image/png;base64,{img3}"); }}
        100% {{ background-position: 100% 50%; }}
    }}

    .stButton>button {{
        background-color: #5CE1D6 !important;
        color: #0F1C1A !important;
        border: 1px solid #45B8A9 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }}
    
    .stButton>button:hover {{
        background-color: #7AEDE4 !important;
        box-shadow: 0 0 20px rgba(92, 225, 214, 0.6) !important;
    }}

    .plan-container {{
        background: rgba(26, 42, 39, 0.92) !important;
        border: 2px solid #5CE1D6 !important;
        border-radius: 16px !important;
        box-shadow: 0 0 20px rgba(92, 225, 214, 0.25);
        padding: 28px 32px !important;
        margin-top: 20px;
        line-height: 1.65;
    }}

    .tip-container {{
        background: rgba(26, 42, 39, 0.92) !important;
        border: 2px solid #5CE1D6 !important;
        border-radius: 16px !important;
        box-shadow: 0 0 20px rgba(92, 225, 214, 0.25);
        padding: 22px !important;
    }}

    .footer {{
        position: fixed;
        bottom: 15px;
        left: 50%;
        transform: translateX(-50%);
        color: #777;
        font-size: 0.9rem;
        text-align: center;
        z-index: 100;
        width: 100%;
    }}
    </style>
    """, unsafe_allow_html=True)

#4. ГЛАВНАЯ ЧАСТЬ
st.markdown(f"""
    <div style="text-align: center; margin-top: 20px; margin-bottom: 10px;">
        <img src="data:image/png;base64,{logo_data}" class="main-logo">
    </div>
    <h1 style='text-align: center; color: white; margin: 0;'>FITGUIDE <span style="color:#5CE1D6">AI</span></h1>
""", unsafe_allow_html=True)

#Боковая панель
with st.sidebar:
    st.markdown(f"""
    <div style="text-align: center; margin-top: 20px; margin-bottom: 25px;">
        <img src="data:image/png;base64,{logo_data}" width="175" class="logo-img">
    </div>
    
    <div style="text-align: center; margin-bottom: 30px;">
        <h2 style="color: white; margin: 0; letter-spacing: -1px; font-size: 2rem;">
            FITGUIDE <span style="color:#5CE1D6">AI</span>
        </h2>
        <p style="opacity: 0.75; margin-top: 8px;">Твой персональный путь к трансформации</p>
    </div>
""", unsafe_allow_html=True)

    st.write("---")
    st.header("⚙️ ПАРАМЕТРЫ")
    weight = st.number_input("Вес (кг):", 40, 200, 75)
    height = st.number_input("Рост (см):", 100, 250, 175)
    gender = st.selectbox("Пол:", ["Мужской", "Женский"])
    body_type = st.selectbox("Телосложение:", ["Эктоморф", "Мезоморф", "Эндоморф"])
    exp = st.select_slider("Твой опыт:", options=["Новичок", "Средний", "Профи"])
    equipment = st.multiselect("Инвентарь:", ["Зал", "Гантели", "Турник", "Без инвентаря"], default=["Без инвентаря"])

st.write("---")

col_input, col_tip = st.columns([1.2, 1])

with col_input:
    #Используем session_state для сохранения введённой цели
    goal = st.text_input("Твоя цель:", 
                        placeholder=f"Например: {random_example}",
                        value=st.session_state.goal,
                        key="goal_input")

    #Обновляем session_state при изменении
    if goal != st.session_state.goal:
        st.session_state.goal = goal

    st.write("")
    btn_generate = st.button("СФОРМИРОВАТЬ ФИТНЕС-ПЛАН")

with col_tip:
    try:
        tip_prompt = """Дай один короткий, полезный и грамотный фитнес-совет на русском языке. 
        Максимум 2 предложения. 
        Пиши чистым правильным русским языком, без markdown, без специальных символов и артефактов."""

        t_res = client.chat_completion(
            messages=[{"role": "user", "content": tip_prompt}], 
            max_tokens=150,
            temperature=0.75
        )
        
        # Извлечение текста
        if hasattr(t_res, 'choices'):
            t_text = t_res.choices[0].message.content
        else:
            t_text = t_res['choices'][0]['message']['content']
        
        #💡 СОВЕТ ДНЯ
        import unicodedata
        t_text = t_text.strip()
        t_text = unicodedata.normalize('NFKC', t_text)         
        t_text = t_text.replace('\u200b', '')                   
        t_text = t_text.replace('\xa0', ' ')                   
        t_text = ''.join(c for c in t_text if ord(c) < 0xF0000) 
        
        st.markdown(f"""
        <div class="tip-container">
            <small style="color: #5CE1D6; font-weight: bold;">💡 СОВЕТ ДНЯ</small><br><br>
            <div style="font-size: 15.5px; line-height: 1.6;">{t_text}</div>
        </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.markdown('''
        <div class="tip-container">
            <small style="color: #5CE1D6; font-weight: bold;">💡 СОВЕТ ДНЯ</small><br><br>
            Регулярность важнее интенсивности. Тренируйтесь 3–4 раза в неделю.
        </div>
        ''', unsafe_allow_html=True)
#5. ГЕНЕРАЦИЯ ПЛАНА
if btn_generate:
    if not st.session_state.goal.strip():   # Проверяем через session_state
        st.warning("Пожалуйста, введите вашу цель!")
    else:
        with st.spinner("⏳ FitGuide Ultra анализирует данные..."):
            main_prompt = f"""Ты элитный тренер FitGuide и хороший друг который может что нибудь подсказать. Составь план тренировок и питания если этого попросят или ответь на вопрос клиента. Не составляй план если этого не просят
            Данные: {gender}, вес {weight}кг, рост {height}см, тип {body_type}, опыт {exp}, цель {st.session_state.goal}.
            Инвентарь: {equipment}. Отвечай строго на русском, грамотно, без ошибок."""
            
            try:
                response = client.chat_completion(messages=[{"role": "user", "content": main_prompt}])
                output = response.choices[0].message.content if hasattr(response, 'choices') else response['choices'][0]['message']['content']

                st.markdown("### ТВОЙ ПЕРСОНАЛЬНЫЙ ПЛАН")
                st.markdown(f'<div class="plan-container">{output}</div>', unsafe_allow_html=True)
                st.balloons()
                st.download_button("💾 Сохранить план в TXT", output, file_name="my_fitplan.txt")
            except Exception as e:
                st.error(f"Ошибка ИИ: {e}")

#Футер
st.markdown("""
    <div class="footer">
        FitGuide AI v1.0 | Дизайн: Звездатый | AI: Кучка китайцев
    </div>
""", unsafe_allow_html=True)