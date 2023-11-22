# Class 07

## Class Outline

1. Warm-Up
1. Review
1. Lecture
1. Demo
1. Lab

## Overview

Infrastructure deployment is an important role for the systems administrator. Public-facing infrastructure such as web servers present unique security and operational challenges compared to endpoints. Configuring a web server requires an understanding of firewall, networking design, network protocols, and security practices.

## How does this topic fit?

**Where we've been**:
Previously we used NAT to translate IPs between sites.

**What are we focusing on today**:
Today, we'll be spinning up our own Linux-based web server.

**Where we're headed**:
Next class we'll be deploying a network access control system.

## Web Server Deployment

### Why
- Deploying a web server allows your website or web application to be accessible to users on the internet. Without deployment, your site would only exist on your local development environment, making it inaccessible to the wider audience.
- Proper web server deployment techniques can help your site handle increased traffic. By deploying your application on scalable infrastructure, you can ensure that your website remains responsive even as the number of users and requests grows.
- A well-deployed web server is typically more reliable. It can withstand hardware failures, network issues, and other problems that might affect the availability of your website. Techniques like load balancing and redundancy can be used to enhance reliability.
- Deploying a web server allows you to fine-tune its performance. You can configure settings, optimize database queries, and use caching mechanisms to ensure your website loads quickly and provides a smooth user experience.
- Learning web server deployment often goes hand in hand with understanding CI/CD pipelines. This enables you to automate the process of testing, building, and deploying your application, making it easier to maintain and update.
- By deploying your web server in a cloud environment, you can optimize costs. Cloud providers offer scalability, allowing you to pay only for the resources you use, which can be cost-effective compared to maintaining physical servers.
- Deploying your web server globally through content delivery networks (CDNs) can reduce latency and ensure that your website loads quickly for users around the world.
- Deployment often involves using version control systems like Git, which allows you to track changes, collaborate with others, and easily roll back to previous versions if issues arise.
- Learning about web server deployment is a valuable skill for developers and system administrators. It exposes you to various technologies, tools, and best practices in the field of web development and infrastructure management.
- Proficiency in web server deployment is in demand in the IT industry. Many companies look for professionals who can effectively deploy and manage web applications, making it a valuable skill for career advancement.

### What
- _______ is the software or hardware component that serves web content to users' browsers when they request a webpage. Common web server software includes Apache, Nginx, and Microsoft Internet Information Services (IIS).
- _______ is the process of making a web application or website accessible on the internet, typically involving the installation, configuration, and maintenance of server infrastructure.
- _______ is the underlying hardware, software, and networking components that support a web server or web application. This can include servers, databases, load balancers, and more.
- _______ is the practice of using remote servers hosted on the internet (in the cloud) to store, manage, and process data, instead of using local servers or personal computers.
- _______ is the protocol used for transferring data over the World Wide Web. It defines how web clients (browsers) and servers communicate. The additional "S" is an extension of HTTP that adds a layer of encryption (SSL/TLS) to secure data transmitted between the client and server.
- _______ is a network of geographically distributed servers that work together to deliver web content (e.g., images, videos) to users from a nearby server, reducing latency and improving load times.
- _______ is a set of practices and tools that automate the building, testing, and deployment of software applications to ensure frequent and reliable releases.
- _______ is a structured collection of data that stores information used by web applications. Common database systems include MySQL, PostgreSQL, MongoDB, and Redis.
- _______ is a service that provides server space and resources to make websites accessible on the internet. It can be shared hosting, VPS (Virtual Private Server) hosting, or dedicated hosting.
- _______ are digital certificates that encrypt data transmission between a web server and a client's browser, ensuring secure communication.

### How
A web server deployment involves a series of steps and processes to make a web application or website accessible on the internet. Here's a simplified overview of how web server deployments typically work:
- **Development and Testing**:
  - Develop your web application or website on a local development environment. This involves writing code, designing the user interface, and testing the application to ensure it functions as intended.
- **Version Control**:
  - Use version control systems like Git to track changes in your codebase. This allows you to collaborate with others, maintain a history of changes, and easily revert to previous versions if necessary.
- **Server Setup**:
  - Choose an appropriate server infrastructure, whether it's a physical server, a virtual private server (VPS), or cloud-based services from providers like AWS, Azure, or Google Cloud. Install the necessary operating system and server software (e.g., Apache, Nginx).
- **Database Setup**:
  - If your web application relies on a database (e.g., MySQL, PostgreSQL, MongoDB), set up the database server and configure it with the necessary schemas and tables to store your data.
- **Security Measures**:
  - Implement security measures, such as firewalls, intrusion detection systems, and regular software updates, to protect your server and application from potential threats.
- **Domain and DNS Configuration**:
  - Register a domain name for your website and configure DNS settings to point the domain to your server's IP address. This step allows users to access your site using a human-readable domain name.
- **SSL/TLS Certificate Installation**:
  - Secure your website by installing an SSL/TLS certificate, which encrypts data transmitted between the server and clients' browsers. This is essential for HTTPS, ensuring data privacy and security.
- **Application Deployment**:
  - Deploy your web application code to the server. This may involve using Git to pull the latest code from a repository, uploading files via FTP, or using deployment tools like Capistrano or Jenkins.
- **Web Server Configuration**:
  - Configure the web server (e.g., Apache or Nginx) to serve your web application. This includes specifying how requests should be handled, setting up virtual hosts, and configuring security settings.
- **Database Connection**:
  - Configure your web application to connect to the database server, specifying connection parameters, credentials, and database drivers.
- **Content and Assets**:
  - Upload any static assets (images, CSS, JavaScript files) to the server or leverage CDNs to distribute these assets efficiently.
- **Testing on Staging**:
  - Before making the site live, test it on a staging environment to ensure that everything works correctly in a production-like setting.
- **Continuous Integration/Continuous Deployment (CI/CD)**:
  - Implement CI/CD pipelines to automate the building, testing, and deployment of your application, ensuring reliable and frequent updates.
- **Monitoring and Logging**:
  - Set up monitoring tools and configure logging to track the performance and security of your web server and application. This helps you identify and address issues proactively.
- **Load Balancing (Optional)**:
  - If needed, use load balancers to distribute traffic across multiple servers for scalability and redundancy.
- **Scalability and Optimization**:
  - Continuously monitor and optimize server performance, scaling resources as necessary to handle increased traffic and ensuring that your web application runs efficiently.
- **Backup and Recovery**:
  - Implement backup strategies to regularly back up data and configurations, allowing for quick recovery in case of data loss or system failures.
- **Maintenance and Updates**:
  - Keep your server and application up to date with security patches, software updates, and code enhancements.
- **User Access Control**:
  - Manage user access to the server and application, setting permissions and authentication mechanisms as needed for security.
- **Documentation**:
  - Maintain documentation that outlines the server setup, configurations, and deployment processes for reference and troubleshooting.

### Experimentation and Discovery Ideas
- In the context of web server deployment, what are the potential advantages and disadvantages of using a cloud-based infrastructure compared to a physical server? How might you experiment to determine which option is more suitable for your project?
- When it comes to security in web server deployment, what are some common vulnerabilities that developers should be aware of, and how can they experiment to identify and mitigate these vulnerabilities effectively?
- Continuous Integration/Continuous Deployment (CI/CD) is a critical practice in modern web development. What are the benefits of implementing CI/CD pipelines for web server deployments? How might you experiment with different CI/CD tools and workflows to optimize your development process?
- Let's talk about scalability. What experiments could you conduct to determine when and how to scale your web server infrastructure to handle increased traffic? What metrics and tools would you use to make informed scaling decisions?
- When deploying a web server globally, what factors should you consider to ensure optimal performance and user experience in different geographic regions? How might you experiment with Content Delivery Networks (CDNs) and geo-distributed servers to achieve this?
- Web server logs contain a wealth of information about server performance and user behavior. How can you experiment with log analysis tools and techniques to gain valuable insights into your web server's operation and user interactions?
- In the context of web server deployment, what role does documentation play? How can you experiment with different documentation practices to ensure that your deployment processes are well-documented and accessible to your team?
- When considering the choice between different web server software (e.g., Apache, Nginx), what experiments could you conduct to evaluate their performance, security, and suitability for your specific project requirements?

## Learning Objectives

### Students will be able to

#### Describe and Define

- NGINX
- Apache
- Web Server
- Web Server Ports:
  - Port 80
  - Port 443
  - Port 8080
  - Port 8443
  - Port 8000
  - Port 8081
  - Port 3000
  - Port 3001
- HTML

#### Execute

- Students should be able to install NGINX on the Ubuntu Server VM and create a basic HTML webpage.
- Students should understand how to configure NGINX to serve a website on a specific port and domain name.
- Students should be able to configure the pfSense firewall, including port forwarding and allowing specific traffic through the firewall.
- Students should be able to test the web server's accessibility from both within and outside the LAN, using the appropriate IP addresses and ports.

## Helpful Resources

- [Ubuntu Official Documentation - Install NGINX](https://ubuntu.com/tutorials/install-and-configure-nginx#3-creating-our-own-website){:target="blank"}
- [YouTube: NGINX Explained in 100 Seconds](https://www.youtube.com/watch?v=JKxlsvZXG7c){:target="blank"}
- If you're serious about web server deployment as a career, consider pursuing relevant certifications, such as **AWS Certified Solutions Architect** or **Certified Kubernetes Administrator (CKA)**.

## Notes

- How can load balancing be used to distribute incoming traffic across multiple web servers, and what are the benefits of this approach?
- What considerations are important when integrating a web server with a database server, and what are some common database technologies used in web applications?
- What strategies and technologies can be employed to ensure high availability and minimize downtime in web server deployments?
- How do web application frameworks (e.g., Ruby on Rails, Django, Express.js) affect web server deployment, and what advantages do they offer?
- What is serverless computing, and how does it change the traditional approach to web server deployment?
- What are containers (e.g., Docker) and container orchestration tools (e.g., Kubernetes), and how can they simplify web server deployment and management?
- How do CDNs enhance web server performance and content delivery, and when should they be utilized?
- What are some essential security best practices for securing web servers, preventing common vulnerabilities (e.g., SQL injection, cross-site scripting), and protecting user data?
- How can authentication and authorization mechanisms be implemented on web servers to control access to different parts of a web application?
