pipeline {
    agent any
    stages {
        stage('0. Reset Docker') {
            steps {
                // Nettoyage pour éviter les conflits de nom
                sh 'docker rm -f openrecon-service || true'
            }
        }
        stage('1. Analyse Bandit') {
            steps {
                sh 'bandit -r . || echo "Vulnérabilités détectées"'
            }
        }
        stage('2. Build Image') {
            steps {
                sh 'docker build -t mon-app-cyber:latest .'
            }
        }
        stage('3. Terraform Infrastructure') {
            steps {
                dir('terraform') {
                    sh 'terraform init'
                    sh 'terraform apply -auto-approve'
                }
            }
        }
        stage('4. Ansible Healthcheck') {
            steps {
                dir('ansible') {
                    // LIAISON : Utilise bien check_status.yml
                    sh 'ansible-playbook check_status.yml'
                }
            }
        }
    }
    post {
        success {
            echo "PIPELINE RÉUSSI : http://localhost:8081"
        }
    }
}
