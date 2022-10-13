pipeline {
  agent any
  stages {
    stage('Checkout'){
      steps {
        echo 'LOG: Checkout codebase'
      }
    }
    stage('SonarQube analysis') {
      steps {
        script {
          def scannerHome = tool 'SonarScanner';
          withSonarQubeEnv('sonarqube') {
            sh "${tool("SonarScanner")}/bin/sonar-scanner -Dsonar.organization=peterdeames -Dsonar.projectKey=peterdeames_dronedemo -Dsonar.sources=. -Dsonar.host.url=https://sonarcloud.io"
          }
        }
      }
    }
    stage("Quality gate") {
      steps {
        script {
          def qualitygate = waitForQualityGate()
          sleep(10)
          if (qualitygate.status != "OK") {
            waitForQualityGate abortPipeline: true
          }
        }
      }
    }
  }
}
