pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        
        stage('Code Quality') {
            steps {
                sh '''
                . venv/bin/activate
                black --check .
                isort --check-only .
                flake8 .
                pylint app/ tests/ app.py || true
                '''
            }
        }
        
        stage('Unit Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest --cov=app --cov-report=xml --cov-fail-under=90
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'coverage.xml', fingerprint: true
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t todo-app-image .'
                sh 'docker save todo-app-image > todo-app-image.tar'
            }
            post {
                success {
                    archiveArtifacts artifacts: 'todo-app-image.tar', fingerprint: true
                }
            }
        }
    }
}
