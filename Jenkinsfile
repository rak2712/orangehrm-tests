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
                    // Run tests and save exit code, but don't fail pipeline immediately
                    def status = sh(script: '''
                        mkdir -p reports
                        docker run --rm \
                            -e BASE_URL=$BASE_URL \
                            -e USER_NAME=$USER_NAME \
                            -e PASSWORD=$PASSWORD \
                            -v $(pwd)/reports:/app/reports \
                            orangehrm-tests
                    ''', returnStatus: true)

                    // Mark build unstable on test failures, but do not fail pipeline
                    if (status != 0) {
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }

        stage('Publish Test Report') {
            steps {
                // Publish JUnit reports from reports folder
                junit allowEmptyResults: true, testResults: 'reports/**/*.xml'
            }
        }
    }

    post {
        always {
            script {
                def testResult = currentBuild.rawBuild.getAction(hudson.tasks.junit.TestResultAction.class)

                if (testResult != null) {
                    int total = testResult.totalCount
                    int failed = testResult.failCount
                    int passed = total - failed

                    def green = "\u001B[32m" // green color
                    def red = "\u001B[31m"   // red color
                    def reset = "\u001B[0m"  // reset color

                    ansiColor('xterm') {
                        println("${green}Tests Passed: ${passed}${reset}")
                        println("${red}Tests Failed: ${failed}${reset}")
                    }
                } else {
                    println("No test results found.")
                }
            }
        }

        failure {
            echo '❌ Build failed!'
        }

        success {
            echo '✅ Build succeeded!'
        }
    }
}
