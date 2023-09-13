pipeline {
    agent any  // run on any available agent

    stages {
        stage('Setup Python') {
            steps {
                // Install Python and pip (assuming a Debian-based image)
                sh 'sudo apt update -y && sudo apt install python3 python3-pip -y'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install pytest using pip
                sh 'pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                // Run the tests
                sh 'pytest add_func_test.py'
            }
        }
    }
}
