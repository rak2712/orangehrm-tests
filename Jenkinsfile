pipeline {
    agent any

    environment {
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
                    echo "Logging into ${BASE_URL} with username ${USER_NAME}"
                    // Perform login via curl or use a testing framework like Selenium
                    sh """
                    curl -X POST ${BASE_URL} -d 'username=${USER_NAME}' -d 'password=${PASSWORD}'
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "Running tests against ${BASE_URL}"

                    // Simulate a test execution with a testing framework (e.g., JUnit or TestNG)
                    // Example: Run your test suite (JUnit or TestNG command here)
                    // You can replace this with the actual command to run your tests
                    sh """
                    # For example, running tests using Maven or Gradle (replace with your test command)
                    mvn clean test  // Assuming you are using Maven
                    """

                    // Archive JUnit test results (Assuming you are using JUnit for test reporting)
                    junit '**/target/test-*.xml'  // Path to your JUnit test results
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up after pipeline'
            // Archive or display test results if necessary

            // You can also display the total number of tests passed/failed in the post-action
            // This will show the result of the junit tests at the end
            junit '**/target/test-*.xml' // Path to your test results (JUnit XML format)
        }
    }
}
