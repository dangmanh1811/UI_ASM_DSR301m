EDUCATION_LIST = ["Bachelors", "Some-college", "11th", "HS-grad"]
WORKCLASS_LIST = ["Private", "Self-emp-not-inc", "Self-emp-inc", \
					   "Federal-gov", "Local-gov", "State-gov", "Without-pay", "Never-worked"]
SEX_LIST = ["Female", "Male"]
MARITAL_STATUS_LIST = ["Divorced", "Never-married", "Separated"]
OCCUPATION_LIST = ["Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial", "Prof-speciality", \
				   "Handlers-cleaners", "Machine-op-inspct", "Adm-clerial", "Farming-fishing", "Transport-moving", \
				   "Priv-house-serv", "Protective-serv", "Armed-Forces"]
RELATIONSHIP_LIST = ["Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmaried"]
RACE_LIST = ["White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Black", "Other"]
NATIVE_COUNTRY_LIST = ["United-States", "Cambodia", "England", "Puerto-Rico", "Canada", "Germany", "Outlying-US", \
					   "India", "Japan", "Greece", "South", "China", "Cuba", "Iran", "Honduras", "Philippines", \
					   "Italy","Poland", "Jamaica", "Vietnam", "Mexico", "Portugal", "Ireland", "France", \
					   "Dominican-Republic", "Laos", "Ecuador", "Taiwan", "Haiti", "Columbia", "Hungary", "Guatemala",\
					    "Nicaragua", "Scotland", "Thailand", "Yugoslavia", "El-Salvador", "Trinadad&Tobago", "Peru", \
						"Hong", "Holand-Netherlands"]

DATAFRAME_COLUMNS = ["age", "workclass", "fnlwgt", "education", "educational-num", "marital-status", "occupation", "relationship", "race", \
					 "gender", "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"]


NUMERICAL_COLUMNS = ['age', 'fnlwgt', 'educational-num', 'capital-gain', 'capital-loss', 'hours-per-week']
CATEGORICAL_COLUMNS = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', \
				   							 'gender', 'native-country']
# Setting layout
LOGO_IMG_PATH = "./source/logoFptEdu.png"
BACKGROUND_IMG_PATH = ...