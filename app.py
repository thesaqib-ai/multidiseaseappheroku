import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
heart_model = pickle.load(open('heart_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0
                           )

# diabetes prediction page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure')
    with col1:
        SkinThickness = st.text_input('Skin Thickness')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('Body Mass Index (BMI)')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age')

    diagnosis = ''

    # Convert inputs to numeric values
    try:
        Pregnancies = int(Pregnancies)
        Glucose = float(Glucose)
        BloodPressure = float(BloodPressure)
        SkinThickness = float(SkinThickness)
        Insulin = float(Insulin)
        BMI = float(BMI)
        DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
        Age = int(Age)

        if st.button('Diabetes Test Result'):
            diabetes_diagnosis = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            if diabetes_diagnosis[0] == 1:
                diabetes_diagnosis = 'The Person is Diabetic'
            else:
                diabetes_diagnosis = 'The Person is not Diabetic'
            st.success(diabetes_diagnosis)

    except ValueError:
        st.error("Please enter valid numeric values.")

# heart disease prediction page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('CP')
    with col4:
        trestbps = st.text_input('TrestBPS')
    with col5:
        chol = st.text_input('Chol')
    with col1:
        fbs = st.text_input('FBS')
    with col2:
        restecg = st.text_input('Rest ECG')
    with col3:
        thalach = st.text_input('thalach')
    with col4:
        exang = st.text_input('Exang')
    with col5:
        oldpeak = st.text_input('Oldpeak')
    with col1:
        slope = st.text_input('Slope')
    with col2:
        ca = st.text_input('CA')
    with col3:
        thal = st.text_input('Thal')

    diagnosis = ''

    # Convert inputs to numeric values
    try:
        age = int(age)
        sex = int(sex)
        cp = int(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = int(fbs)
        restecg = int(restecg)
        thalach = float(thalach)
        exang = int(exang)
        oldpeak = float(oldpeak)
        slope = int(slope)
        ca = int(ca)
        thal = int(thal)

        if st.button('Heart Test Result'):
            heart_diagnosis = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            if heart_diagnosis[0] == 1:
                heart_diagnosis = 'The Person has heart disease'
            else:
                heart_diagnosis = 'The Person does not have heart disease'
            st.success(heart_diagnosis)

    except ValueError:
        st.error("Please enter valid numeric values.")

# parkinsons prediction page
if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction using ML')
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        MDVP_Fo_Hz = st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVP_Fhi_Hz = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVP_Flo_Hz = st.text_input('MDVP:Flo(Hz)')
    with col4:
        MDVP_Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    
    with col1:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col2:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col3:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col4:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    
    with col1:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col4:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    diagnosis = ''

    # Convert inputs to numeric values
    try:
        MDVP_Fo_Hz = float(MDVP_Fo_Hz)
        MDVP_Fhi_Hz = float(MDVP_Fhi_Hz)
        MDVP_Flo_Hz = float(MDVP_Flo_Hz)
        MDVP_Jitter_percent = float(MDVP_Jitter_percent)
        MDVP_Jitter_Abs = float(MDVP_Jitter_Abs)
        MDVP_RAP = float(MDVP_RAP)
        MDVP_PPQ = float(MDVP_PPQ)
        Jitter_DDP = float(Jitter_DDP)
        MDVP_Shimmer = float(MDVP_Shimmer)
        MDVP_Shimmer_dB = float(MDVP_Shimmer_dB)
        Shimmer_APQ3 = float(Shimmer_APQ3)
        Shimmer_APQ5 = float(Shimmer_APQ5)
        MDVP_APQ = float(MDVP_APQ)
        Shimmer_DDA = float(Shimmer_DDA)
        NHR = float(NHR)
        HNR = float(HNR)
        RPDE = float(RPDE)
        DFA = float(DFA)
        spread1 = float(spread1)
        spread2 = float(spread2)
        D2 = float(D2)
        PPE = float(PPE)

        if st.button('Parkinsons Test Result'):
            parkinsons_diagnosis = parkinsons_model.predict([[MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
            
            if parkinsons_diagnosis[0] == 1:
                parkinsons_diagnosis = 'The Person has Parkinsons disease'
            else:
                parkinsons_diagnosis = 'The Person does not have Parkinsons disease'
            
            st.success(parkinsons_diagnosis)

    except ValueError:
        st.error("Please enter valid numeric values.")

