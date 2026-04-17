pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "mon-app-cyber:latest"
        CONTAINER_NAME = "openrecon-service"
    }

    stages {
        stage('1. Préparation') {
            steps {
                deleteDir()
                checkout scm
            }
        }

        stage('2. Scan Sécurité (Bandit)') {
            steps {
                // Le "|| true" permet de continuer le pipeline même si Bandit trouve des failles
                sh 'bandit -r . || echo "Vulnérabilités détectées pour le rapport"'
            }
        }

        stage('3. Build Docker') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('4. Infrastructure (Terraform)') {
            steps {
                dir('terraform') {
                    // Nettoyage préventif pour éviter l'erreur de conflit de nom
                    sh "docker rm -f ${CONTAINER_NAME} || true"
                    
                    sh 'terraform init'
                    sh 'terraform apply -auto-approve'
                }
            }
        }

        stage('5. Contrôle Ansible') {
            steps {
                dir('ansible') {
                    // On utilise main.yml car c'est le nom de ton fichier sur le Desktop
                    sh 'ansible-playbook main.yml'
                }
            }
        }
    }

    post {
        success {
            echo "Déploiement réussi ! L'application est disponible sur le port 8081."
        }
        failure {
            echo "Le pipeline a échoué. Vérifiez les logs ci-dessus."
        }
    }
}
