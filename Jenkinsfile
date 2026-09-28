pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\test\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                bat '"%PYTHON%" --version'
                bat '"%PYTHON%" -c "import sys; print(sys.executable)"'
                bat '"%PYTHON%" -m pip --version'
                bat '"%PYTHON%" -m pip install --upgrade pip'
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat '"%PYTHON%" -m pytest'
            }
        }

        stage('Run Flask') {
            steps {
                bat '"%PYTHON%" app.py'
            }
        }
    }
}
