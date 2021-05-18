from SocketServer.SocketServer import SocketServer
from SocketServer.JobDispatcher import JobDispatcher


def main():

    job_dispatcher = JobDispatcher()

    server = SocketServer(job_dispatcher)  #用變數去接收class，是一個object

    server.setDaemon(True)
    server.serve()


    # because we set daemon is true, so the main thread has to keep alive

    while True:

        command = input()

        if command == "finish":
            break
    

    server.server_socket.close()

    print("leaving ....... ")

    
main()


        


     

    
    