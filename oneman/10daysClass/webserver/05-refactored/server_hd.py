import sys
from http.server import HTTPServer,BaseHTTPRequestHandler
import os
import subprocess

PORT = 8111
class ServerException(Exception):
    pass

class RequestHandler(BaseHTTPRequestHandler):
    """Handle Http requests by returning a fixed 'page'"""
    Page='''\
        <html>
        <body>
        <table>
        <p>hi whf15! web server</p>
        <tr>  <td>Header</td>         <td>Value</td>          </tr>
        <tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>            <tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
        <tr>  <td>Client port</td>    <td>{client_port}s</td> </tr>
        <tr>  <td>Command</td>        <td>{command}</td>      </tr>
        <tr>  <td>Path</td>           <td>{path}</td>         </tr>
        </table>
        </body>
        </html>
        '''

    Error_Page = """\
        <html>
            <body>
            <h1>Error accessing {path}</h1>
            <p>{msg}</p>
            </body>
        </html>
    """
    #Handle a Get request.
    def do_GET(self):
        try:
            # Get current path
            full_path = os.getcwd() + self.path
            if not os.path.exists(full_path):
                #if current path does not exists
                raise ServerException("'{0}' not found".format(self.path))
            elif os.path.isfile(full_path):
                #current path exists
                self.handle_file(full_path)
            else:
                raise ServerException("'{0}' not found".format(self.path))
        except Exception as msg:
            self.handle_error(msg)
        
    # def create_page(self):
    #     page=self.Page.format(date_time=self.date_time_string(),client_host=self.client_address[0],
    #             client_port=self.client_address[1],command=self.command,path=self.path
    #             )
    #     # print(page)
    #     return page

    def handle_file(self,full_path):
        try:
            with open(full_path,"rb") as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)
    

    def handle_error(self,msg):
        content = self.Error_Page.format(path=self.path,msg=msg)
        self.send_content(bytes(content,'utf-8'))

    def send_content(self, content):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.send_header("Content-Length",str(len(content)))
        self.end_headers()
        self.wfile.write(content)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        server_address = ('', PORT)
        server = HTTPServer(server_address, RequestHandler)
        print('strating the web server...127.0.0.1:'+str(PORT))
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the web server...')
        server.socket.close()    
