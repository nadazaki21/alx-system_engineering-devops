# Install Flask and Werkzeug with specific versions using pip3


package {'Werkzeug':
        ensure   => '2.1.0',
        name     => 'Werkzeug',
        provider => 'pip3',
}

package {'flask':
        ensure   => '2.1.0',
        name     => 'flask',
        provider => 'pip3',
}
