pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building virtual environment...'
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv venv
                            venv/bin/python -m pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv venv
                            venv\\Scripts\\python.exe -m pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                script {
                    if (isUnix()) {
                        bat '''
                            mkdir -p test-reports
                            venv/bin/python -m pytest --junitxml=test-reports/results.xml
                        '''
                    } else {
                        bat '''
                            if not exist test-reports mkdir test-reports
                            venv\\Scripts\\python.exe -m pytest --junitxml=test-reports/results.xml
                        '''
                    }
                }
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