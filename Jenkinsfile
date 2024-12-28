pipeline {
    agent any
    environment {
        PYTHON_PATH = 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python313\\Scripts'
    }
    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }
        stage("Build") {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                pip install -r requirements.txt
                '''
            }
        }
        stage("Run Tests with Coverage") {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                python -m coverage run -m unittest discover
                python -m coverage xml -o coverage.xml
                '''
            }
        }
        stage("Sonar-Analysis") {
            environment {
                SONAR_TOKEN = credentials('sonar-token')
            }
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                sonar-scanner -Dsonar.projectKey=python-coverage-pipeline ^
                -Dsonar.sources=. ^
                -Dsonar.host.url=http://localhost:9000 ^
                -Dsonar.token=%SONAR_TOKEN%
                -D"sonar.python.coverage.reportPaths=coverage.xml"
                '''
            }
        }
    }
    post {
        success {
            echo "Pipeline completed successfully."
        }
        failure {
            echo "Pipeline failed. Check the logs for details."
        }
    }
}
