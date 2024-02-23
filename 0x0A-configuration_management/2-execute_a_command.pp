# Using Puppet to create a manifest that kills a process named killmenow.
exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill -9 killmenow',
}
