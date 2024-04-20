# Your SSH client configuration must be configured to refuse to authenticate using a password
# Your SSH client configuration must be configured to use the private key ~/.ssh/school

file { 'config_file':
        
        path    => '/etc/ssh/ssh_config',
        ensure  => 'file',
        content => file('/home/nada-zaki/alx/alx-system_engineering-devops/0x0B-ssh/files/config_file'),
        force   => 'true'
}
