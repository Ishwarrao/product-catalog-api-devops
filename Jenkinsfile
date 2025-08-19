pipeline {
    agent any

    stages {
        stage('Build Backend Docker Images') {
            steps {
                sh 'docker compose build backend'
            }
        }
        stage('Build Frontend Docker Images') {
            steps {
                sh 'docker compose build frontend'
            }
        }

        
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'wsl docker compose build'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'wsl docker compose run backend pytest'
            }
        }

        stage('Push Docker Images') {
            steps {
                // Add your Docker Hub login & push commands here
                echo 'Pushing images to registry (add implementation)'
            }
        }
    }

    post {
        always {
            sh 'wsl docker compose down'
        }
    }
}
