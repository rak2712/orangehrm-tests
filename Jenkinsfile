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
                git branch: 'main', url: 'https://github.com/rak2712/orange-deckor.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t orangehrm-selenium .'
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
                                orangehrm-selenium \
                                pytest --junitxml=/app/reports/results.xml
                        ''',
                        returnStatus: true
                    )

                    if (exitCode != 0) {
                        currentBuild.result = 'UNSTABLE'  // Mark as unstable if tests fail
                    }
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

            script {
                def result = currentBuild.rawBuild.getAction(hudson.tasks.junit.TestResultAction.class)
                if (result != null) {
                    int total = result.totalCount
                    int failed = result.failCount
                    int passed = total - failed

                    def green = "\u001B[32m"
                    def red = "\u001B[31m"
                    def reset = "\u001B[0m"

                    ansiColor('xterm') {
                        echo "${green}✅ Passed: ${passed}${reset}"
                        echo "${red}❌ Failed: ${failed}${reset}"
                    }
                } else {
                    echo "No test results found."
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
