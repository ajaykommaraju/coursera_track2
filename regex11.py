import sys
import os 
import re 

#  write a function error_search that takes log_file as a parameter and returns returned_errors

def error_search(log_file):
    error = input("what is the error? ")
    returned_errors = []
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split())):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    return returned_errors

# create an output file 
def file_output(returned_errors):
      with open(os.path.expanduser('C:\Users\kkumar19\Documents\coursera_python_track2') + 'errors_found.log', 'w') as file:
          for error in returned_errors:
              file.write(error)
          file.close()

if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)
        



