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
                        orangehrm_automation \
                        pytest --junitxml=/app/reports/results.xml
                ''',
                returnStatus: true
            )
            
            def testResults = readFile('reports/results.xml')
            def xml = new XmlSlurper().parseText(testResults)

            def totalTests = xml.testsuite.@tests.toInteger()
            def failures = xml.testsuite.@failures.toInteger()
            def errors = xml.testsuite.@errors.toInteger()
            def skipped = xml.testsuite.@skipped.toInteger()
            
            def failedTests = failures + errors
            echo "Total tests: ${totalTests}, Failed tests (failures + errors): ${failedTests}, Skipped: ${skipped}"

            if (failedTests >= totalTests * 0.5) {
                currentBuild.result = 'FAILURE'
            } else if (failedTests > 0) {
                currentBuild.result = 'UNSTABLE'
            } else {
                currentBuild.result = 'SUCCESS'
            }
        }
    }
}
