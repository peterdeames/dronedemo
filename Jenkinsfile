pipeline {
  agent any
  stages {
    stage('SonarQube analysis') {
      steps {
        script {
          def scannerHome = tool 'SonarScanner';
          withSonarQubeEnv('SonarCloud') {
            sh "${tool("SonarScanner")}/bin/sonar-scanner -Dsonar.organization=peterdeames -Dsonar.projectKey=peterdeames_dronedemo -Dsonar.sources=. -Dsonar.branch.name='${env.BRANCH_NAME}' -Dsonar.host.url=https://sonarcloud.io -Dsonar.python.version=3.8"
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
    stage('Build'){
      steps {
        sh 'python3 test_flight.py'
      }
    }
  }
}
