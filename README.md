# FitGuide AI

**Цифровой ассистент для персонализированных фитнес-рекомендаций на базе Llama-3-8B-Instruct**

## О проекте
Курсовая работа по дисциплине **"Машинное обучение"**.  
Реализован интеллектуальный веб-ассистент, который рассчитывает BMR/TDEE и генерирует персональные планы тренировок и питания с помощью большой языковой модели.

## Стек технологий
- **Frontend**: Streamlit
- **LLM**: Meta-Llama-3-8B-Instruct (Hugging Face Inference API)
- **Язык**: Python 3.10+
- **Контроль версий**: Git + GitHub

- ⸻

 - ## Анализ данных

**Jupyter Notebook:** [FitGuide_Анализ_данных.ipynb](fitguide.ipynb)

В рамках ИДЗ выполнен анализ синтетических данных пользователей приложения. 
Проведены: предобработка данных, визуализация, корреляционный и регрессионный анализ.

## Как запустить локально

```bash
git clone https://github.com/Kolumba05/FitGuide-AI.git
cd FitGuide-AI
pip install -r requirements.txt
streamlit run app.py

