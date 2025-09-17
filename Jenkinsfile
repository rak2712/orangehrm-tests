pipeline {
    agent any

    environment {
        BASE_URL = credentials('BASE_URL')
        USER_NAME = credentials('USER_NAME')
        PASSWORD = credentials('PASSWORD')
    }

    stages {
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

                    # Run pytest and generate JUnit XML report
                    pytest --junitxml=reports/results.xml || true

                    # Make sure Jenkins can read the report
                    if [ -f reports/results.xml ]; then
                        chmod 777 reports/results.xml
                    fi
                '''
            }
        }

        stage('Parse Test Results') {
            steps {
                script {
                    def resultsFile = 'reports/results.xml'
                    if (fileExists(resultsFile)) {
                        def content = readFile(resultsFile)

                        // Count occurrences of tags in the raw XML string
                        def total = content.count('<testcase')
                        def failed = content.count('<failure')
                        def passed = total - failed

                        echo "📊 Total: ${total}, ✅ Passed: ${passed}, ❌ Failed: ${failed}"

                        currentBuild.description = "✅ ${passed} | ❌ ${failed}"
                        currentBuild.displayName = "#${env.BUILD_NUMBER} pass = ${passed} fail = ${failed}"

                        if (total > 0 && failed > (total / 2)) {
                            error("More than 50% of test cases failed. Failing the build.")
                        }
                    } else {
                        echo "⚠️ Test results file not found: ${resultsFile}"
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
