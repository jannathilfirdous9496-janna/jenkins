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
            bat 'python --version'
            bat 'python -m venv venv'
            bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
            bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
        }
    }

    stage('Test') {
        steps {
            bat 'venv\\Scripts\\python.exe -m pytest'
        }
    }

    stage('Run Flask') {
        steps {
            bat 'venv\\Scripts\\python.exe app.py'
        }
    }
}


}
