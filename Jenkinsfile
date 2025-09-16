pipeline {
    agent none

    stages {
        stage('Clone Repository') {
            agent { label 'ubuntu' }
            steps {
                git url: 'https://github.com/rak2712/orangehrm-tests.git', branch: 'main'
            }
        }

        stage('Deploy on Ubuntu') {
            agent { label 'ubuntu' }
            steps {
                echo 'Running Docker container on Ubuntu...'
                sh '''
                    docker run --rm \
                        -v /usr/bin/google-chrome:/usr/bin/google-chrome \
                        -v /usr/bin/chromedriver:/usr/bin/chromedriver \
                        -v $(pwd):/app \
                        -w /app \
                        orangehrm-tests
                '''
            }
        }
    }
}
