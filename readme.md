To Do List:
1. utilise helm plugins with helm chart
2. find a business use case for this helm charts deployment and develop
3. upgrade our helm chart to include additional features like autoscaling service accounts e.g. 
4. add metrics api to cluster so we can monitor the usage and scale upgrade
5. we can develop application docker further or ask simon and kyle for their application and package it into the cluster
6. add networking functionality ingress egress e.g.
7. add liveness and readiness for autoscaler and stress tests
8. do it locally then use cicd
9. get docker working with minikube change values.yaml with fastapi image also keep the mount and also change the copt in fastapi to the mount and use minikube docker env to build once then i am fine and can potentially have the endpoint working