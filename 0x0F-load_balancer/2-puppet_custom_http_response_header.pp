# automate the task of creating a custom HTTP header response, but with Puppet.

exec { 'update':
    command => '/usr/bin/apt update',
}

package { 'install_nginx':
    name     => 'nginx',
    provider => 'apt',
    require  => Exec['update'], # Ensure 'update' command is executed before installing nginx
}

exec { 'insert line':
    command     => '/usr/bin/sed -i \'57iadd_header X-Served-By $HOSTNAME always;\' /etc/nginx/nginx.conf',
    environment => ['HOSTNAME=myhostname'], # Set the HOSTNAME environment variable
    require     => Package['install_nginx'], # Ensure nginx is installed before modifying its config
}

exec { 'reload_nginx':
    command     => '/etc/init.d/nginx reload',
    require     => Exec['insert line'], # Ensure 'insert line' command is executed before reloading nginx
}


