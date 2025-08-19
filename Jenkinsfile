pipeline {
    agent any

    environment {
        IMAGE_NAME = 'product-catalog-api'
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    sh 'docker-compose -f $DOCKER_COMPOSE_FILE build'
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    // Assuming you have a test target in your service, e.g., pytest for Flask backend
                    sh 'docker-compose -f $DOCKER_COMPOSE_FILE run backend pytest'
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    // Add your DockerHub login and push logic if needed
                    echo 'Push images to DockerHub or private registry here'
                }
            }
        }
    }

    post {
        always {
            sh 'docker-compose -f $DOCKER_COMPOSE_FILE down'
        }
    }
}
