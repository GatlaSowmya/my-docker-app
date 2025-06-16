pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-app:${BUILD_NUMBER}"
        CONTAINER_NAME = "app${BUILD_NUMBER}"
        VOLUME_NAME = "vol-${CONTAINER_NAME}"
        PORT = "${BUILD_NUMBER + 5000}" // Example: build #1 => port 5001
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

        stage('Create Volume (if not exists)') {
            steps {
                sh """
                if [ -z "\$(docker volume ls -q -f name=$VOLUME_NAME)" ]; then
                  docker volume create $VOLUME_NAME
                fi
                """
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    sh """
                        docker run -d --name $CONTAINER_NAME \\
                        -v $VOLUME_NAME:/data \\
                        -e APP_VERSION=$CONTAINER_NAME \\
                        -p $PORT:5000 \\
                        $IMAGE_NAME
                    """
                }
            }
        }

        stage('Show All Running Containers') {
            steps {
                sh 'docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"'
            }
        }
    }
}
