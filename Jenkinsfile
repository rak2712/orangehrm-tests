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
                    sudo apt-get update
                    sudo apt-get install -y python3-venv

                    python3 -m venv venv
                    . venv/bin/activate

                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    mkdir -p reports
                    pytest --junitxml=reports/results.xml || true
                '''
            }
        }

        stage('Parse Test Results') {
            steps {
                script {
                    def result = readFile('reports/results.xml')
                    def total = (result =~ /<testcase /).count
                    def failed = (result =~ /<failure /).count
                    def passed = total - failed

                    echo "📊 Total: ${total}, ✅ Passed: ${passed}, ❌ Failed: ${failed}"

                    currentBuild.description = "Passed: ${passed}, Failed: ${failed}"

                    if (total > 0 && failed > (total / 2)) {
                        error("More than 50% test cases failed. Failing the build.")
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
