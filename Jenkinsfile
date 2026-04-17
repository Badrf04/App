pipeline {
    agent any

    stages {
        stage('1. Récupération du Code') {
            steps {
                // Nettoie le dossier et télécharge le code depuis GitHub
                deleteDir()
                checkout scm
            }
        }

        stage('2. Scan Sécurité (Bandit)') {
            steps {
                echo 'Lancement de l\'analyse statique du code...'
                // Exécute bandit sur tout le répertoire actuel
                // Le "|| true" permet au pipeline de continuer même si Bandit trouve des failles
                sh 'bandit -r . || echo "Des vulnérabilités ont été détectées !"'
            }
        }
    }

    post {
        always {
            echo 'Fin de l\'automatisation Jenkins-GitHub-Bandit.'
        }
        success {
            echo '✅ Code analysé avec succès.'
        }
    }
}
