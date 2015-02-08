def write_error(file_name, msg, location, error='Unknown'):
	errors_file = file(file_name, 'a')
	errors_file.write('ERROR: %s\n' % error)
	errors_file.write('MESSAGE: %s\n' % msg)
	errors_file.write('LOCATION: %s' % location)
	errors_file.write('\n\n')
	errors_file.close()