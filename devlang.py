from subprocess import call
import sys
import os


def string_to_devlang(line):
	current_line = ""
	for ch in line:
		current_line += ('developers ' * (ord(ch) - 1)) + 'developers! '
	return current_line

def convert_file_to_devlang(file_lines):
	dev_file = []
	for i, line in enumerate(file_lines):
		dev_file.append(string_to_devlang(line))
	return dev_file

def write_devlang_to_file(dev_conv_list, filename):
	output_file = open(os.path.splitext(filename)[0] + '.developers', 'w')
	output_file.write("%s\n" % string_to_devlang(os.path.splitext(filename)[1]))
	for line in dev_conv_list:
		output_file.write("%s\n" % line)
	output_file.close()

def devlang_string_to_original(line):
	tokens = line.split('! ')
	original_words = ''
	for character in tokens:
		original_words += chr(len(character.split())) # might have to minus 1
	return original_words

def devlang_to_original(file_lines):
	converted_lines = []
	for line in file_lines:
		c_line = devlang_string_to_original(line)
		c_line = c_line[:len(c_line) - 1]
		converted_lines.append(c_line)
	return converted_lines

def write_original_to_file(original_lines, filename):
	output_filename = os.path.splitext(filename)[0] + '_' + original_lines[0]
	output_file = open(output_filename, 'w')
	for line in original_lines[1:]:
		print>>output_file, line.rstrip()
	output_file.close()

def run_file(original, filename):
	output_filename = 'asdfSuperSecretTemp'
	write_original_to_file(original, output_filename)
	file_type = original[0]
	if file_type == '.py':
		os.system("python " + output_filename + "_.py")
	elif file_type == '.cpp':
		os.system("g++ " + output_filename + "_.cpp -o asdfTempOut")
		os.system("./asdfTempOut")
		os.system("rm asdfTempOut")
	elif file_type == '.c':
		os.system("gcc " + output_filename + "_.c -o asdfTempOut")
		os.system("./asdfTempOut")
		os.system("rm asdfTempOut")
	elif file_type == '.rb':
		os.system("ruby " + output_filename + "_.rb")
	elif file_type == '.java':
		os.system("javac " + output_filename + "_.java")
		os.system("java " + output_filename + "_.class")
		os.system("rm " + output_filename + "_.class")
	os.system("rm " + output_filename + "_.*")

def main():
	filename = sys.argv[1]
	convert_to_dev = sys.argv[2]
	file_t = open(filename, 'r')
	file_lines = (file_t.read()).split('\n')
	file_t.close()
	if convert_to_dev == 'todev':
		dev_conv_list = convert_file_to_devlang(file_lines)
		write_devlang_to_file(dev_conv_list, filename)
	else:
		original_reconstruction = devlang_to_original(file_lines)
		if convert_to_dev == 'rundev':
			run_file(original_reconstruction, filename)
			# pass
		elif convert_to_dev == 'fromdev':
			write_original_to_file(original_reconstruction, filename)
if __name__ == '__main__':
	main()
