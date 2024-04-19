# manifest that kills a process named killmenow.

exec { 'killmenow':
    path    => '/',
    command => 'pkill -f killmenow',
}
