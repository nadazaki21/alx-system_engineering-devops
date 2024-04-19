# manifest that kills a process named killmenow.

exec { 'killmenow':
    command => ['/','pkil -f killmenow'],
}
