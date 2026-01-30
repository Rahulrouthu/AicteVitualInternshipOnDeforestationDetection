pipeline {
    agent any

    stages {
        stage('Setup venv') {
            steps {
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\pip install --upgrade pip'
                bat 'venv\\Scripts\\pip install pandas numpy scikit-learn flask streamlit'
            }
        }

        stage('Run App') {
            steps {
                bat 'venv\\Scripts\\python app.py'
            }
        }
    }
}




