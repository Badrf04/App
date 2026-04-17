pipeline {
    agent any
    environment {
        CONTAINER_NAME = "openrecon-service"
    }
    stages {
        stage('0. Nettoyage') {
            steps {
                sh "docker rm -f ${CONTAINER_NAME} || true"
            }
        }
        stage('1. Sécurité') {
            steps {
                sh 'bandit -r . || echo "Vulnérabilités notées"'
            }
        }
        stage('2. Build Image') {
            steps {
                sh 'docker build -t mon-app-cyber:latest .'
            }
        }
        stage('3. Terraform Deploy') {
            steps {
                dir('terraform') {
                    sh 'terraform init'
                    sh 'terraform apply -auto-approve'
                }
            }
        }
        stage('4. Ansible Audit') {
            steps {
                dir('ansible') {
                    sh 'ansible-playbook check_status.yml'
                }
            }
        }
    }
    post {
        success {
            echo "URL : http://localhost:8081"
        }
    }
}
