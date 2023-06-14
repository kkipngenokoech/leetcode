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

let say for example there's a script you want to execute, but you first have to check if some package is installed, like you want to install python but you have to confirm if pip3 is installed first.

i.e:

```ruby
package { 'install tip':
ensure => 'installed',
}

exec { 'install python':
command => '/usr/bin/install python',
require => package['install tip']
}
```

the require option receives a parameter which references another package

let say you want to ensure that a task is executed first before another, you can use the `before` option

```ruby
package {'curl':
    ensure => 'installed'
    before => Exec['install script']
}

exec { 'install script'
    command => 'script to install'
}
```

so a manifest ideally is a collection of resource declarations and it is saved using the extension `.pp`

the thought process of installing applications in ubuntu is normally to `sudo apt update` the repositories first and then you install the package you want to install.

lets write a manifest to install keras package in our ubuntu:

```ruby
exec { 'apt-get update':
    command => 'sudo apt update'
}
package { 'install keras':
    ensure => 'pip install keras"
    require => package['apt-get update']
}
```

ideally you should:

```ruby
# Manifest: keras_install.pp

# Update package lists
exec { 'apt-update':
  command => 'apt-get update',
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
  require => Class['apt']
}

# Install Python3 and pip
package { ['python3', 'python3-pip']:
  ensure => installed,
}

# Install Keras using pip
package { 'keras':
  provider => 'pip',
  ensure   => latest,
  require  => Package['python3-pip'],
}

# Optionally, install other dependencies
package { ['numpy', 'tensorflow']:
  ensure => installed,
}
```

## Variables

variables can be defined at any point in your manifest and this is how they are defined:

```ruby
$package = 'Keras'

package { $package:
    ensure => 'installed',

}
```

you can also define a list/arrays as a variable at any point in your manifest

```ruby
$packages = ['python3', 'python3-pip', 'keras', 'pytorch', 'tensorflow']

package { $packages:
    ensure => 'installed',
}
# you can as well iterate over the packages this way:

$packages.each |String $package| {
    package { $package:
        ensure => 'installed',
    }
}
```

this packages will later be iterated on and installed.

## conditional statements

Puppet also supports conditional statements that is the `if/else` statement and `case` statements

```ruby
if $packages != ['python3', 'python3-pip'] {
    warning('this are not supported')
}
else {
    notify {'Good to go!'}
}
```

in some cases you want some script to execute based on the condition of another command, for that you will:

```ruby
exec { 'test':
    command => 'the command to be run',
    onlyIf => 'the condition to check/the command to execute'
}
```

Similarly, unless will execute the command all times, except when the command under unless exits successfully, so you can replace the `onlyif` command above with `unless` to achieve the opposite effect

## Working with Templates

Templates are typically used to set up configuration files, allowing for the use of variables and other features intended to make these files more versatile and reusable. 

Puppet supports two different formats for templates:

1. Embedded Puppet (EPP)
2. Embedded Ruby (ERB).

Below is an example of an ERB template for setting up an Apache virtual host, using a variable for setting up the document root for this host:

```ruby
# vhost.erb
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot <%= @doc_root %>

    <Directory <%= @doc_root %>>
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```

to use this template, we are going to create a file resource:

```ruby
file { "/etc/apache2/sites-available/000-default.conf":
    ensure => "present",
    content => template("apache/vhost.erb") 
}  
```

## Defining/Triggering service resources

used to make sure services are initialized and enabled. They are also used to trigger service restarts.

```ruby
service { 'apache2':
    ensure => running,
    enable => true
}
```

