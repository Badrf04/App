pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "mon-app-cyber:latest"
        CONTAINER_NAME = "openrecon-service"
    }

    stages {
        stage('0. Nettoyage Initial') {
            steps {
                echo "Suppression des anciens conteneurs..."
                sh "docker rm -f ${CONTAINER_NAME} || true"
            }
        }

        stage('1. Préparation') {
            steps {
                deleteDir()
                checkout scm
            }
        }

        stage('2. Scan Sécurité (Bandit)') {
            steps {
                sh 'bandit -r . || echo "Vulnérabilités détectées"'
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
                    sh 'terraform init'
                    sh 'terraform apply -auto-approve'
                }
            }
        }

        stage('5. Contrôle Ansible') {
            steps {
                dir('ansible') {
                    echo "Lancement du playbook de vérification..."
                    // Correction ici : nom du fichier trouvé avec ls
                    sh 'ansible-playbook check_status.yml'
                }
            }
        }
    }

    post {
        success {
            echo "-----------------------------------------------------------"
            echo "PIPELINE TERMINÉ AVEC SUCCÈS !"
            echo "Application disponible sur : http://localhost:8081"
            echo "-----------------------------------------------------------"
        }
    }
}
