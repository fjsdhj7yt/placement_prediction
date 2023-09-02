import streamlit as st
import pickle


st.title('Placement Prediction Application')

# Load the trained model
pickle_in = open("models/model2.pkl", "rb")
classifier = pickle.load(pickle_in)

def placement_prediction(Internships, CGPA, Hostel, HistoryofBacklogs, Female, Male, Civil, ComputerScience, Electrical, ElectronicsAndCommunication, InformationTechnology, Mechanical):
    prediction = classifier.predict([[Internships, CGPA, Hostel, HistoryofBacklogs, Female, Male, Civil, ComputerScience, Electrical, ElectronicsAndCommunication, InformationTechnology, Mechanical]])
    return prediction[0]

def main():


    st.title('Placement Prediction')
    CGPA = st.slider(
        "Enter Your CGPA",
        min_value=0.0,
        max_value=10.0,
        value=0.0,
        step=0.1,
        format="%.1f",
    )

    Internships = st.number_input("Enter the Number of Internships", min_value=0, max_value=10, value=0)
    hostel_mapping = {"Yes": 1, "No": 0}
    Hostel = st.radio("Do you stay in the hostel?", list(hostel_mapping.keys()))
    HistoryofBacklogs = st.number_input("Number of Backlogs", min_value=0)
    stream_options = ["Civil", "Computer Science", "Electrical", "Electronics and Communication",
                      "Information Technology", "Mechanical"]
    Stream = st.selectbox("Select your stream", stream_options)

    stream_mapping = {stream: 1 if stream == Stream else 0 for stream in stream_options}

    gender_options = ["Male", "Female"]
    Gender = st.selectbox("Select your gender", gender_options)
    gender_mapping = {"Male": 1, "Female": 0}
    gender_mapping[Gender] = 1
    result = ''
    Civil = stream_mapping.get("Civil", 0)
    ComputerScience = stream_mapping.get("Computer Science", 0)
    Electrical = stream_mapping.get("Electrical", 0)
    ElectronicsAndCommunication = stream_mapping.get("Electronics and Communication", 0)
    InformationTechnology = stream_mapping.get("Information Technology", 0)
    Mechanical = stream_mapping.get("Mechanical", 0)

    if st.button("Predict Placement"):
        Female_encoded = 1 if Gender == "Female" else 0
        Male_encoded = 1 if Gender == "Male" else 0
        Hostel_encoded = hostel_mapping[Hostel]
        result = placement_prediction(
            Internships, CGPA, Hostel_encoded, HistoryofBacklogs, Female_encoded, Male_encoded,
            Civil, ComputerScience, Electrical, ElectronicsAndCommunication,
            InformationTechnology, Mechanical
        )
        if result==1:
            st.write('Congrats You will get Placed!!! 😃')
        else:
            st.write('sorry You cant get placed 😞')
if __name__ == '__main__':
    main()
