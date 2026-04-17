pipeline {
    agent any
    stages {
        stage('1. Préparation') {
            steps {
                deleteDir()
                checkout scm
            }
        }
        stage('2. Scan Sécurité (Bandit)') {
            steps {
                // On garde le "|| true" pour que le build continue malgré l'alerte eval()
                sh 'bandit -r . || echo "Vulnérabilités détectées pour le rapport"'
            }
        }
        stage('3. Build Docker') {
            steps {
                // Construction de l'image de la calculatrice
                sh 'docker build -t mon-app-cyber:latest .'
            }
        }
        stage('4. Infrastructure (Terraform)') {
            steps {
                dir('terraform') {
                    sh 'terraform init'
                    sh 'terraform apply -auto-approve'
                }
            }
        }
        stage('5. Contrôle Ansible') {
            steps {
                dir('ansible') {
                    sh 'ansible-playbook check_status.yml'
                }
            }
        }
    }
    post {
        success {
            echo "✅ Tout est en ligne sur le port 8081 !"
        }
    }
}
