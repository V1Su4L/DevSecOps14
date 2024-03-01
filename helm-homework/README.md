# helm-exercise

## docker and application. 
this is a simple react application runs on port 3000
in the repo ther is a dockerfile to build the docker image
create the docker image and upload it to docker hub throw your account 

# helm chart
using the helm commands create a new helm chart file 
## template 
build a deployment yaml and a nodeport yaml

### deployment and serivce 
build a deployment for K8s
the type of the service must be a node port

### the values.yml
the values file must containe the following vlues : 
deployment:
  applicationname: 
  labelkey: 
  labelvalue: 
  numberofreplicas:
  imageurl:
  port:
service:
  nodeprot:
  targetport: must take the port from the deployment values
  port:
  
  
# goodluck
