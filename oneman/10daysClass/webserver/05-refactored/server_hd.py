import sys
from http.server import HTTPServer,BaseHTTPRequestHandler
import os
import subprocess

PORT = 8111

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
    #Handle a Get request.
    def do_GET(self):
        page = self.create_page()
        self.send_page(page)

    def create_page(self):
        page=self.Page.format(date_time=self.date_time_string(),client_host=self.client_address[0],
                client_port=self.client_address[1],command=self.command,path=self.path
                )
        # print(page)
        return page

    def send_page(self, page):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.send_header("Content-Length",str(len(page)))
        self.end_headers()
        self.wfile.write(bytes(page,'utf-8'))


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
