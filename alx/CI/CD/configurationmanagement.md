# CONFIGURATION MANAGEMENT/ SERVER OCHERSTRATION

configuration management refers to the process of systematically handling changes to a system in a way that it maintains integrity over time.

Automation plays an essential role in server configuration management, automation is the heart of configuration management for servers.

There are a number of configuration management tools available in the market:

1. Puppet
2. Ansible
3. Chef
4. Salt

all this tools work towards ensuring that the state of the servers is as it has been described in your provisioning configuration scripts

## Benefits of configuration management

1. Quick provisioning of new servers - deployment of new servers (a cm tool can help you automate this process)
2. Quick recovery from critical states - when a server goes offline due to unknown circumstances, it may take along time to recover and audit a server, to run a replacement server to substitute this server can be done using CM tools
3. automate server deployment
4. easy version control for the server environment.
5. easy replication of servers

## Features of configuration management tools

### Automation Framework

Each CM tool provides a specific syntax and a set of features that you can use to write provisioning scripts. Most tools will have features that make their language similar to conventional programming languages, but in a simplified way. Variables, loops, and conditionals are common features provided to facilitate the creation of more versatile provisioning scripts.

### Idempotent Behavior

Configuration management tools keep track of the state of resources in order to avoid repeating tasks that were executed before. If a package was already installed, the tool won’t try to install it again. The objective is that after each provisioning run the system reaches (or keeps) the desired state, even if you run it multiple times. This is what characterizes these tools as having an idempotent behavior

### System Facts

Configuration management tools usually provide detailed information about the system being provisioned. This data is available through global variables, known as facts. They include things like network interfaces, IP addresses, operating system, and distribution. Each tool will provide a different set of facts. They can be used to make provisioning scripts and templates more adaptive for multiple systems.

### Templating System

Most CM tools will provide a built-in templating system that can be used to facilitate setting up configuration files and services. Templates usually support variables, loops, and conditionals that can be used to maximise versatility. For instance, you can use a template to easily set up a new virtual host within Apache, while reusing the same template for multiple server installations. Instead of having only hard-coded, static values, a template should contain placeholders for values that can change from host to host, such as NameServer and DocumentRoot.

### Extensibility

Even though provisioning scripts can be very specialized for the needs and demands of a particular server, there are many cases when you have similar server setups or parts of a setup that could be shared between multiple servers. Most provisioning tools will provide ways in which you can easily reuse and share smaller chunks of your provisioning setup as modules or plugins.

Third-party modules and plugins are often easy to find on the Internet, specially for common server setups like installing a PHP web server. CM tools tend to have a strong community built around them and users are encouraged to share their custom extensions. Using extensions provided by other users can save you a lot of time, while also serving as an excellent way of learning how other users solved common problems using your tool of choice.
