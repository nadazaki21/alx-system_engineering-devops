# Puppet manifest to intsall flask from pip3.

package {'flask':
        ensure   => '2.1.0',
        name     => 'flask',
        provider => 'pip3',
}
