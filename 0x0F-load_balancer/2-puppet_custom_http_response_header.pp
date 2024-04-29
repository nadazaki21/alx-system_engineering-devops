# automate the task of creating a custom HTTP header response, but with Puppet.

exec { 'update':

    command => 'sudo apt update',
}


package { 'install_nginx':

    name    => 'nginx',
    provider => 'apt',
}


exec { 'export_hostname':

    command => 'export HOSTNAME=$HOSTNAME',
}


exec { 'update':

    command => 'sudo apt update',
}


exec { 'insert line':

    command => 'sed -i '57i\add_header X-Served-By $HOSTNAME always;' /etc/nginx/nginx.conf ',
}

exec { 'reload_nginx':

    command => '/etc/init.d/nginx reload',
}

