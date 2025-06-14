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

        stage('Stop & Remove Existing Containers') {
            steps {
                script {
                    for (int i = 1; i <= 5; i++) {
                        sh """
                            docker rm -f app${i} || true
                        """
                    }
                }
            }
        }

        stage('Create Volumes and Run Containers') {
            steps {
                script {
                    for (int i = 1; i <= 5; i++) {
                        sh """
                            docker volume create vol-app${i}
                            docker run -d \
                                --name app${i} \
                                -e APP_VERSION=${i} \
                                -v vol-app${i}:/data \
                                -p 500${i}:5000 \
                                $IMAGE_NAME
                        """
                    }
                }
            }
        }
    }
}
