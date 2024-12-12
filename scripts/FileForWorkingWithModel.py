import joblib
import numpy as np
import pandas as pd

# Load the trained model
model_path = 'mental_health_predictor_model.pkl'
model = joblib.load(model_path)

# Define the fields and their input prompts
fields = [
    ("Age (0: 0-30, 1: 31-40, 2: 41-50, 3: 51+)", int),
    ("Gender (0: Non-binary, 1: Female, 2: Male, 3: Prefer not to say)", int),
    ("Job Role (0: HR, 1: Data Scientist, 2: Software Engineer, 3: Sales, 4: Marketing, 5: Designer, 6: Project Manager)", int),
    ("Industry (0: Healthcare, 1: IT, 2: Education, 3: Finance, 4: Consulting, 5: Manufacturing, 6: Retail)", int),
    ("Years of Experience (0: <=5, 1: 6-10, 2: 11-20, 3: 21+)", int),
    ("Work Location (0: Hybrid, 1: Onsite, 2: Remote)", int),
    ("Hours Worked Per Week (0: <=20, 1: 21-40, 2: >=41)", int),
    ("Number of Virtual Meetings (0: <=3, 1: 4-6, 2: 7-9, 3: 10-12, 4: >=13)", int),
    ("Work Life Balance Rating (0: Excellent, 1: Good, 2: Fair, 3: Poor, 4: Very Poor)", int),
    ("Stress Level (0: Medium, 1: High, 2: Low)", int),
    ("Access to Mental Health Resources (0: No, 1: Yes)", int),
    ("Productivity Change (0: Decrease, 1: Increase, 2: No Change)", int),
    ("Social Isolation Rating (0: None, 1: Minimal, 2: Moderate, 3: High, 4: Very High)", int),
    ("Satisfaction with Remote Work (0: Unsatisfied, 1: Satisfied, 2: Neutral)", int),
    ("Company Support for Remote Work (0: Minimal, 1: Moderate, 2: Good, 3: Excellent, 4: Exceptional)", int),
    ("Physical Activity (0: Weekly, 1: None, 2: Daily)", int),
    ("Sleep Quality (0: Good, 1: Poor, 2: Average)", int),
    ("Region (0: Europe, 1: Asia, 2: North America, 3: South America, 4: Oceania, 5: Africa)", int)
]

# Feature names as per the model
feature_names = [
    "Age", "Gender", "Job_Role", "Industry", "Years_of_Experience", "Work_Location",
    "Hours_Worked_Per_Week", "Number_of_Virtual_Meetings", "Work_Life_Balance_Rating",
    "Stress_Level", "Access_to_Mental_Health_Resources", "Productivity_Change",
    "Social_Isolation_Rating", "Satisfaction_with_Remote_Work",
    "Company_Support_for_Remote_Work", "Physical_Activity", "Sleep_Quality", "Region"
]

# Collect input from the user
user_input = []
for field, field_type in fields:
    while True:
        try:
            value = field_type(input(f"Enter {field}: "))
            user_input.append(value)
            break
        except ValueError:
            print("Invalid input. Please try again.")

# Convert user input into a DataFrame with feature names
input_df = pd.DataFrame([user_input], columns=feature_names)

# Make a prediction
predicted_condition = model.predict(input_df)[0]

# Analyze feature importances
feature_importances = model.feature_importances_
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Provide personalized suggestions
print(f"\nPredicted Mental Health Condition: {predicted_condition}")
print("\nSuggestions to Improve Mental Health:")

if predicted_condition in ['Bad', 'Very Bad']:
    # Provide specific recommendations for critical conditions
    top_features = importance_df.head(5)['Feature'].values
    for feature in top_features:
        if feature == 'Work_Life_Balance_Rating':
            print("- Consider improving your work-life balance by setting boundaries and prioritizing rest.")
        elif feature == 'Stress_Level':
            print("- Engage in stress-reducing activities like meditation, exercise, or counseling.")
        elif feature == 'Access_to_Mental_Health_Resources':
            print("- Ensure access to mental health resources. Speak to your employer or seek local resources.")
        elif feature == 'Physical_Activity':
            print("- Incorporate regular physical activity into your routine to improve overall well-being.")
        elif feature == 'Sleep_Quality':
            print("- Focus on improving sleep quality by maintaining a consistent sleep schedule.")
else:
    print("- Your mental health condition seems stable. Continue maintaining healthy habits!")

# Show the top contributing features
print("\nTop Features Influencing Prediction:")
print(importance_df.head())
