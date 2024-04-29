# automate the task of creating a custom HTTP header response, but with Puppet.

exec { 'update':

    command => '/usr/bin/apt update',
}


package { 'nginx':
    name     => 'nginx',
    provider => 'apt',
    ensure   => 'installed',
}


exec { 'insert line':

    command => '/usr/bin/sed -i "65i\add_header X-Served-By ${hostname} always;" /etc/nginx/sites-available/default',
    
}

exec {'start_server':

command => '/usr/bin/sudo /usr/sbin/service nginx restart',
}

