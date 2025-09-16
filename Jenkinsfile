pipeline {
    agent { label 'ubuntu' }

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

        stage('Deploy on Ubuntu') {
            steps {
                echo 'Running Docker container on Ubuntu...'
                sh '''
                    echo "Using BASE_URL: $BASE_URL"
                    echo "Logging in with USER_NAME: $USER_NAME"
                    docker run --rm \
                        -e BASE_URL=$BASE_URL \
                        -e USER_NAME=$USER_NAME \
                        -e PASSWORD=$PASSWORD \
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
