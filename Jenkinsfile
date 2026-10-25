pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building virtual environment...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '''
                    . venv/bin/activate
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