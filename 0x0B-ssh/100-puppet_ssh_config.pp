# Your SSH client configuration must be configured to refuse to authenticate using a password
# Your SSH client configuration must be configured to use the private key ~/.ssh/school

file { 'config_file':
        
        path    => '/etc/ssh/ssh_config',
        ensure  => 'file',
        content =>  file('0x0B-ssh/config_file'),
}
