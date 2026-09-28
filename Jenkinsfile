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
                bat '''
                    start "" /B "%PYTHON%" app.py
                    timeout /T 5 /NOBREAK
                    curl.exe -f http://127.0.0.1:5000
               '''
            }
        }
    }

    post {
        always {
            bat '''
                for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":5000" ^| findstr "LISTENING"') do taskkill /PID %%a /F >nul 2>&1
            '''
        }

        success {
            echo 'Jenkins pipeline completed successfully!'
        }

        failure {
            echo 'Jenkins pipeline failed.'
        }
    }
}


