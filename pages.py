import streamlit as st
from utils.markdown import centered_title, centered_subheader
from config import *

def problem1_page():
	"""
		Input: age, workclass, education, education-num, 
			marital-status, occupation, relationship, 
			race, sex, capital-gain, capital-loss, hours-per-week, native-country
		Output: income (> 50K, <= 50k)
	"""
	centered_title("Classification Income")
	centered_subheader("Personal Information")
	col1, col2 = st.columns(2)
	with col1:
		
		age = st.number_input(label="Enter your age: ",
							  min_value=0,
							  max_value=100)
		sex = st.radio(label="Enter your sex: ",
				 	   options=SEX_LIST)
		workclass = st.selectbox(label="Enter your workclass: ",
						   		 options= WORKCLASS_LIST)
		
		education = st.selectbox(label="Enter your education: ",
						   		 options=EDUCATION_LIST)
		
		education_num = st.slider(label="Education number: ", 
								  min_value=0, 
								  max_value=100)
		marital_status = st.selectbox(label="Marital status: ",
									  options=MARITAL_STATUS_LIST)

	with col2:
		
		
		occupation = st.selectbox(label="Occupation: ",
								  options=OCCUPATION_LIST)
		
		relationship = st.selectbox(label="Relationship: ",
							  		options=RELATIONSHIP_LIST)
		
		race = st.selectbox(label="Race", 
					  		options=RACE_LIST)
		
		capital_gain = st.number_input(label="Capital gain", 
						   		 		min_value=0)
		
		capital_loss = st.number_input(label="Capital loss", 
						   		 min_value=0)
		
		hours_per_week = st.slider(label="Hours per week: ",
								   min_value=0, 
								   max_value=168)
		
		native_country = st.selectbox(label="Native Country: ",
									  options=NATIVE_COUNTRY_LIST)
		
		input_args = (age, sex, workclass, education, education_num, marital_status, occupation, relationship, \
						race, sex, capital_gain, capital_loss, hours_per_week, native_country)

	if st.button("Classifiter"):
		# classification_income(*input_args)
		...

def problem2_page():
	"""
		Input : age, workclass, education, education-num, occupation, relationship, race, sex, capital-gain, capital-loss, hours-per-week, native-country 
		Output : marital-status
	"""
	centered_title("Classification Marital Status")
	centered_subheader("Personal Information")
	col1, col2 = st.columns(2)
	with col1:
		
		age = st.number_input(label="Enter your age: ",
							  min_value=0,
							  max_value=100)
		sex = st.radio(label="Enter your sex: ",
				 	   options=SEX_LIST)
		workclass = st.selectbox(label="Enter your workclass: ",
						   		 options= WORKCLASS_LIST)
		
		education = st.selectbox(label="Enter your education: ",
						   		 options=EDUCATION_LIST)
		
		education_num = st.slider(label="Education number: ", 
								  min_value=0, 
								  max_value=100)
		hours_per_week = st.slider(label="Hours per week: ",
								   min_value=0, 
								   max_value=168)
		
	with col2:
		
		
		occupation = st.selectbox(label="Occupation: ",
								  options=OCCUPATION_LIST)
		
		relationship = st.selectbox(label="Relationship: ",
							  		options=RELATIONSHIP_LIST)
		
		race = st.selectbox(label="Race", 
					  		options=RACE_LIST)
		
		capital_gain = st.number_input(label="Capital gain", 
						   		 		min_value=0)
		
		capital_loss = st.number_input(label="Capital loss", 
						   		 min_value=0)
		
		native_country = st.selectbox(label="Native Country: ",
									  options=NATIVE_COUNTRY_LIST)
		
		input_args = (age, sex, workclass, education, education_num, occupation, relationship, \
						race, sex, capital_gain, capital_loss, hours_per_week, native_country)

	if st.button("Classifiter"):
		# classification_marital_status(*input_args)
		...

def problem3_page():
	"""
		Input: age, education, education_num, occupation
		Output: hours-per-week
	"""
	centered_title("Predict Hours Per Week")
	centered_subheader("Personal Information")
	col1, col2 = st.columns(2)
	with col1:
		age = st.number_input(label="Enter your age: ",
							  min_value=0,
							  max_value=100)
		
		education = st.selectbox(label="Enter your education: ",
						   		 options=EDUCATION_LIST)
		
		education_num = st.slider(label="Education number: ", 
								  min_value=0, 
								  max_value=100)

	with col2:
		
		
		occupation = st.selectbox(label="Occupation: ",
								  options=OCCUPATION_LIST)
		
		
	input_args = (age, education, education_num, occupation)

	if st.button("Classifiter"):
		# predict_hours_per_week(*input_args)
		...

def set_layout():
	st.set_page_config(layout="wide")
	st.image(LOGO_IMG_PATH, width=200)
	st.sidebar.title("Options")
	menu = ["Problem 1", "Problem 2", "Problem 3"]
	choice = st.sidebar.selectbox("Select Page", menu)
	
	if choice == "Problem 1":
		problem1_page()
	elif choice == "Problem 2":
		problem2_page()
	else:
		problem3_page()
