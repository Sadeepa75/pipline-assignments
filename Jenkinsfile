pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building virtual environment...'
                bat '''
                    "C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                bat '''
                    call venv\\Scripts\\activate
                    pytest --junitxml=test-reports/results.xml
                '''
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }

        stage('Archive Artifacts') {
            steps {
                echo 'Archiving build files...'
                archiveArtifacts artifacts: 'app.py, requirements.txt', fingerprint: true
            }
        }
    }
}