pipeline {
    agent any
   
     environment {
        registryCredential = 'ecr:us-east-1:awscred'
        appRegistry = "646218025121.dkr.ecr.us-east-1.amazonaws.com/fast-repo"
        vprofileRegistry = "https://646218025121.dkr.ecr.us-east-1.amazonaws.com"
    }
  stages {

        stage('Build App Image') {
       steps {
       
         script {
                    dockerImage = docker.build(appRegistry + ":$BUILD_NUMBER", ".")
                }

            }

        }

        stage('Upload App Image') {
          steps{
            script {
                    docker.withRegistry(vprofileRegistry, registryCredential) {
                        dockerImage.push("$BUILD_NUMBER")
                        dockerImage.push('latest')
                    }
                }
            }
        }

    }
}
