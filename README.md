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

```
   39  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
   40  sudo install minikube-linux-amd64 /usr/local/bin/minikube
   41  minikube version
   42  minikube status
   43  minikube start --vm-driver docker
   44  sudo chmod +777 ///var/run/docker.sock -R
   45  minikube start --vm-driver docker >> To start the minikube with docker 
   46  minikube status >> To check the minikube status
   47 nano value.yaml  >> write value.yaml file for helm airflow installation

Input below mentioned yamal script in value.yaml file
```
![image](https://github.com/anand40090/Apache-Airflow/assets/32446706/5210a006-e44c-49c7-8174-b58ade21c44b)
```
   48  kubectl create namespace airflow && kubectl config set-context --current --namespace=airflow
   49  helm upgrade --install airflow apache-airflow/airflow --namespace airflow --f values.yaml 
   50  helm upgrade --install airflow apache-airflow/airflow --namespace airflow -f values.yaml
```
Output :- 

![image](https://github.com/anand40090/Apache-Airflow/assets/32446706/53f52306-d5ae-424f-b5fc-92abed2bb161)

### Check Airflow Webserver status on Minikube

![image](https://github.com/anand40090/Apache-Airflow/assets/32446706/da82694f-4b68-4817-9c67-fd5a3894e122)

### Now, you can access Airflow UI by using kubectl port-forward:
```
kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow
```
Output :- 
![image](https://github.com/anand40090/Apache-Airflow/assets/32446706/9d229490-e0f6-4257-8d2e-a8fa99b691a6)

### The web server can now be accessed on localhost:8080. The default credentials are username admin and password admin.
Output :- 
![image](https://github.com/anand40090/Apache-Airflow/assets/32446706/ec956be9-8cf5-43ff-a654-e31c8415024d)

![image](https://github.com/anand40090/Apache-Airflow/assets/32446706/e8b24e1a-215a-4848-a6b3-486c3d07a0e1)








