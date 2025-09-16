pipeline {
    agent any

    environment {
        BASE_URL = credentials('BASE_URL')
        USER_NAME = credentials('USER_NAME')
        PASSWORD = credentials('PASSWORD')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rak2712/orangehrm-tests.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t orangehrm_automation .'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    def exitCode = sh(
                        script: '''
                            mkdir -p reports
                            docker run --rm \
                                -e BASE_URL=$BASE_URL \
                                -e USER_NAME=$USER_NAME \
                                -e PASSWORD=$PASSWORD \
                                -v $PWD:/app \
                                orangehrm_automation \
                                pytest --junitxml=/app/reports/results.xml
                        ''',
                        returnStatus: true
                    )
                }
            }
        }

        stage('Publish Test Report') {
            steps {
                junit allowEmptyResults: true, testResults: 'reports/results.xml'
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up...'
            junit allowEmptyResults: true, testResults: 'reports/results.xml'
        }

        failure {
            echo '❌ Build failed!'
        }

        success {
            echo '✅ Build succeeded!'
        }
    }
}
