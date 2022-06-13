#Function to Create SFTP connection and uplaod data to dataframe
def getSFTPData(path, stringpart):
    #Create connection with SFTP
    srv = pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts)
    srv.cwd(path)
    directory_structure = srv.listdir_attr()
    #Read the allocation file from SFTP
    for f in sorted(directory_structure, key=lambda k: k.st_mtime, reverse=True):
        if stringpart.lower() in f.filename.lower():
            with srv.open(f.filename) as f1:
                try:
                    df_n = pd.read_csv(f1)
                except:
                    df_n = pd.read_excel(f1)
        break

    #Closing the connection
    srv.close()
    return df_n
