pipeline {
    agent any
    
    environment {
        IMAGE_NAME = "projeto-devsecops-web"
        KUBE_NAMESPACE = "default"
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/edhuardo666/iac_local_secops.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${BUILD_NUMBER}")
                }
            }
        }
        
        stage('Test Application') {
            steps {
                script {
                    // Testes simples de health check
                    docker.image("${IMAGE_NAME}:${BUILD_NUMBER}").inside {
                        sh '''
                            echo "Executando testes básicos..."
                            # Aqui viriam testes unitários, de integração, etc.
                        '''
                    }
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Carregar imagem no K3s
                    sh """
                        docker save ${IMAGE_NAME}:${BUILD_NUMBER} -o ${IMAGE_NAME}.tar
                        sudo k3s ctr images import ${IMAGE_NAME}.tar
                    """
                    
                    // Atualizar deployment no Kubernetes
                    sh """
                        kubectl set image deployment/web-deployment web=${IMAGE_NAME}:${BUILD_NUMBER} -n ${KUBE_NAMESPACE}
                        kubectl rollout status deployment/web-deployment -n ${KUBE_NAMESPACE}
                    """
                }
            }
        }
    }
    
    post {
        always {
            echo "Pipeline ${BUILD_NUMBER} finalizado!"
            cleanWs()
        }
        success {
            echo "Deploy realizado com sucesso!"
        }
        failure {
            echo "Pipeline falhou - verifique os logs"
        }
    }
}
