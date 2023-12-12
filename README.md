# Apache-Airflow

### What is Apache Airflow - 
Apache Airflow™ is an open-source platform for developing, scheduling, and monitoring batch-oriented workflows. Airflow’s extensible Python framework enables you to build workflows connecting with virtually any technology. A web interface helps manage the state of your workflows. Airflow is deployable in many ways, varying from a single process on your laptop to a distributed setup to support even the biggest workflows.

### Usefull Links - 
- https://airflow.apache.org/docs/apache-airflow/stable/index.html
- https://www.devopsschool.com/blog/what-is-apache-airflow-and-use-cases-of-apache-airflow/

# Method-1 by using helm chart

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
  - curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
  - sudo install minikube-linux-amd64 /usr/local/bin/minikube
  - minikube version
  - minikube status
  - minikube start --vm-driver docker
  - sudo chmod +777 ///var/run/docker.sock -R
  - minikube start --vm-driver docker >> To start the minikube with docker 
  - minikube status >> To check the minikube status
  - nano value.yaml  >> write value.yaml file for helm airflow installation

Input below mentioned yamal script in value.yaml file

![image](https://github.com/anand40090/Apache-Airflow/assets/32446706/5210a006-e44c-49c7-8174-b58ade21c44b)

### Install Apache Airflow Using Helm chart 
Reference - https://hungngph.medium.com/airflow-on-kubernetes-with-helm-c795545325dc
```
   46  helm repo add apache-airflow https://airflow.apache.org
   47  helm repo update
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

```


```


#  Method-2 by using Docker 
- Create Docker file
- Use docker build to run the container from docker file
- Mount the Dags folder to docker conatiner
- Expose the docker container on the listener port to access the Airflow GUI
- https://harshalpagar.medium.com/running-airflow-with-docker-on-developer-environment-9c1c9559668c 
  

### Rquired Tools

- Install python3
  ```
  sudo apt install python3.8 -y 
  ```
- Install Docker
  ```
  sudo apt install docker.io -y 
  ```
#### Create new Dockerfile and copy the below code to it
```
FROM apache/airflow:2.5.1-python3.9

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

USER root

RUN apt-get update && apt-get install -y \
    wget

COPY start.sh /start.sh
RUN chmod +x /start.sh
USER airflow
ENTRYPOINT ["/bin/bash","/start.sh"]

```
#### Create start.sh file
```
#!/bin/bash
airflow standalone
```
The airflow standalone command initializes the database, creates a user, and starts all components. 
standalone command execute multiple commands like - 
airflow db migrate

airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org

airflow webserver --port 8080

airflow scheduler `

#### Build the docker image
```
docker build . -t airflow-local
```
> Check the built docker image "airflow-local"

![image](https://github.com/anand40090/Apache-Airflow/assets/32446706/37641169-e70d-4be2-9356-d261d3c8f3f3)

> Run the image
```
docker run -p 8080:8080 -v /home/admin1/Airflow/dags:/opt/airflow/dags  -d airflow-local

# Here replace local path of airflow DAG's repository, so that if you made changes to dags in the folder we don't have to restart docker
```

> Verify the docker container after the duild

![image](https://github.com/anand40090/Apache-Airflow/assets/32446706/808945ec-c6d5-4ec0-a202-63539d3d51a8)

##### After successful run, this will initialize airflow database, webserver and scheduler. Airflow UI will be up and running at http://localhost:8080/home

###### Go to the running container to note password generated by airflow, we need it to login in the airlfow webserver
![image](https://github.com/anand40090/Apache-Airflow/assets/32446706/e1f569ca-807b-44a5-ae19-c78077caf8d1)
![image](https://github.com/anand40090/Apache-Airflow/assets/32446706/bb646445-2f7e-48c8-95fd-7302e705e695)

##### visit http://localhost:8080/home and on login page enter username and password you noted from logs.

![image](https://github.com/anand40090/Apache-Airflow/assets/32446706/0b15bcab-570a-445f-aff2-cddb7fd4857e)

## Sample Dags and Values files 

#### values.yaml
```
airflow:
  config:
    AIRFLOW__CORE__DAGS_FOLDER: /home/admin1/Airflow/dags
```
#### my_dag.py

```  
  from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_dag',
    default_args=default_args,
    description='A simple Apache Airflow DAG',
    schedule_interval=timedelta(days=1),
)

start_task = DummyOperator(task_id='start_task', dag=dag)
end_task = DummyOperator(task_id='end_task', dag=dag)

start_task >> end_task
```
  
  

#### xample_dag.py

```
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Define default_args dictionary to specify the default parameters of the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate a DAG with the DAG ID and default_args
dag = DAG(
    'example_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),  # Run the DAG daily
)

# Define a task using BashOperator
task_hello_world = BashOperator(
    task_id='hello_world',
    bash_command='echo "Hello, World!"',
    dag=dag,
)

# Set task dependencies (if any)
# task_hello_world >> another_task

if __name__ == "__main__":
    dag.cli()
```














