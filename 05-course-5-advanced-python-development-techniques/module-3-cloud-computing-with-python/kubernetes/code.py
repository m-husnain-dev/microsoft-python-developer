from kubernetes import client, config


def create_deployment_object() -> client.V1Deployment:
    """Kubernetes Deployment specs generate karta hai."""
    # Container specification
    container = client.V1Container(
        name="web-app",
        image="nginx:1.21",
        ports=[client.V1ContainerPort(container_port=80)],
        resources=client.V1ResourceRequirements(
            requests={"cpu": "100m", "memory": "128Mi"},
            limits={"cpu": "250m", "memory": "256Mi"},
        ),
    )

    # Pod Template specification
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "web-app"}),
        spec=client.V1PodSpec(containers=[container]),
    )

    # Deployment Specification (Scaling & Replicas)
    spec = client.V1DeploymentSpec(
        replicas=3,  # 3 replicas for high availability
        selector=client.V1LabelSelector(match_labels={"app": "web-app"}),
        template=template,
    )

    # Final Deployment Object
    return client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name="python-web-deployment"),
        spec=spec,
    )


def deploy_to_kubernetes():
    """Cluster par deployment apply karta hai."""
    # Local kubeconfig load karein (~/.kube/config)
    config.load_kube_config()

    apps_v1 = client.AppsV1Api()
    deployment = create_deployment_object()

    # Default namespace mein deployment create karna
    response = apps_v1.create_namespaced_deployment(
        namespace="default", body=deployment
    )
    print(f"✅ Deployment Created! Status: {response.metadata.name}")


if __name__ == "__main__":
    deploy_to_kubernetes()