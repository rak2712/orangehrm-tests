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

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                    mkdir -p reports
                    pytest --junitxml=reports/results.xml || true
                '''
            }
        }

        stage('Parse Test Results') {
            steps {
                script {
                    def result = readFile('reports/results.xml')
                    def passed = (result =~ /<testcase /).count() - (result =~ /<failure>/).count()
                    def failed = (result =~ /<failure>/).count()
                    def total = passed + failed

                    echo "✅ Passed: ${passed}"
                    echo "❌ Failed: ${failed}"
                    echo "📊 Total: ${total}"

                    currentBuild.description = "Pass: ${passed}, Fail: ${failed}"

                    if (total > 0 && failed >= Math.ceil(total * 0.5)) {
                        error("Too many failed test cases: ${failed}/${total}")
                    } else if (failed > 0) {
                        currentBuild.result = 'UNSTABLE'
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
        }
        failure {
            echo '❌ Build failed!'
        }
        success {
            echo '✅ Build succeeded!'
        }
    }
}
