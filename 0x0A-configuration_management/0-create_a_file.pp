# Create a file named school with file owner and group www-data
file { '/tmp/school':
  content =>  'I love Puppet',
  mode    =>  '0744',
  owner   =>  'www-data',
  group   =>  'www-data',
}
