pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],  // Specifies the master branch
                    userRemoteConfigs: [[url: 'https://github.com/rakeshsun/ui-test-project.git']]
                ])

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