# import necessary libraries
import streamlit as st
import pandas as pd
import joblib

# load simple logistic regression trained model
import os
model_path = os.path.expanduser("~/simple_diabetes_model.pkl")
model = joblib.load(model_path)

# translation dictionary (English/French/Chinese/Korean)
# these are all languages i can understand to some degree
# and i wanted to make sure the app is accessible to a wider audience
# in a real-world app, there would be even more languages and a comprehensive localization strategy
translations = {
    "en": {
        "title": "Diabetes Risk Predictor",
        "age": "Age",
        "bmi": "BMI",
        "general_health": "General Health (1 = Excellent, 5 = Poor)",
        "submit": "Predict Risk",
        "result": "Your predicted risk of diabetes is:",
        "highbp": "High Blood Pressure",
        "highchol": "High Cholesterol",
        "physhlth": "Physically Unhealthy Days (past 30 days)",
        "smoker": "Smoker",
        "physactivity": "Physically Active (past 30 days)",
        "feature_influence": "📈 Feature Influence",
        "feature_names": {
        "Age": "Age",
        "BMI": "BMI",
        "GenHlth": "General Health",
        "HighBP": "High Blood Pressure",
        "HighChol": "High Cholesterol",
        "PhysHlth": "Physically Unhealthy Days",
        "Smoker": "Smoker",
        "PhysActivity": "Physical Activity"
    },
        "model_info": "🧪 This model was trained on U.S. health survey data and achieved **86.13% test accuracy**.",
        "disclaimer": "⚠️ This tool is not a diagnosis. It's based on population data and intended for educational purposes only.",
        "logistic_info_title": "📘 What is Logistic Regression?",
        "logistic_info": """
        Logistic Regression is a machine learning algorithm used to estimate the probability that a given input belongs to a particular category.

        In this case, it estimates the probability that a person has diabetes based on self-reported health and lifestyle factors.

        In contrast to linear regression, which predicts a continuous number, logistic regression predicts a value between 0 and 1 that represents a probability.

        The model also assigns weights to each input feature to determine how strongly it influences the outcome.

        **Why we use it:**
        - Fast and interpretable, 
        - Easy to explain in healthcare terms
        - Works well for binary classification tasks
        """
    },
    "fr": {
        "title": "Prédicteur de Risque de Diabète",
        "age": "Âge",
        "bmi": "Indice de Masse Corporelle (IMC)",
        "general_health": "État de santé général (1=Excellent, 5=Mauvais)",
        "submit": "Prédire le Risque",
        "result": "Votre risque prédit de diabète est :",
        "highbp": "Hypertension artérielle",
        "highchol": "Cholestérol élevé",
        "physhlth": "Jours de mauvaise santé physique (30 derniers)",
        "smoker": "Fumeur",
        "physactivity": "Activité physique (30 derniers jours)",
        "feature_influence": "📈 Influence des variables",
        "feature_names": {
        "Age": "Âge",
        "BMI": "IMC",
        "GenHlth": "Santé générale",
        "HighBP": "Hypertension",
        "HighChol": "Cholestérol élevé",
        "PhysHlth": "Jours de mauvaise santé physique",
        "Smoker": "Fumeur",
        "PhysActivity": "Activité physique"
    },
        "model_info": "🧪 Ce modèle a été entraîné à partir de données d'enquêtes de santé américaines et a atteint une **précision de 86,13 %** sur l'ensemble de test.",
        "disclaimer": "⚠️ Cet outil ne constitue pas un diagnostic médical. Il est basé sur des données de population et destiné uniquement à des fins éducatives.",
        "logistic_info_title": "📘 Qu'est-ce que la régression logistique ?",
        "logistic_info": """
        La régression logistique est un algorithme d'apprentissage automatique qui permet d'estimer la probabilité qu'une entrée appartienne à une catégorie.

        Ici, elle prédit la probabilité qu'une personne soit atteinte de diabète en fonction de ses données de santé et de mode de vie.

        Contrairement à la régression linéaire, qui donne une valeur continue, la régression logistique donne une probabilité entre 0 et 1.

        Le modèle attribue des poids à chaque variable pour déterminer son impact sur le résultat.

        **Pourquoi l'utiliser ici :**
        - Rapide et interprétable
        - Facile à expliquer en santé publique
        - Idéal pour les classifications binaires
        """
    },
    "zh": {
        "title": "糖尿病风险预测器",
        "age": "年龄",
        "bmi": "身体质量指数（BMI）",
        "general_health": "整体健康状况（1=非常好，5=非常差）",
        "submit": "预测风险",
        "result": "您预测的糖尿病风险是：",
        "highbp": "高血压",
        "highchol": "高胆固醇",
        "physhlth": "身体不适天数（过去30天）",
        "smoker": "吸烟者",
        "physactivity": "身体活动（过去30天）",
        "feature_influence": "📈 特征影响",
        "feature_names": {
        "Age": "年龄",
        "BMI": "身体质量指数",
        "GenHlth": "整体健康状况",
        "HighBP": "高血压",
        "HighChol": "高胆固醇",
        "PhysHlth": "身体不适天数",
        "Smoker": "吸烟者",
        "PhysActivity": "身体活动"
    },
        "model_info": "🧪 此模型基于美国健康调查数据训练，测试准确率为 **86.13%**。",
        "disclaimer": "⚠️ 本工具并非诊断手段，仅供教育参考，基于人口健康统计数据构建。",
        "logistic_info_title": "📘 什么是逻辑回归？",
        "logistic_info": """
        逻辑回归是一种机器学习算法，用于估算某个输入属于某个类别的概率。

        在这里，它用于预测一个人患糖尿病的可能性，依据其健康和生活方式数据。

        与线性回归不同，逻辑回归预测的是一个介于 0 和 1 之间的概率值。

        模型为每个输入特征分配权重，以衡量其对结果的影响。

        **为什么使用逻辑回归：**
        - 快速且易于解释
        - 在医疗场景中便于理解
        - 适合处理二分类问题
        """
    },
    "kr": {
        "title": "당뇨병 위험 예측기",
        "age": "나이",
        "bmi": "체질량지수 (BMI)",
        "general_health": "건강 상태 (1=매우 좋음, 5=매우 나쁨)",
        "submit": "위험 예측하기",
        "result": "예측된 당뇨병 위험도:",
        "highbp": "고혈압",
        "highchol": "고콜레스테롤",
        "physhlth": "최근 30일간의 신체 건강 문제 일수",
        "smoker": "흡연 여부",
        "physactivity": "최근 30일간 신체 활동 여부",
        "feature_influence": "📈 특성 영향력",
        "feature_names": {
        "Age": "나이",
        "BMI": "체질량지수",
        "GenHlth": "전반적인 건강 상태",
        "HighBP": "고혈압",
        "HighChol": "고콜레스테롤",
        "PhysHlth": "최근 30일간 건강 문제 일수",
        "Smoker": "흡연 여부",
        "PhysActivity": "신체 활동"
    },
        "model_info": "🧪 이 모델은 미국 건강 조사 데이터를 기반으로 학습되었으며 테스트 정확도는 **86.13%** 입니다.",
        "disclaimer": "⚠️ 이 도구는 진단 도구가 아닙니다. 이는 인구 데이터를 기반으로 하며 교육용으로만 사용됩니다.",
        "logistic_info_title": "📘 로지스틱 회귀란?",
        "logistic_info": """
        로지스틱 회귀는 입력 값이 특정 범주에 속할 확률을 예측하는 머신러닝 알고리즘입니다.

        이 앱에서는 건강 및 생활습관 데이터를 바탕으로 당뇨병에 걸릴 확률을 예측합니다.

        선형 회귀와 달리, 로지스틱 회귀는 0과 1 사이의 확률 값을 출력합니다.

        모델은 각 입력 변수에 가중치를 부여하여 결과에 대한 영향을 계산합니다.

        **왜 사용하나요?**
        - 빠르고 해석 가능
        - 의료 현장에서 설명하기 쉬움
        - 이진 분류 문제에 적합
        """
    },
}

# select language
lang = st.sidebar.selectbox("Language / Langue / 语言 / 언어", ["en", "fr", "zh", "kr"])
text = translations[lang]

# streamlit app UI
st.title(text["title"])
st.markdown(text["model_info"])
st.warning(text["disclaimer"])

# sliders and select boxes for user inputs
age = st.slider(text["age"], 18, 100, 40)
bmi = st.slider(text["bmi"], 10.0, 50.0, 25.0)
genhlth = st.slider(text["general_health"], 1, 5, 3)
highbp = st.selectbox(text["highbp"], ["No", "Yes"])
highchol = st.selectbox(text["highchol"], ["No", "Yes"])
physhealth = st.slider(text["physhlth"], 0, 30, 5)
smoker = st.selectbox(text["smoker"], ["No", "Yes"])
physact = st.selectbox(text["physactivity"], ["No", "Yes"])

# button to submit inputs and get predictions
if st.button(text["submit"]):
    # preprocess user inputs into a DataFrame
    input_df = pd.DataFrame([[
        age,
        bmi,
        genhlth,
        1 if highbp == "Yes" else 0,
        1 if highchol == "Yes" else 0,
        physhealth,
        1 if smoker == "Yes" else 0,
        1 if physact == "Yes" else 0
    ]], columns=[
        "Age", "BMI", "GenHlth", "HighBP", "HighChol",
        "PhysHlth", "Smoker", "PhysActivity"
    ])

    # run the model prediction
    prediction = model.predict_proba(input_df)[0][1]

    # display result
    st.write(f"{text['result']} **{prediction:.2%}**")

    # display feature influence and model information
    with st.sidebar:
        st.caption("🔍 Model Inputs: Age, BMI, General Health")
        st.caption("📊 Model Type: Logistic Regression")
        st.caption("✅ Accuracy: 86.13% on test set")

    with st.expander(text["feature_influence"]):
        feature_labels = text["feature_names"]
        for f, c in zip(model.feature_names_in_, model.coef_[0]):
            direction = "↑" if c > 0 else "↓"
            label = feature_labels.get(f, f)
            st.write(f"{direction} {label}: {c:.4f}")

    # display short explanation of logistic regression
    with st.expander(text["logistic_info_title"]):
        st.markdown(text["logistic_info"])
