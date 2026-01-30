pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Rahulrouthu/AicteVirtualInternshipOnDeforestationDetection.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install pandas numpy scikit-learn flask'
            }
        }

        stage('Run App') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
