pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-app:${BUILD_NUMBER}"
    }

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/<your-username>/my-docker-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Stop Previous Containers') {
            steps {
                script {
                    sh """
                        docker stop app1 || true
                        docker rm app1 || true
                        docker stop app2 || true
                        docker rm app2 || true
                    """
                }
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    // For first build use app1, else use app2
                    def containerName = (env.BUILD_NUMBER.toInteger() % 2 == 0) ? "app2" : "app1"
                    sh "docker run -d --name ${containerName} -p 5000:5000 $IMAGE_NAME"
                }
            }
        }
    }
}

