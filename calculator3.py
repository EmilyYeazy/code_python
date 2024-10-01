#Making a Basic Calculator on Streamlit
#Add, subtract, multiply divide

#External Imports
import streamlit as st

#Streamlit Calculator App
st.title("Basic Calculator")
st.write("Welcome to our app, please input two numeric values.")

num1 = st.number_input(
    label="Enter num1 here.",
    key="num1_input"
)

num2 = st.number_input(
    label="Enter num2 here.",
    key="num2_input"
)

operators = []
if num2 == 0 or num2 == -0.0:
    operators = ['add','subtract','multiply']
else:
    operators = ['add','subtract','multiply','divide']

operator_choice = st.selectbox(
    label="Choose an operation.",
    options=operators,
    key="operator_choice"
)

calculate_button = st.button(
    label="Calculate",
    key="calculate_button"
)

result = 0
if calculate_button:
    #when the button is clicked
    if operator_choice == "add":
        result = num1 + num2
    elif operator_choice == "subtract":
        result = num1 - num2
    elif operator_choice == "multiply":
        result = num1 * num2
    elif operator_choice == "divide":
        result = num1 / num2
    
    operator_dict = {
        'add':'+',
        'subtract':'-',
        'multiply':'*',
        'divide':'/'
    }
    st.write(f"{num1} {operator_dict[operator_choice]} {num2} = {result}")