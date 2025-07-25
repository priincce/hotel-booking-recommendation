pipeline{
      agent any

      stages {
            stage('Cloning github repo to jenkins'){
                  steps {
                        script {
                              echo 'Cloning the repo to jenkins'
                              checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/priincce/hotel-booking-recommendation.git']])
                        }
                  }
            }
      }
}