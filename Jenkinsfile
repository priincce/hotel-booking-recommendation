pipeline{
      agent any

      environment {
            VENV_DIR = 'venv'
            GCP_PROJECT = 'avian-volt-464115-a4'
            GCLOUD_PATH = '/var/jenkins_home/google-cloud-sdk/bin'
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
            
            stage('Setting up Virtual Environment and Installing Dependencies') {
                  steps {
                        script {
                              echo 'Setup Python Virtual Environment and Install Dependencies'
                              sh  '''
                                    python -m venv ${VENV_DIR}
                                    . ${VENV_DIR}/bin/activate
                                    pip install --upgrade pip
                                    pip install -e .
                              '''
                        }
                  }
            }

            stage('Building and Pushing Docker Image to GCR') {
                  steps {
                        script {
                              withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                                    sh '''
                                          echo "Building and Pushing Docker Image to GCR........................."
                                          export PATH=$PATH:${GCLOUD_PATH}
                                          gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                                          gcloud config set project ${GCP_PROJECT}
                                          gcloud auth configure-docker --quiet
                                          docker build -t gcr.io/${GCP_PROJECT}/hotel-booking-recommendation:latest .
                                          docker push gcr.io/${GCP_PROJECT}/hotel-booking-recommendation:latest
                                    '''
                              }
                        }
                  }
            }

            stage('Deploying to google cloud run') {
                  steps {
                        script {
                              withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                                    sh '''
                                          echo "Deploying to Google Cloud Run........................."
                                          export PATH=$PATH:${GCLOUD_PATH}
                                          gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                                          gcloud config set project ${GCP_PROJECT}

                                          gcloud run deploy hotel-booking-recommendation \
                                             --image=gcr.io/${GCP_PROJECT}/hotel-booking-recommendation:latest \
                                             --platform=managed \
                                             --region=us-central1 \
                                             --allow-unauthenticated
                                    '''
                              }
                        }
                  }
            }
      }
}