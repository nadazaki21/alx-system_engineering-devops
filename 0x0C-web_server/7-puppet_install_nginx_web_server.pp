# manifest to install and configure nginx

package { 'nginx':
    name     => 'nginx',
    provider => 'apt',
    ensure   => 'installed',
}

file { 'default-page':
    path    => '/var/www/html/index.nginx-debian.html',
    ensure  => 'present',
    content => 'Hello World!',
}


exec { 'redirect':
    command => '/usr/bin/sed -i "48i\   location /redirect_me {\nreturn 301 permanent;\n    }" /etc/nginx/sites-available/default'
}


exec {'start_server':

command => '/usr/bin/sudo /usr/sbin/service nginx start',
}