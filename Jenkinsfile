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
                    python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pip install --upgrade pip --break-system-packages
                    pip install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                    . venv/bin/activate

                    mkdir -p reports
                    chmod -R 777 reports

                    pytest --junitxml=reports/results.xml || true
                '''
            }
        }

        stage('Parse Test Results') {
            steps {
                script {
                    def result = readFile('reports/results.xml')
                    def total = 0
                    def failed = 0

                    for (line in result.readLines()) {
                        if (line.contains("<testcase")) total++
                        if (line.contains("<failure")) failed++
                    }

                    def passed = total - failed

                    echo "📊 Total: ${total}, ✅ Passed: ${passed}, ❌ Failed: ${failed}"
                    currentBuild.description = "✅ ${passed} | ❌ ${failed}"

                    if (total > 0 && failed > (total / 2)) {
                        error("More than 50% of test cases failed. Failing the build.")
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

        success {
            echo '✅ Build succeeded!'
        }

        failure {
            echo '❌ Build failed!'
        }
    }
}
