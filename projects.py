import streamlit as st
from PIL import Image

def show_projects():
    # --- PROJECT PAGE HEADER WITH CONSISTENT ALIGNMENT ---
    left_spacer, content_col, right_spacer = st.columns([1, 3, 1])
    with content_col:
        st.title("Personal Projects")
        st.write("---")
        st.markdown("<br>", unsafe_allow_html=True)

    # --- PROJECT DATA ---
    projects = [
        {
            "title": "Mutual Learning Algorithm for News Classification",
            "image": "images/Mutual.png",
            "description": "Developed a mutual learning framework integrating Multinomial Naïve Bayes, SVM, and MLP Neural Networks, achieving 98% accuracy. The model employs a student-teacher approach to improve classification accuracy by 3.21%, enabling efficient model training in resource-constrained environments.",
            "outcome": [
                "Improved model classification accuracy by 3.21% using mutual learning.",
                "Reduced training time and computational costs for scalability.",
                "Achieved 98% accuracy for real-time news classification applications."
            ],
            "technologies": [
                "<span style='color:#FF6347; font-weight:bold;'>Machine Learning:</span> Naïve Bayes, SVM, MLP Neural Networks",
                "<span style='color:#FF6347; font-weight:bold;'>NLP:</span> Tokenization, Lemmatization, Stop-word Removal",
                "<span style='color:#FF6347; font-weight:bold;'>Optimization:</span> Knowledge Distillation, Mutual Learning",
                "<span style='color:#FF6347; font-weight:bold;'>Libraries:</span> Scikit-learn, NLTK, Pandas, NumPy"
            ],
            "github": "https://github.com/jp1779/Capstone_Project",
            "report": "https://drive.google.com/file/d/1owcMzd3VMgxlZp8xTyLK9ZNRtAJaeg0-/view?usp=drive_link"
        },
        {
            "title": "AI-Driven Diabetes Prediction Pipeline",
            "image": "images/Diabetes.jpeg",
            "description": "Built an ML pipeline to predict diabetes risk with Random Forest, SVM, Decision Tree, and Deep Learning models, achieving 97% recall and 95% ROC AUC. Used SMOTE and GridSearchCV to improve generalization and hyperparameter tuning.",
            "outcome": [
                "Achieved 97% recall and 95% ROC AUC, outperforming traditional diagnostic models.",
                "Handled class imbalance, reducing false negatives.",
                "Optimized deep learning models, improving prediction performance by 15%."
            ],
            "technologies": [
                "<span style='color:#FF6347; font-weight:bold;'>ML Models:</span> Random Forest, SVM, Decision Tree, MLP",
                "<span style='color:#FF6347; font-weight:bold;'>Data Preprocessing:</span> SMOTE, One-Hot Encoding",
                "<span style='color:#FF6347; font-weight:bold;'>Feature Engineering:</span> Log Transformations, Batch Normalization",
                "<span style='color:#FF6347; font-weight:bold;'>Libraries:</span> Scikit-learn, TensorFlow, Pandas, Matplotlib"
            ],
            "github": "https://github.com/RajaATAli/CSCI365_481_Final_Project",
        },
        {
            "title": "Counts of Bushels Project (Agricultural Data Analysis)",
            "image": "images/PDM_Final.png",
            "description": "Designed a 5NF relational database for Indiana's crop yield tracking in SQL Server 2022. Developed SQL-based ETL workflows for transforming agricultural data, enabling efficient trend analysis and decision-making.",
            "outcome": [
                "Reduced query execution time by 40% with optimized data storage.",
                "Improved scalability for handling large agricultural datasets.",
                "Enabled real-time decision-making for 100+ stakeholders."
            ],
            "technologies": [
                "<span style='color:#FF6347; font-weight:bold;'>Database:</span> SQL Server 2022, PostgreSQL",
                "<span style='color:#FF6347; font-weight:bold;'>ETL:</span> Data Ingestion, Transformation, Storage",
                "<span style='color:#FF6347; font-weight:bold;'>Query Optimization:</span> Indexing, Joins, Stored Procedures"
            ],
            "github": "https://github.com/Aopandey/5NF-Counts-of-Bushels-Project",
            "report": "https://drive.google.com/file/d/11g0LNbEw1lXqfwNd4_bknOUOafn1h8pD/view?usp=drive_link"
        },
        {
            "title": "Money Buddy – Personalized Financial Tracker",
            "image": "images/buddy.png",
            "description": "Developed Money Buddy, a CLI-based personal finance tracker that allows users to log and analyze income/expenses. Implemented secure data storage with Java Serialization and CSV export for financial reports.",
            "outcome": [
                "Simplified personal finance tracking for budget management.",
                "Ensured data persistence across user sessions.",
                "Implemented CSV export for generating financial reports."
            ],
            "technologies": [
                "<span style='color:#FF6347; font-weight:bold;'>Programming:</span> Java",
                "<span style='color:#FF6347; font-weight:bold;'>Data Storage:</span> Java Serialization, CSV Export",
                "<span style='color:#FF6347; font-weight:bold;'>Software Design:</span> Modular Architecture, Exception Handling"
            ],
            "github": "https://github.com/RajaATAli/MoneyBuddy",
            "report": "https://drive.google.com/file/d/18uYUz0HpNfe0BvyCt0CsLnX7DmPmM0Zw/view?usp=drive_link"
        },
        {
            "title": "Weather Station Data Hub (Real-Time API & Analytics)",
            "image": "images/weather.png",
            "description": "Built a Flask-powered API for real-time weather data retrieval and analysis with 99% uptime. Integrated Pandas for historical queries and data filtering, ensuring efficient climate trend analysis.",
            "outcome": [
                "Delivered real-time weather data with 99% uptime.",
                "Enabled historical and real-time data retrieval for research.",
                "Designed a scalable API for seamless integration."
            ],
            "technologies": [
                "<span style='color:#FF6347; font-weight:bold;'>Web API:</span> Flask, REST API",
                "<span style='color:#FF6347; font-weight:bold;'>Data Processing:</span> Pandas, NumPy",
                "<span style='color:#FF6347; font-weight:bold;'>Deployment:</span> Docker"
            ],
            "github": "https://github.com/Aopandey/Weather-Station-Data-Hub",
        }
    ]


    # --- DISPLAY PROJECTS ---
    for project in projects:
        content_container = st.container()
        with content_container:
            left_space, content_col, right_space = st.columns([1, 3, 1])
            with content_col:
                inner_col1, inner_col2 = st.columns([1, 2])
                st.write("---")  # Separator between projects

                with inner_col1:
                    st.image(Image.open(project["image"]), width=500)
                    st.markdown("<br>", unsafe_allow_html=True)

                with inner_col2:
                    st.markdown(f"<h3>{project['title']}</h3>", unsafe_allow_html=True)
                    st.markdown(f"<p style='font-size:1.1em;'>{project['description']}</p>", unsafe_allow_html=True)
                    st.markdown("<span style='color:#1E90FF; font-size:1.3em; font-weight:bold;'>📈 **Outcome:**</span>", unsafe_allow_html=True)
                    for outcome in project["outcome"]:
                        st.markdown(f"- {outcome}", unsafe_allow_html=True)
                    st.markdown("<br>", unsafe_allow_html=True)

                    st.markdown("🛠 <span style='color:#1E90FF; font-size:1.3em; font-weight:bold;'>**Technologies Used:**</span>", unsafe_allow_html=True)
                    for tech in project["technologies"]:
                        st.markdown(f"- {tech}", unsafe_allow_html=True)
                    st.markdown("<br>", unsafe_allow_html=True)

                    # GitHub and Report Links in One Row
                    github_link = f"🐙 <a href='{project['github']}' target='_blank' style='margin-right: 30px; color:#1E90FF;'>GitHub</a>"
                    report_link = project.get("report", "")
                    if report_link:
                        github_link += f" 📄 <a href='{report_link}' target='_blank' style='color:#1E90FF;'>Report</a>"
                    st.markdown(f"<div style='display: flex; align-items: center;'>{github_link}</div>",
                                unsafe_allow_html=True)
