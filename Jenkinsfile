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
                sh """
                    docker stop app1 || true
                    docker rm app1 || true
                    docker stop app2 || true
                    docker rm app2 || true
                """
            }
        }

        stage('Create Docker Volumes') {
            steps {
                sh """
                    docker volume create vol1 || true
                    docker volume create vol2 || true
                """
            }
        }

        stage('Run Containers with Volume Mounts') {
            steps {
                sh """
                    docker run -d --name app1 -p 5000:5000 -v vol1:/data -e APP_VERSION=1 $IMAGE_NAME
                    docker run -d --name app2 -p 5001:5000 -v vol2:/data -e APP_VERSION=2 $IMAGE_NAME
                """
                echo "✅ app1 running on http://<your-ip>:5000"
                echo "✅ app2 running on http://<your-ip>:5001"
            }
        }
    }
}
