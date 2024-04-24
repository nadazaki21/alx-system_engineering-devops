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

file_line { 'redirection':
    path  => '/etc/nginx/sites-available/default',
    line  => ' location /redirect_me {\nreturn 301 permanent;\n    }',
    after => '^server_name',
}


exec {'start_server':

command => '/usr/bin/sudo /usr/sbin/service nginx start',
}