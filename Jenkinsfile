pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install pandas numpy scikit-learn flask'
            }
        }

        stage('Run App') {
            steps {
                bat 'python app.py'
            }
        }
    }
}


