
import sys
from http.server import HTTPServer,BaseHTTPRequestHandler
import os
import subprocess

PORT = 8112

class RequestHandler(BaseHTTPRequestHandler):
    """Handle Http requests by returning a fixed 'page'"""
    #Page to send back
    Page=b'''\
        <html>
            <body>
                <p>Hello ,web!,i'am whf15</p>
            </body>
        </html>
        '''

        #Handle a Get request.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.send_header("Content-Length",str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page)
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
