pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-app:${BUILD_NUMBER}"
        INSTANCE_COUNT = 5
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

        stage('Run New Containers') {
            steps {
                script {
                    for (int i = 1; i <= INSTANCE_COUNT.toInteger(); i++) {
                        def containerName = "app${i}-build${BUILD_NUMBER}"
                        def volumeName = "vol-app${i}"

                        // Ensure volume exists
                        sh "docker volume create ${volumeName}"

                        // Run container using existing volume
                        def port = 5000 + i
                        sh """
                            docker run -d \
                              --name ${containerName} \
                              -v ${volumeName}:/data \
                              -e APP_VERSION="${containerName}" \
                              -p ${port}:5000 \
                              $IMAGE_NAME
                        """
                    }
                }
            }
        }
    }
}
