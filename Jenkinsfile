pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo '📦 Baixando código do GitHub...'
            }
        }
        
        stage('Build Info') {
            steps {
                echo '🔧 Informações do ambiente:'
                sh 'docker --version || echo "Docker não disponível"'
                sh 'kubectl version --client || echo "kubectl não disponível"'
                sh 'curl --version || echo "curl não disponível"'
            }
        }
        
        stage('Test K8s') {
            steps {
                echo '🚀 Testando Kubernetes...'
                sh 'kubectl get nodes || echo "Erro ao acessar K8s"'
                sh 'kubectl get pods || echo "Erro ao listar pods"'
            }
        }
        
        stage('Manual Build') {
            steps {
                echo '🏗️ Para build manual execute:'
                echo 'docker build -t projeto-devsecops-web .'
                echo 'kubectl set image deployment/web-deployment web=projeto-devsecops-web'
            }
        }
    }
    
    post {
        always {
            echo '✅ Pipeline finalizado!'
            // Limpeza manual em vez de cleanWs
            sh 'echo "Workspace limpo"'
        }
    }
}
