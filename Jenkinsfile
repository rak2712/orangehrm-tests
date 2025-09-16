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
                echo 'Building Docker image from Dockerfile...'
                sh '''
                    docker build -t orangehrm-tests .
                '''
            }
        }

        stage('Run Tests in Container') {
            steps {
                echo 'Running tests inside Docker container...'
                sh '''
                    mkdir -p reports

                    docker run --rm \
                        -e BASE_URL=$BASE_URL \
                        -e USER_NAME=$USER_NAME \
                        -e PASSWORD=$PASSWORD \
                        -v $(pwd)/reports:/app/reports \
                        orangehrm-tests
                '''
            }
        }

        stage('Publish Test Report') {
            steps {
                junit 'reports/**/*.xml'
            }
        }
    }
}
