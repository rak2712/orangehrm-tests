pipeline {
    agent none

    environment {
        BASE_URL = credentials('BASE_URL')
        USER_NAME = credentials('USER_NAME')
        PASSWORD = credentials('PASSWORD')
    }

    stages {
        stage('Clone Repository') {
            agent { node { label 'master' } } // or remove label if controller has no label
            steps {
                git url: 'https://github.com/rak2712/orangehrm-tests.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            agent { node { label 'master' } }
            steps {
                echo 'Building Docker image from Dockerfile...'
                sh '''
                    docker build -t orangehrm-tests .
                '''
            }
        }

        stage('Run Tests in Container') {
            agent { node { label 'master' } }
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
            agent { node { label 'master' } }
            steps {
                junit 'reports/**/*.xml'
            }
        }
    }
}
