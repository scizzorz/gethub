#!/usr/bin/env python
import getopt, getpass, os, subprocess, sys
import github

def _shell(cmd):
	print '$ {}'.format(cmd)
	subprocess.check_output(cmd, shell = True)
	print

def main(args):
	username = None
	password = None
	fetchGists = False

	# Parse options
	opts, _ = getopt.getopt(args, 'gau:', ['gists', 'auth', 'user='])
	for opt, arg in opts:
		if opt in ('-a', '--auth'):
			username = raw_input('Username? ')
			password = getpass.getpass('Password? ')
		elif opt in ('-u', '--user'):
			if ':' in arg:
				username, password = arg.split(':')
			else:
				username = arg
		elif opt in ('-g', '--gists'):
			fetchGists = True

	# Exit if no username set
	if not username:
		print 'Please provide a username with -u or ask for a username prompt with -a.'
		sys.exit(0)

	# Authenticate if password set
	if not password:
		API = github.GitHub()
		if fetchGists:
			repos = API.users(username).gists()
		else:
			repos = API.users(username).repos()

	# Anonymous if no password set
	else:
		API = github.GitHub(username = username, password = password)
		if fetchGists:
			repos = API.gists()
		else:
			repos = API.user().repos()

	# Iterate repos and clone
	repos = repos.get()
	for repo in repos:
		if fetchGists:
			url = repo.git_pull_url
			path = repo.id
		else:
			url = repo.ssh_url
			path = repo.name

		# Don't clone if it already exists in this directory
		if not os.path.exists(path):
			_shell('git clone {}'.format(url))
		else:
			print '{} exists, aborting clone'.format(path)

if __name__ == '__main__':
	main(sys.argv[1:])
