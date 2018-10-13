node {
    stage("Stage1"){
        sh 'ssh root@${IP}    yum install httpd -y'
    }
    stage("Sleep 5"){
        sleep 5
    }
    
    stage("Pull Code"){
        git 'git@gitlab.acirrustech.com:deployment/applicaiton_deployment.git'
    }
    
    stage("Copy App"){
        sh "scp  -r ${workspace}/*        root@${IP}:/tmp"
    }
    
    stage("Install Packages"){
        sh 'ssh root@${IP}  yum -y install epel-release   python-pip  mariadb-devel  gcc install python-devel libxslt-devel libffi-devel openssl-devel'
    }
    
    stage("Python Dependencies"){
        sh 'ssh root@${IP} pip install -r /tmp/requirements.txt'

    }
    stage("Run App"){
        sh 'ssh root@${IP} nohup python /tmp/app.py &'
    }
    
    
}
