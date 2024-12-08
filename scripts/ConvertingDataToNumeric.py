import pandas as pd

def age_group(age):
    if 0 <= age <= 30:
        return 0
    elif 31 <= age <= 40:
        return 1
    elif 41 <= age <= 50:
        return 2
    elif 51 <= age <= 120:
        return 3
    else:
        print(f"Havent found this age {age}")
        return None

def gender_to_numeric(gender):
    if gender == "Non-binary":
        return 0
    elif gender == "Female":
        return 1
    elif gender == "Male":
        return 2
    elif gender == "Prefer not to say":
        return 3
    else:
        print(f"Havent found this gender {gender}")
        return None

def job_role_to_numeric(job_role):
    if job_role == "HR":
        return 0
    elif job_role == "Data Scientist":
        return 1
    elif job_role == "Software Engineer":
        return 2
    elif job_role == "Sales":
        return 3
    elif job_role == "Marketing":
        return 4
    elif job_role == "Designer":
        return 5
    elif job_role == "Project Manager":
        return 6
    else:
        print(f"Havent found this job_role {job_role}")
        return None

def industry_to_numeric(industry):
    if industry == "Healthcare":
        return 0
    elif industry == "IT":
        return 1
    elif industry == "Education":
        return 2
    elif industry == "Finance":
        return 3
    elif industry == "Consulting":
        return 4
    elif industry == "Manufacturing":
        return 5
    elif industry == "Retail":
        return 6
    else:
        print(f"Havent found this industry {industry}")
        return None

def experience_to_numeric(experience):
    if experience <= 5:
        return 0
    elif 6 <= experience <= 10:
        return 1
    elif 11 <= experience <= 20:
        return 2
    elif experience >= 21:
        return 3
    else:
        print(f"Havent found this experience {experience}")
        return None

def work_location_to_numeric(work_location):
    if work_location == "Hybrid":
        return 0
    elif work_location == "Onsite":
        return 1
    elif work_location == "Remote":
        return 2
    else:
        print(f"Havent found this work_location {work_location}")
        return None

def work_hours_to_numeric(work_hours):
    if work_hours <= 20:
        return 0
    elif 21 <= work_hours <= 40:
        return 1
    elif work_hours >= 41:
        return 2
    else:
        print(f"Havent found this work_hours {work_hours}")
        return None

def number_of_meetings_to_numeric(number_of_meetings):
    if number_of_meetings <= 3:
        return 0
    elif 4 <= number_of_meetings <= 6:
        return 1
    elif 7 <= number_of_meetings <= 9:
        return 2
    elif 10 <= number_of_meetings <= 12:
        return 3
    elif number_of_meetings >= 13:
        return 4
    else:
        print(f"Havent found this number_of_meetings {number_of_meetings}")
        return None

def work_life_balance_to_numeric(work_life_balance):
    if work_life_balance == 5:
        return 0
    elif work_life_balance == 4:
        return 1
    elif work_life_balance == 3:
        return 2
    elif work_life_balance == 2:
        return 3
    elif work_life_balance == 1:
        return 4
    else:
        print(f"Havent found this work_life_balance {work_life_balance}")
        return None

def stress_level_to_numeric(stress_level):
    if stress_level == "Medium":
        return 0
    elif stress_level == "High":
        return 1
    elif stress_level == "Low":
        return 2
    else:
        print(f"Havent found this stress_level {stress_level}")
        return None

def access_to_mental_health_resources_to_numeric(access_to_mental_health_resources):
    if access_to_mental_health_resources == "No":
        return 0
    elif access_to_mental_health_resources == "Yes":
        return 1
    else:
        print(f"Havent found this access_to_mental_health_resources {access_to_mental_health_resources}")
        return None

def productivity_change_to_numeric(productivity_change):
    if productivity_change == "Decrease":
        return 0
    elif productivity_change == "Increase":
        return 1
    elif productivity_change == "No Change":
        return 2
    else:
        print(f"Havent found this productivity_change {productivity_change}")
        return None

def social_isolation_to_numeric(social_isolation):
    if social_isolation == 1:
        return 0
    elif social_isolation == 2:
        return 1
    elif social_isolation == 3:
        return 2
    elif social_isolation == 4:
        return 3
    elif social_isolation == 5:
        return 4
    else:
        print(f"Havent found this social_isolation {social_isolation}")
        return None

def satisfaction_with_remote_work_to_numeric(satisfaction_with_remote_work):
    if satisfaction_with_remote_work == "Unsatisfied":
        return 0
    elif satisfaction_with_remote_work == "Satisfied":
        return 1
    elif satisfaction_with_remote_work == "Neutral":
        return 2
    else:
        print(f"Havent found this satisfaction_with_remote_work {satisfaction_with_remote_work}")
        return None

def remote_work_support_to_numeric(remote_work_support):
    if remote_work_support == 1:
        return 0
    elif remote_work_support == 2:
        return 1
    elif remote_work_support == 3:
        return 2
    elif remote_work_support == 5:
        return 3
    elif remote_work_support == 4:
        return 4
    else:
        print(f"Havent found this work_life_balance {remote_work_support}")
        return None

def physical_activity_to_numeric(physical_activity):
    if physical_activity == "Weekly":
        return 0
    elif physical_activity == "None":
        return 1
    elif physical_activity == "Daily":
        return 2
    else:
        print(f"Havent found this physical_activity {physical_activity}")
        return None

def sleep_quality_to_numeric(sleep_quality):
    if sleep_quality == "Good":
        return 0
    elif sleep_quality == "Poor":
        return 1
    elif sleep_quality == "Average":
        return 2
    else:
        print(f"Havent found this sleep_quality {sleep_quality}")
        return None

def mental_health_to_numeric(mental_health):
    if mental_health == "None":
        return "Good"
    elif mental_health == "Anxiety":
        return "Medium"
    elif mental_health == "Burnout":
        return "Bad"
    elif mental_health == "Depression":
        return "Very Bad"
    else:
        print(f"Havent found this mental_health {mental_health}")
        return None

def region_to_numeric(region):
    if region == "Europe":
        return 0
    elif region == "Asia":
        return 1
    elif region == "North America":
        return 2
    elif region == "South America":
        return 3
    elif region == "Oceania":
        return 4
    elif region == "Africa":
        return 5
    else:
        print(f"Havent found this region {region}")
        return None

data = pd.read_csv('Impact_of_Remote_Work_on_Mental_Health.csv')

if 'Employee_ID' in data.columns:
    data = data.drop(columns=['Employee_ID'])

data['Mental_Health_Condition'].fillna('None', inplace=True)
data['Physical_Activity'].fillna('None', inplace=True)

data['Age'] = data['Age'].apply(age_group)
data['Gender'] = data['Gender'].apply(gender_to_numeric)
data['Job_Role'] = data['Job_Role'].apply(job_role_to_numeric)
data['Industry'] = data['Industry'].apply(industry_to_numeric)
data['Years_of_Experience'] = data['Years_of_Experience'].apply(experience_to_numeric)
data['Work_Location'] = data['Work_Location'].apply(work_location_to_numeric)
data['Hours_Worked_Per_Week'] = data['Hours_Worked_Per_Week'].apply(work_hours_to_numeric)
data['Number_of_Virtual_Meetings'] = data['Number_of_Virtual_Meetings'].apply(number_of_meetings_to_numeric)
data['Work_Life_Balance_Rating'] = data['Work_Life_Balance_Rating'].apply(work_life_balance_to_numeric)
data['Stress_Level'] = data['Stress_Level'].apply(stress_level_to_numeric)
data['Access_to_Mental_Health_Resources'] = data['Access_to_Mental_Health_Resources'].apply(access_to_mental_health_resources_to_numeric)
data['Productivity_Change'] = data['Productivity_Change'].apply(productivity_change_to_numeric)
data['Social_Isolation_Rating'] = data['Social_Isolation_Rating'].apply(social_isolation_to_numeric)
data['Satisfaction_with_Remote_Work'] = data['Satisfaction_with_Remote_Work'].apply(satisfaction_with_remote_work_to_numeric)
data['Company_Support_for_Remote_Work'] = data['Company_Support_for_Remote_Work'].apply(remote_work_support_to_numeric)
data['Physical_Activity'] = data['Physical_Activity'].apply(physical_activity_to_numeric)
data['Sleep_Quality'] = data['Sleep_Quality'].apply(sleep_quality_to_numeric)
data['Region'] = data['Region'].apply(region_to_numeric)
data['Mental_Health_Condition'] = data['Mental_Health_Condition'].apply(mental_health_to_numeric)

output_path = 'Impact_of_Remote_Work_on_Mental_Health_output.csv'
data.to_csv(output_path, index=False)
