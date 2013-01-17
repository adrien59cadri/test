#pragma once
#include "Content.h"
#include "ControlCenter.h"

class MyJUCEApp;
	class MyAppW : public DialogWindow{
	public:
	
		MyAppW(MyJUCEApp*app);
		virtual void closeButtonPressed(){
			_app->quit();
		}
	private:
		JUCEApplication * _app;
		Content _content;
	};
      class MyJUCEApp  : public JUCEApplication
        {
        public:
            MyJUCEApp()
            {
            }

            virtual ~MyJUCEApp()
            {
            }

            virtual void initialise (const String& commandLine)
            {
                myMainWindow = new MyAppW(this);
                myMainWindow->setBounds (100, 100, 400, 500);
                myMainWindow->setVisible (true);
            }
			IControlCenter&getCC(){return _cc;}
            virtual void shutdown()
            {
                myMainWindow = 0;
            }

            virtual const String getApplicationName()
            {
                return "Super JUCE-o-matic";
            }

            virtual const String getApplicationVersion()
            {
                return "1.0";
            }

        private:
            ScopedPointer <DialogWindow> myMainWindow;
			ControlCenter _cc;
        };

        // this creates wrapper code to actually launch the app properly.
  