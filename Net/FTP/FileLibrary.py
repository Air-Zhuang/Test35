import os

class FileLibrary:
    @staticmethod
    def showAll():
        allFiles=",".join(os.listdir("file"))
        return allFiles
    @staticmethod
    def download(connect,filename):
        with open("file/"+filename, "rb") as f:
            data2 = f.read(1024 * 1024)
            connect.send(data2)
    @staticmethod
    def writefile(filename,response):
        with open("file/"+filename, "wb") as f:
            f.write(response)
            print("Download finished")

if __name__ == '__main__':
    fil=FileLibrary()
    print(fil.showAll())
