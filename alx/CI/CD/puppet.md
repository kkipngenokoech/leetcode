# PUPPET

this is an open source configuration management tool

Puppet is designed to help automate the management and configuration of software and infrastructure. It allows you to define the desired state of your systems and applications using a declarative language. With Puppet, you can define configurations, policies, and dependencies for your software and infrastructure components. These configurations can be version-controlled and tested, allowing for consistent and reproducible deployments.

## PUPPET TERMS

**Puppet Master:** the master server that controls configuration on the nodes

**Puppet Agent Node:** a node controlled by the Puppet Master

**Manifest:** a file that contains a set of instructions to be executed

**Resource:** a portion of the code that declares how its state is supposed to be changed

**Module:** a collection of manifests and other related files organized in a pre-defined way to facilitate sharing and reusing parts of the provisioning.

**Class:** normal classes in programming languages, it helps organize our code so that we can easily reuse portions of the code.

**Facts:** global variables containing information about the system - i.e network interfaces and operating systems.

**Services:** used to trigger service status changes, i.e restrart or stopping services

## PUPET SYNTAX

puppet is normally written in DSL - domain specific language that is based on ruby

in puppet tasks or steps are defined by declaring resources which can represent packages, files, services, users and commands.

in resources, we can check if a package is installed and if not we can trigger a service  - package installation

```ruby
package { 'nginx':
ensure => installed
}
```

the 'nginx' is an identifier for the resource same is 'apg-get-update' below

```ruby
exec {'apg-get update':
command => '/usr/bin/apg-get update'
}
```

often we need to reference other resources from with a resource, that is why we need an identifier.

when writing manifests, it is important to know that commands are not essentially executed as they are defined
