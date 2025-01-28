pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/rakeshsun/ui-test-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './run_tests.sh'
            }
        }

        stage('Publish Test Report') {
            steps {
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'test_report.html',
                    reportName: 'UI Test Report'
                ])
            }
        }
    }
}