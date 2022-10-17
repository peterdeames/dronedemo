pipeline {
  agent any
  options{
    timestamps()
    buildDiscarder logRotator(artifactDaysToKeepStr: '1', artifactNumToKeepStr: '', daysToKeepStr: '7', numToKeepStr: '')
    disableConcurrentBuilds()
    timeout(time: 5, unit: 'MINUTES')
  }
  stages {
    stage('SonarQube analysis') {
      steps {
        script {
          def scannerHome = tool 'SonarScanner';
          withSonarQubeEnv('SonarCloud') {
            sh "${tool("SonarScanner")}/bin/sonar-scanner -Dsonar.organization=peterdeames -Dsonar.projectKey=peterdeames_dronedemo -Dsonar.sources=. -Dsonar.branch.name='${env.BRANCH_NAME}' -Dsonar.projectVersion='${BUILD_NUMBER}' -Dsonar.host.url=https://sonarcloud.io -Dsonar.python.version=3.8"
          }
        }
      }
    }
    stage("Quality gate") {
      steps {
        script {
          for(int i = 0;i<9;i++) {
            qualitygate = waitForQualityGate();
            if(qualitygate.status == 'OK')
              break;
            sleep(10)
          }
          if (qualitygate.status != "OK") {
            waitForQualityGate abortPipeline: true
          }
        }
      }
    }
    stage('Setup'){
      steps {
        sh 'pip3 install -r requirements.txt'
        sh 'python3 wifi_setup.py'
      }
    }
    stage('Test Flight'){
      steps {
        sh 'python3 test_flight.py'
      }
    }
    stage('Square Dance'){
      steps {
        sh 'python3 square.py'
      }
    }
    stage('Flip n Flight'){
      steps {
        sh 'python3 flip.py'
      }
    }
  }
  post{
    always{
      sh 'python3 wifi_disconnect.py'
    }
  }
}
