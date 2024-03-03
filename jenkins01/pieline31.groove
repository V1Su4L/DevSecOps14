pipeline{
    agent any
    stages{
        stage('checkout'){
            steps{
                sh 'rm -fr demo1 && git clone https://github.com/hothaifa96/demo1'
            }
        }
        stage('Build'){
            steps{
                sh 'python3 main.py' 
            }
        }
        stage('Testing'){
            steps{
                sh 'echo testing'
            }
        }
        stage('Build Image'){
            steps{
                sh 'echo Build Image'
            }
        }
        stage('Push Image'){
            steps{
                sh 'echo Push Image'
            }
        }
    }
}