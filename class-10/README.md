# Class 10

## Class Outline

1. Warm-Up
1. Review
1. Lecture
1. Demo
1. Lab

## Overview

Networking in the AWS cloud differs substantially from traditional on-prem LANs. Understanding how to build efficient and resilient network infrastructure on a cloud platform is an important skill.

## How does this topic fit?

**Where we've been**:
In the previous class we studied traffic mirroring.

**What are we focusing on today**:
Today, we'll be building networking infrastructure in the AWS Cloud.

**Where we're headed**:
Next module's theme is Network Administration, expect to be learning about Active Directory and Domain Controllers.

## Cloud Networking

### Why
- Cloud networking allows organizations to easily scale their network infrastructure up or down based on their needs. This is crucial for handling increased traffic during peak times or when expanding operations. Traditional networking often requires significant time and effort to scale, whereas cloud networking can be adjusted almost instantly.
- Cloud networking can help reduce infrastructure costs by allowing organizations to pay only for the resources they use. Traditional networking often involves significant upfront investments in hardware, whereas cloud networking follows a pay-as-you-go model, which can lead to cost savings.
- Cloud providers offer data centers in multiple regions around the world. This global presence allows organizations to expand their reach and provide low-latency access to users and customers worldwide, improving the overall user experience.
- Cloud networking often includes built-in redundancy and disaster recovery options. Data and services can be replicated across multiple data centers, ensuring business continuity even in the face of hardware failures or natural disasters.
- Cloud providers invest heavily in security measures, which can help organizations protect their data and applications. They offer a wide range of security services, including firewalls, encryption, and identity and access management tools.

### What
- _______ is the delivery of computing services (such as servers, storage, databases, networking, software, and analytics) over the internet to offer faster innovation, flexible resources, and cost savings.
- _______ are companies that offer cloud computing services, such as Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP), and IBM Cloud.
- _______ is a private, logically isolated section of a public cloud where an organization can launch its resources while maintaining control over network configurations.
- _______ is the automatic adjustment of resources based on traffic or demand to maintain optimal performance and cost efficiency.
- _______ is a network-based security feature in cloud environments that acts as a virtual firewall, controlling inbound and outbound traffic to and from cloud resources.
- _______ is a distributed network of servers that delivers web content and assets to users based on their geographic location, improving website performance and reducing latency.
- _______ is a security framework that manages user access and permissions to cloud resources, ensuring only authorized users can access them.

### How
Cloud computing is a technology that allows users and organizations to access and use computing resources (such as servers, storage, databases, networking, software, and more) over the internet, often referred to as "the cloud." Here's an explanation of how cloud computing works:
- **Infrastructure Setup by Cloud Providers**
  - Cloud computing begins with cloud service providers (CSPs) like Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform (GCP) establishing data centers and building a vast infrastructure of servers, storage, and networking equipment around the world.
- **User/Client Access**
  - Users or clients access cloud services and resources via the internet using devices like computers, smartphones, or tablets.
  - To access cloud resources, users typically use a web browser or specialized software applications provided by the CSPs.
- **Service Models**
  - Cloud computing offers various service models, including:
    - **Infrastructure as a Service (IaaS):** Users can rent virtualized computing resources like virtual machines (VMs) or storage.
    - **Platform as a Service (PaaS):** Users can develop, run, and manage applications without worrying about underlying infrastructure.
    - **Software as a Service (SaaS):** Users access software applications hosted and maintained by the CSP over the internet.
- **Deployment Models**
  - Cloud computing also has different deployment models, including:
    - **Public Cloud:** Resources are owned and operated by a third-party CSP and shared among multiple customers.
    - **Private Cloud:** Resources are dedicated to a single organization and may be hosted on-premises or by a third-party provider.
    - **Hybrid Cloud:** A combination of public and private clouds, allowing data and applications to be shared between them.
- **Resource Provisioning**
  - Users or organizations provision (allocate) computing resources based on their specific needs. This can include VMs, storage, databases, and more.
  - With public cloud providers, resource provisioning can be done through a web-based console or via APIs (Application Programming Interfaces).
- **Resource Management and Virtualization**
  - Cloud providers use virtualization technologies to abstract and pool physical resources. Virtualization allows multiple virtual instances (e.g., VMs) to run on the same physical hardware.
- **Networking and Security**
  - Cloud networking involves the setup of virtual networks, subnets, and security groups to control traffic and isolate resources.
  - Security measures like firewalls, encryption, and identity and access management (IAM) are implemented to protect data and applications.
- **Data Storage**
  - Cloud providers offer various storage services, including object storage, block storage, and databases.
  - Users can store data in these services, and cloud providers manage data redundancy, backup, and availability.
- **Scaling and Load Balancing**
  - Users can scale their resources up or down based on demand. This can be done manually or automatically through services like auto-scaling.
  - Load balancers distribute traffic across multiple servers or resources to ensure high availability and performance.
- **Data Processing and Analytics**
  - Cloud computing platforms often provide tools and services for data processing, analytics, and machine learning, making it easier to extract insights from large datasets.
- **Monitoring and Management**
  - Cloud users have access to dashboards and management consoles that provide real-time insights into resource usage, performance, and costs.
  - Automation and orchestration tools help manage and optimize resources efficiently.
- **Billing and Cost Management**
  - Cloud users are billed based on their actual resource usage, typically on a pay-as-you-go or subscription basis.
  - Cost management tools help users track and control their spending.
- **Backup and Disaster Recovery**
  - Cloud providers offer backup and disaster recovery services to ensure data and application availability in case of failures or disasters.
- **Continuous Updates and Maintenance**
  - Cloud providers continually update and maintain their infrastructure, including security patches and hardware upgrades, to ensure reliability and security.
- **Compliance and Regulations**
  - Cloud providers adhere to various compliance standards and regulations to ensure data security and privacy, which can be important for businesses in regulated industries.

### Experimentation and Discovery Ideas
- What are some common misconceptions people have about cloud computing? How might these misconceptions affect their decision-making when considering cloud services for their businesses or projects?
- Imagine you're responsible for managing IT infrastructure for a small business. What factors would you consider when deciding whether to migrate to the cloud or continue using on-premises solutions?
- Consider the environmental impact of cloud computing. How might the shift to cloud services affect energy consumption and carbon emissions? Are there potential benefits or drawbacks in terms of sustainability?
- In the context of cloud security, what are some common concerns or criticisms people have about storing sensitive data in the cloud? How can organizations address these concerns effectively?
- What are the economic implications of cloud computing for different types of businesses? How might startups benefit from cloud services compared to established enterprises?
- In a world increasingly reliant on cloud services, what ethical considerations should individuals and organizations keep in mind when handling data, privacy, and security?
- Think about the future of cloud computing. What emerging trends or technologies do you anticipate will shape the industry, and how might they impact the way we use and think about cloud services?


## Learning Objectives

### Students will be able to

#### Describe and Define

- VPC
  - Private subnets, and what services live within
  - Public subnets, and what services live within
- AWS EC2
- AMI
- AWS Elastic IP
- Security Group
- Internet Gateway
- NAT Gateway
- Route Table

#### Execute
- Set up a Virtual Private Cloud with a specified IPv4 CIDR block.
- Create both public and private subnets within the VPC, each with its own CIDR block.
- Establish a gateway to allow communication between VPC instances and the internet.
- Set up routing rules for directing network traffic within the VPC.
- Define inbound and outbound traffic rules for instances in the subnets.
- Launch virtual servers in both public and private subnets, configuring instance types, security groups, and networking settings.
- Verify connectivity by attempting to ping and SSH into instances in both public and private subnets.
- Create initial and revised topology diagrams of the network infrastructure.

## Helpful Resources

- [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html){:target="_blank"}
- [Default VPC and default subnets](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html){:target="_blank"}
- [VPC with public and private subnets (NAT)](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html){:target="_blank"}
- Professor Messer:
  - [Cloud Models](https://www.professormesser.com/free-a-plus-training/220-1001/cloud-models/){:target="_blank"}
  - [Cloud Computing](https://www.professormesser.com/security-plus/sy0-401/cloud-computing-2/){:target="_blank"}
- [YouTube - Amazon Web Services](https://www.youtube.com/user/AmazonWebServices){:target="_blank"}
- [Conference Event: AWS re:Invent](https://reinvent.awsevents.com/){:target="_blank"}
- AWS Certifications:
  - [AWS Certified Cloud Practitioner:](https://aws.amazon.com/certification/certified-cloud-practitioner/){:target="_blank"}
    - This is the most beginner-friendly AWS certification. It covers the basics of AWS services, architecture, security, and pricing. It's designed for individuals with non-technical backgrounds or those who want to get a broad overview of AWS.
  - [AWS Certified Solutions Architect – Associate:](https://aws.amazon.com/certification/certified-solutions-architect-associate/){:target="_blank"}
    - While not as basic as the Cloud Practitioner, the Solutions Architect – Associate certification is still beginner-friendly. It focuses on designing distributed systems on AWS and covers key services and architectural best practices.
  - [AWS Certified Developer – Associate:](https://aws.amazon.com/certification/certified-developer-associate/){:target="_blank"}
    - This certification is suitable for those interested in developing applications on AWS. It covers core AWS services, security, and best practices for developing and deploying applications.
  - [AWS Certified SysOps Administrator – Associate:](https://aws.amazon.com/certification/certified-sysops-admin-associate/){:target="_blank"}
    - This certification is geared toward individuals who want to focus on operations tasks such as managing and maintaining AWS resources. It covers system operations, deployment, and troubleshooting.

## Notes

- What are the key differences between AWS and other major cloud service providers like Microsoft Azure and Google Cloud Platform (GCP)? How should one decide which cloud provider to choose for a specific project or organization?
- What is the AWS Well-Architected Framework, and why is it important when designing solutions on AWS? How can it help ensure the reliability, performance, and cost-effectiveness of your applications?
- What is the significance of AWS Identity and Access Management (IAM)? How does IAM play a crucial role in managing security and permissions within AWS?
- What are the best practices for optimizing cost in AWS? Are there any specific tools or services that can help identify cost-saving opportunities within an AWS environment?
- What is serverless computing, and how does AWS Lambda fit into the serverless landscape? What are some common use cases for AWS Lambda?
- What is Amazon S3 (Simple Storage Service), and how can it be used for data storage and backup? What are the various storage classes available in Amazon S3, and when should each be used?
- What is AWS Elastic Beanstalk, and how does it simplify the deployment and management of web applications? How does it differ from other AWS compute services like EC2 and ECS?
- What are AWS Regions and Availability Zones, and why are they important for ensuring high availability and disaster recovery in AWS deployments? How should multi-region architectures be designed?
- How can AWS CloudFormation be used for infrastructure as code (IaC)? What are the benefits of defining and managing AWS resources through code, and what are some common IaC best practices?
- What are AWS Marketplace and AWS Marketplace Seller Private Offers? How can organizations leverage these platforms to discover and procure third-party software and services?
- What are Amazon RDS (Relational Database Service) and Amazon DynamoDB, and how do they differ in terms of database management? What factors should influence the choice between these two database services?
- What is AWS CloudWatch, and how does it facilitate monitoring and observability of AWS resources? What are some key CloudWatch metrics and alarms that should be set up to ensure system health?
