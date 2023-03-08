#https://code.visualstudio.com/docs/python/python-tutorial
#https://medium.com/edureka/kivy-tutorial-9a0f02fe53f5
#https://allanchain.github.io/ProgramingNotes/kivy/Buildozer/
#https://stackoverflow.com/questions/61362147/build-failure-no-main-pyo-found-in-your-app-directory
#https://developer.android.com/studio?gclid=CjwKCAiAr4GgBhBFEiwAgwORrVBA8VRX_ssR9Aj8Klzsp-bl2bcf48hAmNBcn-RSwfWjKX6J5SNXEhoC74wQAvD_BwE&gclsrc=aw.ds
#/home/mdelgert/test/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/dists/myapp/build/outputs/apk/debug/myapp-debug.apk myapp-debug-0.1.apk
#https://www.geeksforgeeks.org/how-to-install-an-apk-on-the-emulator-in-android-studio/
#buildozer android debug
#buildozer android debug deploy
#msg = "test"
#print(msg)

from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string('''
FloatLayout:
    canvas.before:
        Color:
            rgba: 0, 1, 0, 1
        Rectangle:
            # self here refers to the widget i.e FloatLayout
            pos: self.pos
            size: self.size
    Button:
        text: 'Hello Matthew!'
        size_hint: .5, .5
        pos_hint: {'center_x':.5, 'center_y': .5}
''')

class MainApp(App):

    def build(self):
        return root

if __name__ == '__main__':
    MainApp().run()