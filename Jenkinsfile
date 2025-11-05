pipeline {
    agent any

    environment {
        // Use Jenkins' credentials store to inject values securely
        BASE_URL = credentials('BASE_URL')  // Secret Text for the URL
        USER_NAME = credentials('USER_NAME')  // Username (Admin)
        PASSWORD = credentials('PASSWORD')  // Password (admin123)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm  // Checkout code from SCM (e.g., Git)
            }
        }

        stage('Login to Application') {
            steps {
                script {
                    echo "Logging into ${BASE_URL} with username ${USER_NAME}"

                    // Example: Selenium or curl for logging in
                    sh """
                    curl -X POST ${BASE_URL} -d 'username=${USER_NAME}' -d 'password=${PASSWORD}'
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests against ${BASE_URL}"
                // Run your tests here (e.g., using Selenium or another framework)
            }
        }
    }

    post {
        always {
            echo 'Cleaning up after pipeline'
        }
    }
}
