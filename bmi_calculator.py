import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 16:
        return "Severe Thinness"
    elif bmi < 17:
        return "Moderate Thinness"
    elif bmi < 18.5:
        return "Mild Thinness"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obese Class 1"
    elif bmi < 40:
        return "Obese Class 2"
    else:
        return "Obese Class 3"

def convert_height_to_meters(feet, inches):
    total_inches = (feet * 12) + inches
    height_in_meters = total_inches * 0.0254
    return height_in_meters

def main():
    st.title("BMI Calculator 📊")
    
    if st.button("Limitations of BMI calculator ❗"):
        st.write("📌 It does not take into account muscle mass or body composition ❗")
        st.write("📌 It may not be accurate for people who are very muscular or very short ❗")
        st.write("📌 It may not be suitable for people from different ethnic backgrounds ❗")
        st.write("📥 Enter your weight and height to calculate your BMI.")
    st.write("Enter your weight and height to calculate your BMI.")

    col1, col2, col3 = st.columns(3)
    weight = col1.number_input("Weight (in kg)", min_value=0.0, step=0.1)
    feet = col2.number_input("Height (in feet)", min_value=0, step=1)
    inches = col3.number_input("Inches", min_value=0, max_value=11, step=1)

    if st.button("Calculate BMI"):
        height_in_meters = convert_height_to_meters(feet, inches)
        bmi = calculate_bmi(weight, height_in_meters)
        category = get_bmi_category(bmi)
        st.write(f"Your BMI is: {bmi:.2f}")
        st.write(f"Your BMI category is: {category}")

        if category == "Severe Thinness":
            st.write("You are severely underweight. Please consult a doctor or a registered dietitian to develop a weight gain plan.")
        elif category == "Moderate Thinness":
            st.write("You are moderately underweight. You may want to consider increasing your calorie intake to achieve a healthy weight.")
        elif category == "Mild Thinness":
            st.write("You are mildly underweight. You may want to consider increasing your calorie intake to achieve a healthy weight.")
        elif category == "Normal":
            st.write("You are at a healthy weight. Keep up the good work!")
        elif category == "Overweight":
            st.write("You are overweight. You may want to consider reducing your calorie intake and increasing your physical activity to achieve a healthy weight.")
        elif category == "Obese Class 1":
            st.write("You are obese class 1. You may want to consider reducing your calorie intake and increasing your physical activity to achieve a healthy weight. Please consult a doctor or a registered dietitian for personalized advice.")
        elif category == "Obese Class 2":
            st.write("You are obese class 2. You may want to consider reducing your calorie intake and increasing your physical activity to achieve a healthy weight. Please consult a doctor or a registered dietitian for personalized advice.")
        elif category == "Obese Class 3":
            st.write("You are obese class 3. Please consult a doctor or a registered dietitian to develop a weight loss plan.")

if __name__ == "__main__":
    main()


