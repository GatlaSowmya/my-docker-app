pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-app:${BUILD_NUMBER}"
    }

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/GatlaSowmya/my-docker-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Stop Previous Containers') {
            steps {
                sh """
                    docker rm -f app1 || true
                    docker rm -f app2 || true
                """
            }
        }

        stage('Run Both Containers') {
            steps {
                sh """
                    docker run -d --name app1 -p 5000:5000 -e APP_VERSION=1 $IMAGE_NAME
                    docker run -d --name app2 -p 5001:5000 -e APP_VERSION=2 $IMAGE_NAME
                """
            }
        }
    }
}
