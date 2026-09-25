pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 -m pytest
                '''
            }
        }

        stage('Run Flask') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 app.py
                '''
            }
        }
    }
}
