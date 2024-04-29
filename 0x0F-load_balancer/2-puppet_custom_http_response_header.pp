# automate the task of creating a custom HTTP header response, but with Puppet.

exec { 'update':

    command => '/usr/bin/apt update',
}


package { 'install_nginx':

    name    => 'nginx',
    provider => 'apt',
}


exec { 'insert line':

    command => '/usr/bin/sed -i \'57i\add_header X-Served-By $HOSTNAME always;\' /etc/nginx/nginx.conf ',
    environment => ['HOSTNAME=$HOSTNAME'],
}

exec { 'reload_nginx':

    command => '/etc/init.d/nginx reload',
    environment => ['HOSTNAME=$HOSTNAME'],
}

