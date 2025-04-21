from flask import Flask, render_template, request, session, redirect, url_for
import pickle
import numpy as np

app = Flask(__name__)

scaler = pickle.load(open("Models/scaler2.pkl", "rb"))
model = pickle.load(open("Models/model2.pkl", "rb"))

# class_names = ['Lawyer', 'Doctor', 'Government Officer', 'Artist', 'Unknown',
#                'Software Engineer', 'Teacher', 'Business Owner', 'Scientist',
#                'Banker', 'Writer', 'Accountant', 'Designer',
#                'Construction Engineer', 'Game Developer', 'Stock Investor',
#                'Real Estate Developer']


# def Recommendations(gender, part_time_job, absence_days, extracurricular_activities, weekly_self_study_hours, math_score, history_score, physics_score,
#                     chemistry_score, biology_score, english_score, geography_score, total_score, average_score):

#     # encoding categorical variables
#     gender_encoded = 1 if gender.lower() == 'female' else 0
#     part_time_job_encoded = 1 if part_time_job else 0
#     extracurricular_activities_encoded = 1 if extracurricular_activities else 0

#     # create feature array
#     feature_array = np.array([[gender_encoded, part_time_job_encoded, absence_days, extracurricular_activities_encoded,
#                           weekly_self_study_hours, math_score, history_score, physics_score,
#                           chemistry_score, biology_score, english_score, geography_score,
#                           total_score, average_score]])

#     # scale features
#     scaled_features = scaler.transform(feature_array)

#     # Predict using the model
#     probabilities = model.predict_proba(scaled_features)

#     #get top five predicted classes along with their probabilities
#     top_classes_idx = np.argsort(-probabilities[0])[:5]

#     top_classes_name_probs = [(class_names[idx], probabilities[0][idx]) for idx in top_classes_idx]

#     return top_classes_name_probs

class_names = [
    'commerce', 'arts', 'law', 'business', 'architecture', 
    'engineering', 'medicine', 'science']


def Recommendations(Drawing, Dancing, Singing, Sports, VideoGame, Acting, Travelling, Gardening, Animals, 
                    Photography, Teaching, Exercise, Coding, ElectricityComponents, MechanicParts, 
                    ComputerParts, Researching, Architecture, HistoricCollection, Botany, Zoology, Physics, Accounting, 
                    Economics, Sociology, Geography, Psycology, History, Science, BussinessEducation, Chemistry, Mathematics, 
                    Biology, Makeup, Designing, ContentWriting, Crafting, Literature, Reading, Cartooning, Debating, Asrtology, 
                    Hindi, French, English, Urdu, OtherLanguage, SolvingPuzzles, Gymnastics, Yoga, Engeeniering, Doctor, 
                    Pharmisist, Cycling, Knitting, Director, Journalism, Bussiness, ListeningMusic):

    # Create feature array
    feature_array = np.array([[Drawing, Dancing, Singing, Sports, VideoGame, Acting, Travelling, Gardening, Animals, 
                               Photography, Teaching, Exercise, Coding, ElectricityComponents, MechanicParts, 
                               ComputerParts, Researching, Architecture, HistoricCollection, Botany, Zoology, 
                               Physics, Accounting, Economics, Sociology, Geography, Psycology, History, Science, 
                               BussinessEducation, Chemistry, Mathematics, Biology, Makeup, Designing, ContentWriting, 
                               Crafting, Literature, Reading, Cartooning, Debating, Asrtology, Hindi, French, English, 
                               Urdu, OtherLanguage, SolvingPuzzles, Gymnastics, Yoga, Engeeniering, Doctor, Pharmisist, 
                               Cycling, Knitting, Director, Journalism, Bussiness, ListeningMusic]])

    # Scale features
    scaled_features = scaler.transform(feature_array)

    # Predict using the model
    probabilities = model.predict_proba(scaled_features)

    # Get top five predicted classes along with their probabilities 
    top_classes_idx = np.argsort(-probabilities[0])[:5]   

    top_classes_name_probs = [(class_names[idx], probabilities[0][idx]) for idx in top_classes_idx]

    return top_classes_name_probs



@app.route("/")
def home():
    session.clear()
    return render_template('h1.html')

app.secret_key = 'Zeal1234'

@app.route("/recommend")
def recommend():
    # return render_template('recommend.html')
    # return render_template('group1.html')
   
    return render_template('g11.html')


@app.route('/group1', methods=['GET', 'POST'])
def group1():
    if request.method == 'POST':
        # print(request.form)
        # print(session)
        for field in ['Drawing', 'Dancing', 'Singing', 'Acting', 'Makeup', 'Designing', 'ContentWriting', 'Crafting', 
                      'Literature', 'Reading', 'Cartooning', 'Debating', 'Asrtology', 'Director', 'Journalism']:
            session[field] = int(request.form.get(field.lower(), 0))
        print(session)
        return redirect(url_for('group2'))
    return render_template('g11.html')



@app.route('/group2', methods=['GET', 'POST'])
def group2():
    if request.method == 'POST':
        for field in ['Teaching', 'Researching', 'HistoricCollection', 'Physics', 'Chemistry', 'Biology', 'Mathematics', 
                      'Geography', 'History', 'Sociology', 'Psycology', 'Accounting', 'Economics', 'Science', 'BussinessEducation', 
                      'English', 'Hindi', 'French', 'Urdu', 'Architecture', 'Botany', 'Zoology', 'OtherLanguage']:
            session[field] = int(request.form.get(field, 0))
        return redirect(url_for('group3'))
    return render_template('group2.html')



@app.route('/group3', methods=['GET', 'POST'])
def group3():
    if request.method == 'POST':
        for field in ['Coding', 'ElectricityComponents', 'MechanicParts', 'ComputerParts', 'Engeeniering', 'Doctor', 'Pharmisist', 'Bussiness']:
            session[field] = int(request.form.get(field, 0))
        return redirect(url_for('group4'))
    return render_template('group3.html')



@app.route('/group4', methods=['GET', 'POST'])
def group4():
    if request.method == 'POST':
        for field in ['Sports', 'VideoGame', 'Travelling', 'Gardening', 'Animals', 'Photography', 'Exercise', 'SolvingPuzzles', 
                      'Gymnastics', 'Yoga', 'Cycling', 'Knitting', 'ListeningMusic']:
            session[field] = int(request.form.get(field, 0))
        
        # Call Recommendations with all session data
        final_recommendations = Recommendations(**{key: session.get(key, 0) for key in session})

        return render_template('results.html', recommendations=final_recommendations)

    return render_template('group4.html')


# @app.route("results.html")
# def results():
#     return render_template("results.html")


# @app.route("/pred", methods=['POST', 'GET'])
# def pred():
#     if request.method == 'POST':
#         gender = request.form['gender']
#         part_time_job = request.form['part_time_job'] == 'true'
#         absence_days = int(request.form['absence_days'])
#         extracurricular_activities = request.form['extracurricular_activities'] == 'true'
#         weekly_self_study_hours = int(request.form['weekly_self_study_hours'])
#         math_score = int(request.form['math_score'])
#         history_score = int(request.form['history_score'])
#         physics_score = int(request.form['physics_score'])
#         chemistry_score = int(request.form['chemistry_score'])
#         biology_score = int(request.form['biology_score'])
#         english_score = int(request.form['english_score'])
#         geography_score = int(request.form['geography_score'])
#         total_score = float(request.form['total_score'])
#         average_score = float(request.form['average_score'])

#         recommendations = Recommendations(gender, part_time_job, absence_days, extracurricular_activities,
#                                           weekly_self_study_hours, math_score, history_score, physics_score,
#                                           chemistry_score, biology_score, english_score, geography_score,
#                                           total_score, average_score)

#         return render_template('results.html', recommendations=recommendations)
#     return render_template('home.html')


# @app.route("/pred", methods=['POST', 'GET'])
# def pred():
#     if request.method == 'POST':
#         # List of all your features (should match exactly with your model)
#         feature_names = [
#             'Drawing', 'Dancing', 'Singing', 'Sports', 'VideoGame', 'Acting', 'Travelling',
#             'Gardening', 'Animals', 'Photography', 'Teaching', 'Exercise', 'Coding', 'ElectricityComponents',
#             'MechanicParts', 'ComputerParts', 'Researching', 'Architecture', 'HistoricCollection', 'Botany',
#             'Zoology', 'Physics', 'Accounting', 'Economics', 'Sociology', 'Geography', 'Psycology', 'History',
#             'Science', 'BussinessEducation', 'Chemistry', 'Mathematics', 'Biology', 'Makeup', 'Designing',
#             'ContentWriting', 'Crafting', 'Literature', 'Reading', 'Cartooning', 'Debating', 'Astrology',
#             'Hindi', 'French', 'English', 'Urdu', 'OtherLanguage', 'SolvingPuzzles', 'Gymnastics', 'Yoga',
#             'Engeeniering', 'Doctor', 'Pharmisist', 'Cycling', 'Knitting', 'Director', 'Journalism',
#             'Bussiness', 'ListeningMusic'
#         ]

#         # Collect feature values from the form
#         feature_data = {}
#         for feature in feature_names:
#             # Get the value from the form and convert it to int (assuming form sends '0' or '1')
#             feature_data[feature] = int(request.form.get(feature, 0))  # default to 0 if not found

#         # Add a dummy Courses field with 0, for later storage (optional)
#         # feature_data['Courses'] = 0

#         print(feature_data)
#         # Get recommendations
#         recommendations = Recommendations(**feature_data)

#         # Add the top predicted course
#         top_course = recommendations[0][0]
#         feature_data['Courses'] = top_course

        # Optional: Save to CSV
        # csv_path = 'predicted_courses_dataset.csv'
        # try:
        #     existing_df = pd.read_csv(csv_path)
        #     updated_df = pd.concat([existing_df, pd.DataFrame([feature_data])], ignore_index=True)
        # except FileNotFoundError:
        #     updated_df = pd.DataFrame([feature_data])

        # updated_df.to_csv(csv_path, index=False)

    #     return render_template('results.html', recommendations=recommendations)

    # return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)
