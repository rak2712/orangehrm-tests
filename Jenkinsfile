pipeline {
    agent any

    environment {
        BASE_URL = credentials('BASE_URL')
        USER_NAME = credentials('USER_NAME')
        PASSWORD = credentials('PASSWORD')
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/rak2712/orangehrm-tests.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t orangehrm-tests .'
            }
        }

        stage('Run Tests in Container') {
            steps {
                script {
                    def status = sh(script: '''
                        mkdir -p reports
                        docker run --rm \
                            -e BASE_URL=$BASE_URL \
                            -e USER_NAME=$USER_NAME \
                            -e PASSWORD=$PASSWORD \
                            -v $(pwd)/reports:/app/reports \
                            orangehrm-tests
                    ''', returnStatus: true)
                    currentBuild.result = (status == 0) ? 'SUCCESS' : 'UNSTABLE'
                }
            }
        }

        stage('Publish Test Report') {
            steps {
                junit allowEmptyResults: true, testResults: 'reports/**/*.xml'
            }
        }
    }

    post {
        always {
            script {
                // Read test result summary from junit step's built-in variables
                def testResult = currentBuild.rawBuild.getAction(hudson.tasks.junit.TestResultAction.class)

                if (testResult != null) {
                    int total = testResult.totalCount
                    int failed = testResult.failCount
                    int passed = total - failed
                    def green = "\u001B[32m"
                    def red = "\u001B[31m"
                    def reset = "\u001B[0m"

                    // Print colored summary to console log
                    ansiColor('xterm') {
                        println("${green}Tests Passed: ${passed}${reset}")
                        println("${red}Tests Failed: ${failed}${reset}")
                    }
                } else {
                    println("No test results found.")
                }
            }
        }
    }
}
