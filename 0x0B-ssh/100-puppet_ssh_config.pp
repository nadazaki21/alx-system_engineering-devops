# Your SSH client configuration must be configured to refuse to authenticate using a password
# Your SSH client configuration must be configured to use the private key ~/.ssh/school



file_line { 'config_file_pass':

        path    => '/etc/ssh/ssh_config',
        line   => '   PasswordAuthentication no',
}

file_line { 'config_file_key':
        

        path    => '/etc/ssh/ssh_config',
        line   => '   IdentityFile ~/.ssh/school',
}


