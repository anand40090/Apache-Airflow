# Apache-Airflow

### What is Apache Airflow - 
Apache Airflow™ is an open-source platform for developing, scheduling, and monitoring batch-oriented workflows. Airflow’s extensible Python framework enables you to build workflows connecting with virtually any technology. A web interface helps manage the state of your workflows. Airflow is deployable in many ways, varying from a single process on your laptop to a distributed setup to support even the biggest workflows.

### Usefull Links - 
- https://airflow.apache.org/docs/apache-airflow/stable/index.html
- https://www.devopsschool.com/blog/what-is-apache-airflow-and-use-cases-of-apache-airflow/


### Required Tools 
- Install python3
  ```
  sudo apt install python3.8 -y 
  ```
- Install Docker
  ```
  sudo apt install docker.io -y 
  ```
- Install Helm
  ```
  $ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
  $ chmod 700 get_helm.sh
  $ ./get_helm.sh
  ```
- Install Minikube & Kubectl
  ```
  https://linux.how2shout.com/how-to-install-minikube-on-ubuntu-22-04-lts-linux/

  - sudo apt update -y
  - sudo apt install curl wget apt-transport-https -y
  - curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
  - sudo install minikube-linux-amd64 /usr/local/bin/minikube
  - minikube version
  - curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
  - chmod +x ./kubectl
  - sudo mv kubectl /usr/local/bin/
  - kubectl version --client --output=yaml
  - minikube start --vm-driver docker
  - minikube status
  
  ```

### Install Apache Airflow Using Helm chart 
Reference - https://hungngph.medium.com/airflow-on-kubernetes-with-helm-c795545325dc
![image](https://github.com/anand40090/Apache-Airflow/assets/32446706/372c1599-698a-479b-8165-3384e5a3bec7)



