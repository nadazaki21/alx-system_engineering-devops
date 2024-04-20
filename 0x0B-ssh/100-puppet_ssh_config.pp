# Your SSH client configuration must be configured to refuse to authenticate using a password
# Your SSH client configuration must be configured to use the private key ~/.ssh/school



file_line { 'config_file_pass':
        ensure  => 'present',
        path    => '/etc/ssh/ssh_config',
        line   => '   PasswordAuthentication no',
}

file_line { 'config_file_key':
        
        ensure  => 'present',
        path    => '/etc/ssh/ssh_config',
        line   => '   IdentityFile ~/.ssh/school',
}


file_line { 'remove_pass':
      ensure            => 'present',
      path              => '/etc/ssh/ssh_config',
      match             => '   PasswordAuthentication no',
      match_for_absence => true,
    }

