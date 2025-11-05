pipeline {
    agent any

    environment {
        // Directly define the credentials (Not recommended for sensitive info)
        BASE_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        USER_NAME = 'Admin'
        PASSWORD = 'admin123'
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
                    // Here we simulate logging into the application with the hardcoded credentials
                    echo "Logging into ${BASE_URL} with username ${USER_NAME}"

                    // For example, using curl (or a tool like Selenium or another test framework) 
                    // to automate the login process

                    // Example of using curl to send a POST request to login (for an API-based login)
                    sh """
                    curl -X POST ${BASE_URL} -d 'username=${USER_NAME}' -d 'password=${PASSWORD}'
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Add test execution steps here (e.g., using Selenium, Cypress, etc.)
                echo "Running tests against ${BASE_URL}"
                // Your test execution logic
            }
        }
    }

    post {
        always {
            echo 'Cleaning up after pipeline'
            // Any cleanup tasks you want to perform, e.g., archiving test results
        }
    }
}
