# this Puppet manifest ensures certain  attriubutes about a file resource.

node default {
    file { '/tmp/school',
        path => '/tmp/school'
        ensure => '/tmp/school'
        owner => 'www-data'
        group => 'www-data'
        content => 'I love Puppet'

    }
}
