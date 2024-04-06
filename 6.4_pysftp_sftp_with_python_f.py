'''
Python can be used to transfer files to/from server using ftp/sftp
Modules are used
Python has ftplib module - FTP may be disabled as not secured
SFTP / SCP is preferred method
Python requires 3 modules - install using command prompt / server:
pip install pycrypto
pip install paramiko
pip install pysftp
Within python script:
'''

import pysftp as sftp

def push_file_to_server():
    # Disable host key checking (NOT RECOMMENDED FOR PRODUCTION)
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None

    # Connect to the server
    s = sftp.Connection(host='167.99.43.15', username='root', password='elm86Court', port=22, cnopts=cnopts)

    local_path = "testme.txt"
    remote_path = "/home/testme.txt"

    # Transfer the file
    s.put(local_path, remote_path)

    # Close the connection
    s.close()

def get_file_from_server():
    # Disable host key checking (NOT RECOMMENDED FOR PRODUCTION)
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None

    # Connect to the server
    s = sftp.Connection(host='167.99.43.15', username='root', password='elm86Court', port=22, cnopts=cnopts)

    local_path = "testme.txt"
    remote_path = "/home/testme.txt"

    # Transfer the file
    s.get(remote_path, local_path)

    # Close the connection
    s.close()

push_file_to_server()
get_file_from_server()
