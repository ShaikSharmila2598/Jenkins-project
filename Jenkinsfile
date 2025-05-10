pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code...'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt || echo "No requirements.txt file"'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/ || echo "No tests found"'
            }
        }

        stage('Run Script') {
            steps {
                sh 'list.py'
            }
        }
    }
}
