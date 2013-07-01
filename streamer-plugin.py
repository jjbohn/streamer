import sublime, sublime_plugin
import sys
import os.path

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path += [BASE_PATH] + [os.path.join(BASE_PATH, f) for f in ['zope', 'twisted']]
from twisted.internet import reactor, protocol
from twisted.protocols import basic
from threading import Thread

__version__      = '0.0.1'
__authors__      = ['"John Bohn" <jjbohn@gmail.com>']

class EchoProtocol(protocol.Protocol):
  def dataReceived(self, data):
    self.transport.write(data)

class EchoFactory(protocol.Factory):
  def buildProtocol(self, addr):
    return Echo()



if not reactor.running:
  print(reactor.running)
  # reactor.callFromThread(reactor.stop)
  # reactor.listenTCP(12348, EchoFactory())
  # Thread(target=reactor.run, args=(False,)).start()

class EventDispatch(sublime_plugin.EventListener):
  def on_load(self, view):
    print(view.file_name(), "just got loaded")

  def on_pre_save(self, view):
    print(view.file_name(), "is about to be saved")

  def on_post_save(self, view):
    print(view.file_name(), "just got saved")

  def on_new(self, view):
    print("new file")

  def on_modified(self, view):
    print(view.file_name(), "modified")

  def on_activated(self, view):
    print(view.file_name(), "is now the active view")

  def on_close(self, view):
    print(view.file_name(), "is no more")

  def on_clone(self, view):
    print(view.file_name(), "just got cloned")
