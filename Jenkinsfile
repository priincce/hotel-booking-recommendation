pipeline{
      agent any

      environment {
            VENV_DIR = 'venv'
      }
      stages {
            stage('Cloning github repo to jenkins'){
                  steps {
                        script {
                              echo 'Cloning the repo to jenkins'
                              checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/priincce/hotel-booking-recommendation.git']])
                        }
                  }
            }
            stage('Setup Python Virtual Environment and Install Dependencies') {
                        steps {
                              script {
                                    echo 'Setup Python Virtual Environment and Install Dependencies'
                                    sh '''
                                       python -m venv $VENV_DIR
                                       ./$VENV_DIR/bin/activate
                                       pip install --upgrade pip
                                       pip install -e .
                                    '''
                              }
                        }
                  }
      }
}