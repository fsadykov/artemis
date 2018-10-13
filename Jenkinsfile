// Farkhod Sadykov
node {
   stage("Git pull") {
       git poll: true, url: "git@gitlab.acirrustech.com:deployment/applicaiton_deployment.git"
   }
   stage("Createing apps Folder") {
     // This line will check /apps folder if doesn't exist will create
     sh "ssh root@${hostname} 'if [ -d /apps ]; then echo 'Folder is exist'; else mkdir /apps; fi'"
   }

   stage("Copy everything from workspace to remote host") {
       sh "rsync -avz --delete ${workspace}/* root@${hostname}:/apps/"
   }

   stage('Installing packages for application') {
     // run.sh script will install packages on remote host
     sh "ssh root@${hostname} 'sh /apps/run.sh'"
   }

   stage("Installing modules"){
     // requirements.txt file contents are modules name for python application
       sh "ssh root@${hostname}    pip install -r /apps/requirements.txt"
   }

   stage("Run the application"){
     // We use nohub command to run app on baground
       sh "ssh root@${hostname}  'nohup  python /apps/app.py &' "
   }
   
}
