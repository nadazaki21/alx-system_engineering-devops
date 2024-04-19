# this Puppet manifest ensures certain  attriubutes about a file resource.


file { '/tmp/school':
    path    => '/tmp/school',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
    mode    => '0744'
}

