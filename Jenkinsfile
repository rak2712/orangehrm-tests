stage('Run Tests in Container') {
    steps {
        script {
            // Run tests but don't fail the whole pipeline if tests fail
            def status = sh(script: '''
                mkdir -p reports
                docker run --rm \
                    -e BASE_URL=$BASE_URL \
                    -e USER_NAME=$USER_NAME \
                    -e PASSWORD=$PASSWORD \
                    -v $(pwd)/reports:/app/reports \
                    orangehrm-tests
            ''', returnStatus: true)

            // Save status in variable for later use
            currentBuild.result = (status == 0) ? 'SUCCESS' : 'UNSTABLE'
        }
    }
}

stage('Publish Test Report') {
    steps {
        junit allowEmptyResults: true, testResults: 'reports/**/*.xml'
    }
}
