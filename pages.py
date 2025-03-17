import streamlit as st
from utils.markdown import centered_title, centered_subheader
from config import *
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import plotly.express as px

def show_info_of_a_column(df):
	tmp = df.isnull().sum().to_frame().T
	list_nunique = []
	list_dtypes = []
	list_null_values = [0, 2799, 0, 0, 0, 0, 2809, 0, 0, 0, 0, 0, 0, 857, 0]
	# list_null_values = list(np.sum(df == "?"))

	for col in df.columns:
		list_dtypes.append(df[col].dtype)
		list_nunique.append(df[col].nunique())
		# list_null_values.append(df.isnull().sum()[col])
	tmp_df = pd.DataFrame({"Null values": list_null_values, "Data Type": list_dtypes, "unique values": list_nunique}, index=df.columns)
	return tmp_df

def plot_numerical_distributions(df, column_name):
	if column_name not in df.columns:
		st.error(f"Column '{column_name}' is not found in DataFrame!")
		return
	

	fig = px.histogram(df[column_name], x=column_name, nbins=20, title=f"Distribution of {column_name}", 
                           marginal="box", color_discrete_sequence=["royalblue"])
	st.plotly_chart(fig)
		
def plot_categorical_distribution(df, column_name):
    if column_name not in df.columns:
        st.error(f"Column '{column_name}' is not found in  DataFrame!")
        return
    
    count_df = df[column_name].value_counts().reset_index()
    count_df.columns = [column_name, "count"] 
    
    fig = px.bar(
        count_df,
        x="count",
        y=column_name,
        orientation="h",
        text="count",
        title=f"Distribution of {column_name}",
        labels={column_name: "Category", "count": "Frequency"},
        color=column_name,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    fig.update_traces(textposition="outside") 
    st.plotly_chart(fig)
	
def plot_scatter_plot(df, x_column_name, y_column_name):
	fig = px.scatter(df, x=x_column_name, y=y_column_name, title=f'Scatter Plot of {x_column_name} vs {y_column_name}',
                         labels={x_column_name: x_column_name, y_column_name: y_column_name})
	st.plotly_chart(fig)
	
def plot_categorical_heatmap(df, col_x, col_y):
    # Tạo bảng đếm số lần xuất hiện của từng cặp giá trị
    contingency_table = df.groupby([col_x, col_y]).size().reset_index(name="count")

    # Vẽ heatmap bằng Plotly
    fig = px.density_heatmap(
        contingency_table, x=col_x, y=col_y, z="count",
        color_continuous_scale="Blues",
        title=f"Heatmap: {col_x} vs {col_y}"
    )

    st.plotly_chart(fig)
	
def visualize_page():
	centered_title("Adult Dataset Visualization")
	train_df = pd.read_csv("./data/adult/adult.csv", header=None, names=DATAFRAME_COLUMNS)
	print((train_df == '?').sum())
	num_rows = st.slider(label="Number of rows",
					  	 min_value=1,
						 max_value=len(train_df))
	st.write(train_df.head(num_rows))
	col1v1, col2v1 = st.columns(2)
	with col1v1:
		centered_subheader("Describe")
		is_include_all = st.checkbox("Including categorical columns")
		st.table(train_df.describe(include=('all' if is_include_all == True else None)).T)
		
	with col2v1:
		centered_subheader("Information of each column")
		st.table(show_info_of_a_column(train_df))
		
	col1v2, col2v2 = st.columns(2)
	with col1v2:
		centered_subheader("Numerical Distribution")
		numerical_column_name = st.selectbox(label="Column Name", 
							 		options=NUMERICAL_COLUMNS)
		plot_numerical_distributions(train_df, numerical_column_name)
		
		centered_subheader("Scatter Plot")
		x_column_name = st.selectbox("Select X", NUMERICAL_COLUMNS)
		y_column_name = st.selectbox("Select Y", NUMERICAL_COLUMNS)
		plot_scatter_plot(train_df, x_column_name, y_column_name)
	with col2v2:
		centered_subheader("Categorical Variable Distribution")
		categorical_column_name = st.selectbox(label="Column Name", 
							 		options=CATEGORICAL_COLUMNS)
		plot_categorical_distribution(train_df, categorical_column_name)

		centered_subheader("Categorical Heat Map")
		col_x = st.selectbox("Select X", CATEGORICAL_COLUMNS, key="select_x")
		if col_x:
			col_y = st.selectbox("Select Y", [col for col in CATEGORICAL_COLUMNS if col != col_x], key="select_y")
			if col_y:
				plot_categorical_heatmap(train_df, col_x, col_y)
		
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

	if st.button("Classify"):
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

	if st.button("Predict"):
		# predict_hours_per_week(*input_args)
		...

def set_layout():
	st.set_page_config(layout="wide")
	st.image(LOGO_IMG_PATH, width=200)
	st.sidebar.title("UI Demo - DSR301m")
	menu = ["Problem 1", "Problem 2", "Problem 3", "Visualization",]
	choice = st.sidebar.selectbox("Select Page", menu)
	
	if choice == "Problem 1":
		problem1_page()
	elif choice == "Problem 2":
		problem2_page()
	elif choice == "Problem 3":
		problem3_page()
	elif choice == "Visualization":
		visualize_page()

