node {
    stage("Git pull") {
        git poll: true, url: "git@gitlab.acirrustech.com:deployment/applicaiton_deployment.git"
    }
    stage("Copy files ") {
        sh "scp -r ${workspace}/* root@${hostname}:/apps/"
    }
    stage("Install packages"){
        sh "ssh root@${hostname}    pip install -r /apps/requirements.txt"
    }
    stage("Run services"){
        sh "ssh root@${hostname}    nohup  python /apps/app.py & "
    }
}
