stages {

    stage('Checkout') {
        steps {
            checkout scm
        }
    }

    stage('Setup') {
        steps {
            bat '''
                python --version
                python -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
            '''
        }
    }

    stage('Test') {
        steps {
            bat '''
                call venv\\Scripts\\activate
                python -m pytest
            '''
        }
    }

    stage('Run Flask') {
        steps {
            bat '''
                call venv\\Scripts\\activate
                start /B python app.py
                timeout /t 5 /nobreak
                curl --fail http://127.0.0.1:5000/
            '''
        }
    }
}


