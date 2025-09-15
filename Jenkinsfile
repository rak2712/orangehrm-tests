pipeline {
    agent none

    stages {
        stage('Test on Linux') {
            agent { label 'linux' }

            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    pytest tests
                '''
            }
        }

        stage('Test on Windows') {
            agent { label 'windows' }

            steps {
                bat '''
                    python -m venv venv
                    venv\\Scripts\\activate
                    pip install -r requirements.txt
                    pytest tests
                '''
            }
        }
    }

    post {
        always {
            junit 'tests/test-results.xml'
        }
    }
}
