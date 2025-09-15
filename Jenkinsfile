pipeline {
    agent none

    stages {
        stage('Clone Repository') {
            agent any
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

        stage('Deploy on Windows') {
            agent { label 'windows' }
            steps {
                echo 'Running Docker container on Windows...'
                bat '''
                    docker run --rm ^
                        -v "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe":/usr/bin/google-chrome ^
                        -v "C:\\tools\\chromedriver.exe":/usr/bin/chromedriver ^
                        -v "%cd%":/app ^
                        -w /app ^
                        orangehrm-tests
                '''
            }
        }
    }
}
