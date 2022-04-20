import http.server
import socketserver
import threading
import webbrowser


class SilentServer(
    http.server.SimpleHTTPRequestHandler
):  # Opens the webserver and makes sure that there is no long log message
    protocol_version = "HTTP/1.0"

    def log_message(self, *args):
        pass


def open_webpage(PORT=8000):
    def thread_function():
        Handler = SilentServer
        try:  # make sure that server is not already running
            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print("serving at port", PORT)
                httpd.serve_forever()
        except OSError:
            pass

    mythread = threading.Thread(target=thread_function)
    mythread.start()

    url = f"http://localhost:{PORT}/"
    print(
        f"{url} will now be opened in your default browser. Closing this notebook will also shut the server"
    )
    webbrowser.open_new_tab(url)
