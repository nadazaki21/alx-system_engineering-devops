# manifest that kills a process named killmenow.

exec { 'killmenow':
    path    => '/',
    command => '/usr/bin/pkill -f killmenow',
}
